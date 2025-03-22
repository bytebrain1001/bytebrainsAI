# Integrated Platform Environment (IPE) - System Architecture Documentation (Part 4)
________________________________________

## 8. Deployment & Integration

### 8.1 Docker Configuration
```dockerfile:Dockerfile
# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ ./src/
COPY .env .

# Expose port
EXPOSE 8501

# Run application
CMD ["streamlit", "run", "src/app.py"]
```

### 8.2 Docker Compose Setup
```yaml:docker-compose.yml
version: '3.8'

services:
  ipe-app:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - VECTOR_DB_PATH=/app/data/vector_store
    restart: unless-stopped

  vector-db:
    image: chromadb/chroma
    ports:
      - "8000:8000"
    volumes:
      - ./data/vector_store:/chroma/data
    environment:
      - CHROMA_DB_IMPL=duckdb+parquet
      - PERSIST_DIRECTORY=/chroma/data
```

## 9. Sample Data Management

### 9.1 Sample Data Generator
```python:src/utils/sample_data_generator.py
import random
from datetime import datetime, timedelta
from typing import List, Dict, Any

class SampleDataGenerator:
    def __init__(self):
        self.incident_types = ["CPU", "Memory", "Disk", "Network", "Application"]
        self.severities = ["Low", "Medium", "High", "Critical"]
        self.statuses = ["Open", "In Progress", "Resolved", "Closed"]
        self.systems = ["web-server", "app-server", "db-server", "cache-server"]

    def generate_incidents(self, count: int = 100) -> List[Dict[str, Any]]:
        """Generate sample incident data"""
        incidents = []
        for i in range(count):
            incident_type = random.choice(self.incident_types)
            severity = random.choice(self.severities)
            
            incident = {
                "id": f"INC{str(i+1).zfill(6)}",
                "title": f"{severity} {incident_type} Issue",
                "description": self._generate_incident_description(incident_type),
                "system": random.choice(self.systems),
                "severity": severity,
                "status": random.choice(self.statuses),
                "created_at": (datetime.now() - timedelta(
                    days=random.randint(0, 30)
                )).isoformat(),
                "metadata": {
                    "type": incident_type,
                    "system_type": "production",
                    "department": "IT"
                }
            }
            incidents.append(incident)
        return incidents

    def _generate_incident_description(self, incident_type: str) -> str:
        """Generate detailed incident description"""
        descriptions = {
            "CPU": [
                "High CPU utilization observed",
                "CPU throttling detected",
                "Excessive CPU usage by process"
            ],
            "Memory": [
                "Memory leak detected",
                "High memory consumption",
                "Out of memory errors"
            ],
            "Disk": [
                "Low disk space warning",
                "Disk I/O bottleneck",
                "File system errors"
            ],
            "Network": [
                "Network latency issues",
                "Packet loss detected",
                "Connection timeouts"
            ],
            "Application": [
                "Application not responding",
                "Error rate increase",
                "Service degradation"
            ]
        }
        
        base_description = random.choice(descriptions[incident_type])
        details = self._generate_technical_details(incident_type)
        
        return f"{base_description}. {details}"

    def generate_telemetry(self, 
                          system: str, 
                          hours: int = 24) -> List[Dict[str, Any]]:
        """Generate sample telemetry data"""
        data_points = []
        current_time = datetime.now()
        
        for i in range(hours * 12):  # 5-minute intervals
            timestamp = current_time - timedelta(minutes=i * 5)
            
            data_point = {
                "timestamp": timestamp.isoformat(),
                "system": system,
                "metrics": {
                    "cpu_usage": random.uniform(20, 95),
                    "memory_usage": random.uniform(30, 90),
                    "disk_usage": random.uniform(40, 85),
                    "network_latency": random.uniform(5, 200)
                },
                "metadata": {
                    "system_type": "production",
                    "location": "primary-dc"
                }
            }
            data_points.append(data_point)
        
        return data_points

    def generate_kb_articles(self) -> List[Dict[str, Any]]:
        """Generate sample knowledge base articles"""
        articles = [
            {
                "id": "KB001",
                "title": "CPU Usage Troubleshooting Guide",
                "content": """
                # CPU Usage Troubleshooting Guide

                ## Common Causes
                1. Resource-intensive processes
                2. Application memory leaks
                3. Background services
                4. Malware or unauthorized processes

                ## Diagnostic Steps
                1. Check top processes using `top` or Task Manager
                2. Review application logs
                3. Monitor system resources
                4. Analyze process behavior

                ## Resolution Steps
                1. Identify problematic processes
                2. Optimize application settings
                3. Update system resources
                4. Implement monitoring alerts
                """,
                "category": "Troubleshooting",
                "tags": ["cpu", "performance", "monitoring"]
            },
            # Add more articles...
        ]
        return articles
```

### 9.2 Data Loading and Integration
```python:src/scripts/load_sample_data.py
from utils.sample_data_generator import SampleDataGenerator
from services.data_service import DataService
from utils.vector_db_manager import VectorDBManager
from utils.openai_service import OpenAIService
from utils.logger import Logger

class DataLoader:
    def __init__(self):
        self.generator = SampleDataGenerator()
        self.data_service = DataService()
        self.vector_db = VectorDBManager()
        self.openai_service = OpenAIService()
        self.logger = Logger(__name__)

    def load_all_sample_data(self):
        """Load all sample data into the system"""
        try:
            # Generate sample data
            incidents = self.generator.generate_incidents(100)
            kb_articles = self.generator.generate_kb_articles()
            
            # Process incidents
            self._process_incidents(incidents)
            
            # Process KB articles
            self._process_kb_articles(kb_articles)
            
            # Generate and process telemetry
            for system in self.generator.systems:
                telemetry = self.generator.generate_telemetry(system)
                self._process_telemetry(telemetry)
                
            self.logger.info("Successfully loaded all sample data")
            
        except Exception as e:
            self.logger.error(f"Error loading sample data: {str(e)}")
            raise

    def _process_incidents(self, incidents: List[Dict[str, Any]]):
        """Process and store incident data"""
        try:
            # Prepare texts for embedding
            texts = [
                f"{inc['title']} {inc['description']}" 
                for inc in incidents
            ]
            
            # Generate embeddings
            embeddings = self.openai_service.get_embeddings(texts)
            
            # Store in vector database
            self.vector_db.add_documents(
                collection_name="incidents",
                documents=[{
                    "text": text,
                    "metadata": inc
                } for text, inc in zip(texts, incidents)],
                embeddings=embeddings
            )
            
        except Exception as e:
            self.logger.error(f"Error processing incidents: {str(e)}")
            raise

    def _process_kb_articles(self, articles: List[Dict[str, Any]]):
        """Process and store KB articles"""
        try:
            # Prepare texts for embedding
            texts = [
                f"{art['title']}\n{art['content']}" 
                for art in articles
            ]
            
            # Generate embeddings
            embeddings = self.openai_service.get_embeddings(texts)
            
            # Store in vector database
            self.vector_db.add_documents(
                collection_name="kb_articles",
                documents=[{
                    "text": text,
                    "metadata": art
                } for text, art in zip(texts, articles)],
                embeddings=embeddings
            )
            
        except Exception as e:
            self.logger.error(f"Error processing KB articles: {str(e)}")
            raise

    def _process_telemetry(self, telemetry_data: List[Dict[str, Any]]):
        """Process and store telemetry data"""
        try:
            # Prepare texts for embedding
            texts = [
                f"System: {data['system']}, Metrics: {str(data['metrics'])}" 
                for data in telemetry_data
            ]
            
            # Generate embeddings
            embeddings = self.openai_service.get_embeddings(texts)
            
            # Store in vector database
            self.vector_db.add_documents(
                collection_name="telemetry",
                documents=[{
                    "text": text,
                    "metadata": data
                } for text, data in zip(texts, telemetry_data)],
                embeddings=embeddings
            )
            
        except Exception as e:
            self.logger.error(f"Error processing telemetry: {str(e)}")
            raise
```

[Continued in Part 5...] 