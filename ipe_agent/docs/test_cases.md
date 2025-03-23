# Integrated Platform Environment (IPE) - Agentic AI Test Cases
________________________________________

## 1. Task Creation Tests

### 1.1 Basic Task Creation
| Test ID | Description | Test Data | Expected Result |
|---------|-------------|-----------|-----------------|
| TASK-001 | Create task with description | Description: "Analyze system logs", Context: {} | Task created with pending status |
| TASK-002 | Create task with context | Description: "Check CPU usage", Context: {"time_range": "24h"} | Task created with context |
| TASK-003 | Create task with invalid JSON | Description: "Test", Context: "{invalid json}" | Error message displayed |
| TASK-004 | Create task with empty description | Description: "", Context: {} | Validation error shown |

### 1.2 Task Planning
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

## 2. Task Execution Tests

### 2.1 Task Execution Flow
| Test ID | Description | Test Data | Expected Result |
|---------|-------------|-----------|-----------------|
| EXEC-001 | Execute pending task | Task ID: "task_1" | Task status updates to running |
| EXEC-002 | Execute completed task | Task ID: "task_2" | Error message displayed |
| EXEC-003 | Execute non-existent task | Task ID: "invalid_id" | Error message displayed |
| EXEC-004 | Step execution | Step ID: "step_1" | Step status updates to completed |

### 2.2 Sample Execution Data
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

## 3. Task History Tests

### 3.1 History Management
| Test ID | Description | Test Data | Expected Result |
|---------|-------------|-----------|-----------------|
| HIST-001 | Archive completed task | Task ID: "task_1" | Task moves to history |
| HIST-002 | View task history | None | List of completed tasks |
| HIST-003 | Filter history by date | Date range: "Last 7 days" | Filtered history list |
| HIST-004 | Search history | Query: "CPU analysis" | Matching tasks |

### 3.2 Sample History Data
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

## 4. Log Analysis Tests

### 4.1 Log Processing
| Test ID | Description | Test Data | Expected Result |
|---------|-------------|-----------|-----------------|
| LOG-001 | Analyze error logs | Log type: "error" | Error patterns identified |
| LOG-002 | Analyze performance logs | Log type: "performance" | Performance metrics extracted |
| LOG-003 | Invalid log format | Log: "invalid format" | Error handled |
| LOG-004 | Empty log file | Log: "" | Warning message |

### 4.2 Sample Log Data
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

## 5. Data Persistence Tests

### 5.1 File Operations
| Test ID | Description | Test Data | Expected Result |
|---------|-------------|-----------|-----------------|
| DATA-001 | Save active tasks | Tasks: [task_1, task_2] | Tasks saved to file |
| DATA-002 | Load active tasks | File: "active_tasks.json" | Tasks loaded correctly |
| DATA-003 | Save task history | History: [task_1, task_2] | History saved to file |
| DATA-004 | Load task history | File: "task_history.json" | History loaded correctly |

### 5.2 Sample File Data
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
```

3. Generate Test Report:
```bash
python -m pytest tests/ --html=report.html
```

## Sample Test Script

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