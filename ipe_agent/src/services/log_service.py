import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import json
from typing import List, Dict, Optional
import os
from datasets import load_dataset
import logging

class LogService:
    def __init__(self):
        self.log_data = {}
        self.sample_data_path = "data/sample_logs"
        self._setup_logging()
        
    def _setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
    def load_sample_data(self, source: str = "huggingface") -> Dict:
        """Load sample log data from various sources"""
        try:
            if source == "huggingface":
                return self._load_from_huggingface()
            elif source == "kaggle":
                return self._load_from_kaggle()
            else:
                return self._generate_sample_data()
        except Exception as e:
            self.logger.error(f"Error loading sample data: {str(e)}")
            return self._generate_sample_data()
            
    def _load_from_huggingface(self) -> Dict:
        """Load sample log data from Hugging Face datasets"""
        try:
            # Try to load from Hugging Face
            dataset = load_dataset("logpai/loghub")
            # Convert to our format
            return self._convert_dataset_to_logs(dataset)
        except Exception as e:
            self.logger.warning(f"Failed to load from Hugging Face: {str(e)}")
            return self._generate_sample_data()
            
    def _load_from_kaggle(self) -> Dict:
        """Load sample log data from Kaggle datasets"""
        try:
            # Implementation for Kaggle dataset loading
            # This would require Kaggle API setup
            return self._generate_sample_data()
        except Exception as e:
            self.logger.warning(f"Failed to load from Kaggle: {str(e)}")
            return self._generate_sample_data()
            
    def _generate_sample_data(self) -> Dict:
        """Generate synthetic log data"""
        applications = ["web_server", "database", "auth_service", "api_gateway"]
        servers = ["server-01", "server-02", "server-03", "server-04"]
        log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
        log_messages = [
            "User authentication successful",
            "Database connection established",
            "API request processed",
            "Cache miss occurred",
            "Memory usage high",
            "CPU utilization exceeded threshold",
            "Network latency increased",
            "Service health check failed"
        ]
        
        logs = {}
        for app in applications:
            logs[app] = {}
            for server in servers:
                logs[app][server] = []
                # Generate 100 log entries per server
                for _ in range(100):
                    timestamp = datetime.now() - timedelta(
                        hours=random.randint(0, 24),
                        minutes=random.randint(0, 60)
                    )
                    log_entry = {
                        "timestamp": timestamp,
                        "level": random.choice(log_levels),
                        "message": random.choice(log_messages),
                        "server": server,
                        "application": app,
                        "trace_id": f"trace-{random.randint(1000, 9999)}",
                        "user_id": f"user-{random.randint(1, 100)}",
                        "duration_ms": random.randint(10, 1000),
                        "status_code": random.choice([200, 201, 400, 401, 403, 500])
                    }
                    logs[app][server].append(log_entry)
                    
        return logs
        
    def _convert_dataset_to_logs(self, dataset) -> Dict:
        """Convert dataset to our log format"""
        logs = {}
        # Implementation for dataset conversion
        return logs
        
    def get_logs(self, 
                 application: str,
                 server: str,
                 start_time: Optional[datetime] = None,
                 end_time: Optional[datetime] = None,
                 log_level: Optional[str] = None) -> List[Dict]:
        """Get logs for specific application and server with filters"""
        if application not in self.log_data:
            self.log_data = self.load_sample_data()
            
        if application not in self.log_data or server not in self.log_data[application]:
            return []
            
        logs = self.log_data[application][server]
        
        # Apply filters
        if start_time:
            logs = [log for log in logs if log["timestamp"] >= start_time]
        if end_time:
            logs = [log for log in logs if log["timestamp"] <= end_time]
        if log_level:
            logs = [log for log in logs if log["level"] == log_level]
            
        return sorted(logs, key=lambda x: x["timestamp"])
        
    def get_log_summary(self, 
                       application: str,
                       server: str,
                       time_window: str = "1h") -> Dict:
        """Get summary statistics for logs"""
        logs = self.get_logs(application, server)
        
        # Calculate time window
        end_time = datetime.now()
        if time_window == "1h":
            start_time = end_time - timedelta(hours=1)
        elif time_window == "24h":
            start_time = end_time - timedelta(days=1)
        else:
            start_time = end_time - timedelta(hours=1)
            
        filtered_logs = [log for log in logs if start_time <= log["timestamp"] <= end_time]
        
        return {
            "total_logs": len(filtered_logs),
            "error_count": len([log for log in filtered_logs if log["level"] == "ERROR"]),
            "warning_count": len([log for log in filtered_logs if log["level"] == "WARNING"]),
            "avg_response_time": np.mean([log["duration_ms"] for log in filtered_logs]),
            "status_codes": self._count_status_codes(filtered_logs),
            "log_levels": self._count_log_levels(filtered_logs)
        }
        
    def _count_status_codes(self, logs: List[Dict]) -> Dict:
        """Count occurrences of status codes"""
        counts = {}
        for log in logs:
            status = log["status_code"]
            counts[status] = counts.get(status, 0) + 1
        return counts
        
    def _count_log_levels(self, logs: List[Dict]) -> Dict:
        """Count occurrences of log levels"""
        counts = {}
        for log in logs:
            level = log["level"]
            counts[level] = counts.get(level, 0) + 1
        return counts 