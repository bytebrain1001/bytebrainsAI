# Integrated Platform Environment (IPE) - Agentic AI Solution

## Overview
The Integrated Platform Environment (IPE) is an AI-powered platform designed to enhance support operations through intelligent task automation and analysis. It combines OpenAI's capabilities with a robust task management system to create, execute, and track automated tasks.

## 🚀 Features

### Core Components
- **AI-Powered Task Automation**: Intelligent task planning and execution using OpenAI
- **Task Management System**: Create, execute, and track automated tasks
- **Task History**: Comprehensive tracking of completed tasks and their results
- **Log Analysis**: AI-powered analysis of system logs and performance metrics
- **Anomaly Detection**: Automated detection of system anomalies and issues

### Technical Features
- OpenAI integration for intelligent task planning and execution
- JSON-based task storage and history
- Real-time task status tracking
- Automated task archiving
- Comprehensive logging system
- Step-by-step task execution with status tracking

## 📋 Prerequisites
- Python 3.9+
- OpenAI API key
- Streamlit for the web interface

## 🛠️ Installation

### Manual Installation
```bash
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
```

## 🏗️ Project Structure
```
ipe/
├── src/
│   ├── components/          # UI components
│   ├── services/           # Service implementations
│   ├── utils/             # Utility functions
│   ├── config/            # Configuration files
│   └── main.py            # Application entry point
├── data/                  # Data storage
│   ├── active_tasks.json  # Active tasks storage
│   └── task_history.json  # Task history storage
├── logs/                  # Application logs
└── docs/                  # Documentation
```

## 💻 Usage

### Starting the Application
```bash
python src/main.py
```

### Accessing the Interface
- Main application: http://localhost:8501

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

### Data Storage
- JSON-based task storage
- Persistent task history
- Active task management
- Execution results tracking

## 🔧 Troubleshooting

### Common Issues
1. **OpenAI API Errors**
   - Validate API key
   - Check rate limits
   - Verify network connectivity

2. **Task Execution Issues**
   - Check task status
   - Review execution logs
   - Verify task parameters

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