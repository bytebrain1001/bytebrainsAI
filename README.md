# Integrated Platform Environment (IPE)

## Overview
The Integrated Platform Environment (IPE) is a Gen-AI enabled platform designed to enhance support operations within technology organizations. It combines chat interfaces, telemetry monitoring, knowledge base management, and automation capabilities into a unified solution.

## 🚀 Features

### Core Components
- **AI-Powered Chat Interface**: Contextual support assistance using OpenAI
- **Real-time Telemetry Dashboard**: System metrics monitoring and visualization
- **Knowledge Base Management**: Vector-based search for documentation and articles
- **Automation Engine**: Automated response and remediation capabilities
- **Role-Based Access Control**: Secure access management with multiple user roles

### Technical Features
- Vector similarity search using ChromaDB
- JWT-based authentication
- Real-time data processing
- Configurable alerting system
- Automated health checks
- Comprehensive logging system

## 📋 Prerequisites
- Python 3.9+
- Docker and Docker Compose
- OpenAI API key
- ChromaDB
- Node.js 16+ (for frontend)

## 🛠️ Installation

### Using Docker
```bash
# Clone the repository
git clone https://github.com/your-repo/ipe.git
cd ipe

# Create and configure .env file
cp .env.example .env
# Edit .env with your configurations

# Build and run with Docker Compose
docker-compose up --build
```

### Manual Installation
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Install frontend dependencies
cd frontend
npm install
npm run build
cd ..

# Start the application
python src/main.py
```

## ⚙️ Configuration

### Environment Variables
```env
# API Keys
OPENAI_API_KEY=your-api-key-here

# Security
JWT_SECRET_KEY=your-jwt-secret
JWT_EXPIRATION_HOURS=24

# Database
VECTOR_DB_PATH=./data/vector_store

# Logging
LOG_LEVEL=INFO
LOG_FILE_PATH=./logs/ipe.log

# Server
PORT=8501
HOST=0.0.0.0
```

### Sample Data Configuration
The application uses a built-in Sample Data Generator for demo purposes. Configure sample data generation in `src/config/sample_data_config.py`.

## 🏗️ Project Structure
```
ipe/
├── src/
│   ├── components/          # Core components
│   ├── services/           # Service implementations
│   ├── utils/             # Utility functions
│   ├── config/            # Configuration files
│   └── main.py            # Application entry point
├── frontend/              # Frontend React application
├── tests/                # Test files
├── data/                 # Data storage
├── logs/                # Application logs
├── docker/              # Docker configuration
└── docs/                # Documentation
```

## 🔒 Security Features
- JWT-based authentication
- Role-based access control (ADMIN, SUPPORT, VIEWER)
- Secure token refresh mechanism
- API rate limiting
- Input validation and sanitization

## 💻 Usage

### Starting the Application
```bash
# Using Docker
docker-compose up

# Manual start
python src/main.py
```

### Accessing the Interface
- Main application: http://localhost:8501
- Vector DB interface: http://localhost:8000

### Default Credentials
```
Admin User:
- Username: admin
- Password: admin123

Support User:
- Username: support
- Password: support123

Viewer:
- Username: viewer
- Password: viewer123
```

## 🔍 Key Components

### Chat Interface
- AI-powered responses using OpenAI
- Context-aware assistance
- History tracking
- Knowledge base integration

### Telemetry Dashboard
- Real-time metrics visualization
- System health monitoring
- Configurable alerts
- Historical data analysis

### Knowledge Base
- Vector-based similarity search
- Document management
- Category organization
- Tag-based filtering

### Automation Engine
- Automated incident response
- Health check automation
- Alert management
- Task scheduling

## 🧪 Testing
```bash
# Run all tests
pytest

# Run specific test category
pytest tests/test_chat.py
pytest tests/test_telemetry.py
```

## 📊 Sample Data
The application includes a Sample Data Generator that creates:
- Incident tickets
- Knowledge base articles
- System telemetry data
- System inventory

## 🔧 Troubleshooting

### Common Issues
1. **Vector DB Connection Issues**
   - Verify ChromaDB is running
   - Check connection settings

2. **OpenAI API Errors**
   - Validate API key
   - Check rate limits

3. **Authentication Issues**
   - Clear browser cache
   - Verify JWT settings

## 📝 Contributing
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Support
For support, please:
1. Check the documentation
2. Search existing issues
3. Create a new issue if needed

## 🔄 Updates and Maintenance
- Regular updates for security patches
- Quarterly feature releases
- Continuous integration with GitHub Actions

## 🗺️ Roadmap
- [ ] Advanced analytics dashboard
- [ ] Custom automation workflows
- [ ] Integration with additional AI models
- [ ] Enhanced reporting capabilities