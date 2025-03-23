# Integrated Platform Environment (IPE) - Test Cases
________________________________________

## 1. Authentication Tests

### 1.1 Login Functionality
| Test ID | Description | Test Data | Expected Result |
|---------|-------------|-----------|-----------------|
| AUTH-001 | Valid login | username: "admin", password: "admin123" | Login successful, redirected to dashboard |
| AUTH-002 | Invalid password | username: "admin", password: "wrong" | Error message displayed |
| AUTH-003 | Empty credentials | username: "", password: "" | Validation error shown |
| AUTH-004 | Session timeout | Wait for 8 hours | User logged out automatically |

### 1.2 Role-Based Access
| Test ID | Description | Test Data | Expected Result |
|---------|-------------|-----------|-----------------|
| RBAC-001 | Admin access | Role: "admin" | Access to all features |
| RBAC-002 | Support access | Role: "support" | Limited admin features |
| RBAC-003 | Viewer access | Role: "viewer" | Read-only access |

## 2. Chat Interface Tests

### 2.1 Basic Chat Functionality
| Test ID | Description | Test Data | Expected Result |
|---------|-------------|-----------|-----------------|
| CHAT-001 | Simple query | Query: "How to check CPU usage?" | Relevant response with steps |
| CHAT-002 | Complex query | Query: "Troubleshoot high memory usage in PostgreSQL" | Detailed response with context |
| CHAT-003 | Empty query | Query: "" | Validation message |

### 2.2 Context-Aware Responses
```python
# Sample incident context
test_incident = {
    "id": "INC001",
    "title": "High CPU Usage",
    "description": "Server experiencing sustained CPU usage above 90%",
    "status": "active",
    "priority": "high"
}

# Sample test queries
test_queries = [
    "What's causing the high CPU?",
    "Show related incidents",
    "Suggest resolution steps"
]
```

## 3. Telemetry Dashboard Tests

### 3.1 Metrics Display
| Test ID | Description | Test Data | Expected Result |
|---------|-------------|-----------|-----------------|
| TEL-001 | CPU metrics | System: "web-server-01" | CPU graph displayed |
| TEL-002 | Memory metrics | System: "app-server-02" | Memory graph displayed |
| TEL-003 | Time range selection | Range: "Last 24 Hours" | Updated graphs |

### 3.2 Sample Metrics Data
```python
test_metrics = {
    "cpu_usage": [
        {"timestamp": "2024-03-17T10:00:00", "value": 85.5},
        {"timestamp": "2024-03-17T10:05:00", "value": 90.2},
        {"timestamp": "2024-03-17T10:10:00", "value": 87.8}
    ],
    "memory_usage": [
        {"timestamp": "2024-03-17T10:00:00", "value": 75.5},
        {"timestamp": "2024-03-17T10:05:00", "value": 78.2},
        {"timestamp": "2024-03-17T10:10:00", "value": 77.8}
    ]
}
```

## 4. Task Creation Tests

### 4.1 Basic Task Creation
| Test ID | Description | Test Data | Expected Result |
|---------|-------------|-----------|-----------------|
| TASK-001 | Create task with description | Description: "Analyze system logs", Context: {} | Task created with pending status |
| TASK-002 | Create task with context | Description: "Check CPU usage", Context: {"time_range": "24h"} | Task created with context |
| TASK-003 | Create task with invalid JSON | Description: "Test", Context: "{invalid json}" | Error message displayed |
| TASK-004 | Create task with empty description | Description: "", Context: {} | Validation error shown |

### 4.2 Task Planning
```python
# Sample task planning test data
test_tasks = [
    {
        "description": "Analyze system logs for the last 24 hours",
        "context": {
            "time_range": "24h",
            "severity": ["ERROR", "CRITICAL"],
            "include_performance": true
        },
        "expected_steps": [
            {
                "id": "step_1",
                "description": "Access system log files",
                "type": "action",
                "parameters": {
                    "location": "system log directory",
                    "access_rights": "administrator privileges"
                }
            },
            {
                "id": "step_2",
                "description": "Filter logs for last 24 hours",
                "type": "analysis",
                "parameters": {
                    "time_range": "24 hours"
                }
            }
        ]
    }
]
```

## 5. Task Execution Tests

### 5.1 Task Execution Flow
| Test ID | Description | Test Data | Expected Result |
|---------|-------------|-----------|-----------------|
| EXEC-001 | Execute pending task | Task ID: "task_1" | Task status updates to running |
| EXEC-002 | Execute completed task | Task ID: "task_2" | Error message displayed |
| EXEC-003 | Execute non-existent task | Task ID: "invalid_id" | Error message displayed |
| EXEC-004 | Step execution | Step ID: "step_1" | Step status updates to completed |

### 5.2 Sample Execution Data
```python
test_execution = {
    "task_id": "task_1",
    "status": "running",
    "steps": [
        {
            "id": "step_1",
            "status": "completed",
            "result": "Successfully accessed log files",
            "completed_at": "2024-03-23T19:30:00"
        },
        {
            "id": "step_2",
            "status": "running",
            "result": None,
            "started_at": "2024-03-23T19:30:05"
        }
    ]
}
```

## 6. Task History Tests

### 6.1 History Management
| Test ID | Description | Test Data | Expected Result |
|---------|-------------|-----------|-----------------|
| HIST-001 | Archive completed task | Task ID: "task_1" | Task moves to history |
| HIST-002 | View task history | None | List of completed tasks |
| HIST-003 | Filter history by date | Date range: "Last 7 days" | Filtered history list |
| HIST-004 | Search history | Query: "CPU analysis" | Matching tasks |

### 6.2 Sample History Data
```python
test_history = {
    "completed_tasks": [
        {
            "task_id": "task_1",
            "description": "CPU Usage Analysis",
            "status": "completed",
            "created_at": "2024-03-23T19:00:00",
            "completed_at": "2024-03-23T19:15:00",
            "steps": [
                {
                    "id": "step_1",
                    "status": "completed",
                    "result": "CPU usage within normal range"
                }
            ]
        }
    ]
}
```

## 7. Log Analysis Tests

### 7.1 Log Processing
| Test ID | Description | Test Data | Expected Result |
|---------|-------------|-----------|-----------------|
| LOG-001 | Analyze error logs | Log type: "error" | Error patterns identified |
| LOG-002 | Analyze performance logs | Log type: "performance" | Performance metrics extracted |
| LOG-003 | Invalid log format | Log: "invalid format" | Error handled |
| LOG-004 | Empty log file | Log: "" | Warning message |

### 7.2 Sample Log Data
```python
test_logs = {
    "error_logs": [
        {
            "timestamp": "2024-03-23T19:00:00",
            "level": "ERROR",
            "message": "CPU usage exceeded threshold",
            "source": "system_monitor"
        }
    ],
    "performance_logs": [
        {
            "timestamp": "2024-03-23T19:00:00",
            "metric": "cpu_usage",
            "value": 95.5,
            "threshold": 90.0
        }
    ]
}
```

## 8. Knowledge Base Tests

### 8.1 Search Functionality
| Test ID | Description | Test Data | Expected Result |
|---------|-------------|-----------|-----------------|
| KB-001 | Keyword search | Query: "CPU usage" | Relevant articles |
| KB-002 | Category filter | Category: "Troubleshooting" | Filtered results |
| KB-003 | No results | Query: "xyz123" | "No results" message |

### 8.2 Sample KB Articles
```python
test_kb_articles = [
    {
        "id": "KB001",
        "title": "CPU Usage Troubleshooting Guide",
        "content": """
        # CPU Usage Troubleshooting
        
        ## Common Causes
        1. Resource-intensive processes
        2. Application memory leaks
        3. Background services
        
        ## Resolution Steps
        1. Check top processes
        2. Review application logs
        3. Monitor system resources
        """,
        "category": "Troubleshooting",
        "tags": ["cpu", "performance", "troubleshooting"]
    }
]
```

## 9. Data Persistence Tests

### 9.1 File Operations
| Test ID | Description | Test Data | Expected Result |
|---------|-------------|-----------|-----------------|
| DATA-001 | Save active tasks | Tasks: [task_1, task_2] | Tasks saved to file |
| DATA-002 | Load active tasks | File: "active_tasks.json" | Tasks loaded correctly |
| DATA-003 | Save task history | History: [task_1, task_2] | History saved to file |
| DATA-004 | Load task history | File: "task_history.json" | History loaded correctly |

### 9.2 Sample File Data
```python
test_files = {
    "active_tasks.json": [
        {
            "task_id": "task_1",
            "status": "pending",
            "created_at": "2024-03-23T19:00:00"
        }
    ],
    "task_history.json": [
        {
            "task_id": "task_2",
            "status": "completed",
            "completed_at": "2024-03-23T18:00:00"
        }
    ]
}
```

## 10. Integration Tests

### 10.1 Workflow Tests
| Test ID | Description | Steps | Expected Result |
|---------|-------------|-------|-----------------|
| WF-001 | Incident Resolution | 1. View incident<br>2. Check telemetry<br>3. Run health check<br>4. Execute playbook | Incident resolved |
| WF-002 | Proactive Monitoring | 1. View dashboards<br>2. Identify issues<br>3. Run automation | Issues prevented |

### 10.2 Sample Workflow Data
```python
test_workflow = {
    "incident": {
        "id": "INC002",
        "title": "Database Performance Issue",
        "status": "active"
    },
    "telemetry": {
        "cpu": "45%",
        "memory": "89%",
        "disk": "92%"
    },
    "actions": [
        "Run health check",
        "Execute disk cleanup",
        "Restart service"
    ]
}
```

## 11. Performance Tests

### 11.1 Load Testing
| Test ID | Description | Test Data | Expected Result |
|---------|-------------|-----------|-----------------|
| PERF-001 | Multiple users | 50 concurrent users | Response < 2s |
| PERF-002 | Data loading | 1000 incidents | Load time < 3s |
| PERF-003 | Chat responses | 10 simultaneous chats | Response < 1s |

## 12. Error Handling Tests

### 12.1 Error Scenarios
| Test ID | Description | Test Data | Expected Result |
|---------|-------------|-----------|-----------------|
| ERR-001 | API timeout | Delay: 30s | Timeout message |
| ERR-002 | Invalid data | Malformed JSON | Error handled |
| ERR-003 | Network error | Disconnect network | Retry option |

## Test Execution Instructions

1. Setup Test Environment:
```bash
# Install requirements
pip install -r requirements.txt

# Set up test configuration
cp .env.example .env.test
```

2. Run Tests:
```bash
# Run all tests
python -m pytest tests/

# Run specific test category
python -m pytest tests/test_task_creation.py
python -m pytest tests/test_task_execution.py
python -m pytest tests/test_task_history.py
python -m pytest tests/test_log_analysis.py
python -m pytest tests/test_data_persistence.py
python -m pytest tests/test_chat.py
python -m pytest tests/test_telemetry.py
```

3. Generate Test Report:
```bash
python -m pytest tests/ --html=report.html
```

## Sample Test Scripts

### Task Creation Test
```python:tests/test_task_creation.py
import pytest
from services.agent_service import AgentService

def test_create_task():
    service = AgentService()
    task = service.create_task(
        "Analyze system logs",
        {"time_range": "24h"}
    )
    assert task is not None
    assert task["status"] == "pending"
    assert len(task["steps"]) > 0

def test_task_execution():
    service = AgentService()
    task = service.create_task(
        "Check CPU usage",
        {"threshold": 90}
    )
    result = service.execute_task(task["task_id"])
    assert result["status"] == "completed"
    assert all(step["status"] == "completed" for step in result["steps"])

def test_task_archiving():
    service = AgentService()
    task = service.create_task(
        "Test task",
        {}
    )
    service.archive_task(task["task_id"])
    history = service.get_task_history()
    assert any(t["task_id"] == task["task_id"] for t in history)
```

### Chat Interface Test
```python:tests/test_chat_interface.py
import pytest
from utils.openai_service import OpenAIService
from components.chat_interface import ChatInterface

def test_chat_response():
    chat = ChatInterface()
    response = chat.get_response("How to check CPU usage?")
    assert response is not None
    assert len(response) > 0

def test_context_awareness():
    chat = ChatInterface()
    incident = test_incident  # From sample data
    chat.set_context(incident)
    response = chat.get_response("What's the current status?")
    assert incident["status"] in response.lower()

def test_error_handling():
    chat = ChatInterface()
    with pytest.raises(Exception):
        chat.get_response("")  # Empty query should raise error
```

## Test Data Management

### Test Data Cleanup
```python
def cleanup_test_data():
    """Clean up test data files"""
    import os
    import json
    
    # Clean up active tasks
    if os.path.exists("active_tasks.json"):
        with open("active_tasks.json", "w") as f:
            json.dump([], f)
    
    # Clean up task history
    if os.path.exists("task_history.json"):
        with open("task_history.json", "w") as f:
            json.dump([], f)
```