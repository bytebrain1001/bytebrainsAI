# Integrated Platform Environment (IPE) - Agentic AI Solution

## Overview
The Integrated Platform Environment (IPE) is a Gen-AI enabled platform designed to enhance support operations within technology organizations. It combines intelligent task automation, log analysis, and knowledge management into a unified solution powered by OpenAI's capabilities.

## 🚀 Features

### Core Components
- **AI-Powered Chat Interface**: Contextual support assistance using OpenAI
- **Real-time Telemetry Dashboard**: System metrics monitoring and visualization
- **Knowledge Base Management**: Vector-based search for documentation and articles
- **Automation Engine**: Automated response and remediation capabilities
- **Role-Based Access Control**: Secure access management with multiple user roles
- **AI-Powered Task Automation**: Intelligent task planning and execution using OpenAI
- **Task Management System**: Create, execute, and track automated tasks
- **Task History**: Comprehensive tracking of completed tasks and their results
- **Log Analysis**: AI-powered analysis of system logs and performance metrics
- **Anomaly Detection**: Automated detection of system anomalies and issues

### Technical Features
- Vector similarity search using ChromaDB
- JWT-based authentication
- Real-time data processing
- Configurable alerting system
- Automated health checks
- Comprehensive logging system
- OpenAI integration for intelligent task planning and execution
- JSON-based task storage and history
- Real-time task status tracking
- Automated task archiving
- Step-by-step task execution with status tracking
- Secure API integration

## 📋 Prerequisites
- Python 3.9+
- OpenAI API key
- Streamlit for the web interface
- Git for version control

## 🛠️ Installation

### Manual Installation
```bash
# Clone the repository
git clone https://github.com/your-repo/ipe.git
cd ipe

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Start the application
python src/main.py
```

## ⚙️ Configuration

### Environment Variables
```env
# API Keys
OPENAI_API_KEY=your-api-key-here

# Logging
LOG_LEVEL=INFO
LOG_FILE_PATH=./logs/ipe.log

# Server
PORT=8501
HOST=0.0.0.0

# Security
JWT_SECRET_KEY=your-jwt-secret
JWT_EXPIRATION_HOURS=24
```

## 🏗️ Project Structure
```
ipe/
├── src/
│   ├── components/          # UI components
│   │   ├── automation_panel.py
│   │   └── task_history_panel.py
│   ├── services/           # Service implementations
│   │   ├── agent_service.py
│   │   └── openai_service.py
│   ├── utils/             # Utility functions
│   │   ├── config.py
│   │   └── logger.py
│   ├── config/            # Configuration files
│   └── main.py            # Application entry point
├── data/                  # Data storage
│   ├── active_tasks.json  # Active tasks storage
│   └── task_history.json  # Task history storage
├── logs/                  # Application logs
└── docs/                  # Documentation
    ├── markdown.md        # System integration documentation
    ├── system_architecture.md  # Detailed system architecture
    └── test_cases.md      # Test cases and scenarios
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
python src/main.py
```

### Accessing the Interface
- Main application: http://localhost:8501

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

### Task Management
1. **Creating Tasks**
   - Go to the "Agent Tasks" tab
   - Fill in task description and context
   - Click "Create Task"

2. **Executing Tasks**
   - View active tasks
   - Click "Execute Task" for the desired task
   - Monitor task progress and results

3. **Viewing History**
   - Access completed tasks in the "Task History" tab
   - View detailed execution results and timestamps

## 🔍 Key Components

### Chat Interface
- AI-powered responses using OpenAI
- Context-aware assistance
- History tracking
- Knowledge base integration
- Real-time conversation management
- Multi-turn dialogue support

### Telemetry Dashboard
- Real-time metrics visualization
- System health monitoring
- Configurable alerts
- Historical data analysis
- Performance trend tracking
- Resource utilization monitoring

### Knowledge Base
- Vector-based similarity search
- Document management
- Category organization
- Tag-based filtering
- Content versioning
- Search history tracking

### Automation Engine
- Automated incident response
- Health check automation
- Alert management
- Task scheduling
- Workflow automation
- Event-driven actions

### Task Automation
- AI-powered task planning
- Step-by-step execution
- Status tracking and updates
- Result collection and storage

### Log Analysis
- System log analysis
- Performance metrics tracking
- Anomaly detection
- Insight generation
- Pattern recognition
- Root cause analysis

### Data Storage
- JSON-based task storage
- Persistent task history
- Active task management
- Execution results tracking
- Data versioning
- Backup and recovery

## 🧪 Testing
```bash
# Run all tests
pytest

# Run specific test category
pytest tests/test_task_creation.py
pytest tests/test_task_execution.py
pytest tests/test_task_history.py
pytest tests/test_log_analysis.py
pytest tests/test_data_persistence.py
```

## 📊 Sample Data
The application includes sample data for testing:
- Task templates and examples
- Log analysis datasets
- System performance metrics
- Task execution results
- Historical task data

## 🔧 Troubleshooting

### Common Issues
1. **Vector DB Connection Issues**
   - Verify ChromaDB is running
   - Check connection settings
   - Validate database credentials
   - Ensure proper network access
   - Check database health status

2. **OpenAI API Errors**
   - Validate API key
   - Check rate limits
   - Verify network connectivity
   - Ensure proper API permissions
   - Monitor API usage quotas

3. **Authentication Issues**
   - Clear browser cache
   - Verify JWT settings
   - Check user permissions
   - Validate token expiration
   - Ensure proper role assignments

4. **Task Execution Issues**
   - Check task status
   - Review execution logs
   - Verify task parameters
   - Monitor resource usage
   - Check task dependencies

5. **Data Storage Issues**
   - Verify file permissions
   - Check disk space
   - Validate JSON format
   - Monitor file system health
   - Ensure backup integrity

## 📝 Contributing
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## 📚 Documentation

### System Integration Documentation (`docs/markdown.md`)
- Integration points and data flow
- API configurations and endpoints
- Data schemas and formats
- Error handling strategies
- Performance considerations
- Security implementations

### System Architecture (`docs/system_architecture.md`)
- Core components and services
- Data flow architecture
- Service layer implementation
- Data loading and initialization
- Sample data generation
- Error handling
- Performance optimization
- OpenAI integration details

### Test Cases (`docs/test_cases.md`)
- Authentication tests
- Chat interface tests
- Telemetry dashboard tests
- Knowledge base tests
- Integration tests
- Performance tests
- Error handling tests
- Task management tests
- Log analysis tests
- Data persistence tests

