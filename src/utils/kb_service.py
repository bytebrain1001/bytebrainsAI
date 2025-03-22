from datetime import datetime, timedelta
from typing import List, Dict, Any

class KBService:
    def __init__(self):
        # Initialize with sample knowledge base data
        self._articles = self._initialize_articles()
        self._guides = self._initialize_guides()
        self._stack_overflow = self._initialize_stack_overflow()
        self._documentation = self._initialize_documentation()

    def _initialize_articles(self) -> List[Dict[str, Any]]:
        """Initialize sample KB articles"""
        return [
            {
                "id": "KB001",
                "title": "Common System Issues and Solutions",
                "category": "Troubleshooting",
                "content": """
                # Common System Issues and Solutions
                
                ## High CPU Usage
                - Check for resource-intensive processes
                - Review application logs
                - Monitor system metrics
                
                ## Memory Leaks
                - Identify memory-consuming processes
                - Analyze heap dumps
                - Review application memory settings
                """,
                "tags": ["system", "cpu", "memory", "troubleshooting"],
                "last_updated": datetime.now() - timedelta(days=5)
            },
            {
                "id": "KB002",
                "title": "Database Performance Optimization",
                "category": "Best Practices",
                "content": """
                # Database Performance Optimization
                
                ## Index Optimization
                - Review query execution plans
                - Analyze index usage
                - Implement missing indexes
                
                ## Query Tuning
                - Identify slow queries
                - Optimize query structure
                - Use query hints when necessary
                """,
                "tags": ["database", "performance", "optimization"],
                "last_updated": datetime.now() - timedelta(days=2)
            }
        ]

    def _initialize_guides(self) -> List[Dict[str, Any]]:
        """Initialize sample troubleshooting guides"""
        return [
            {
                "id": "TG001",
                "title": "Resolving High CPU Usage",
                "system": "Linux Servers",
                "problem": "System experiencing sustained high CPU usage",
                "steps": [
                    "Check top processes using 'top' command",
                    "Review system logs in /var/log/",
                    "Monitor CPU usage patterns",
                    "Identify and optimize resource-intensive applications"
                ],
                "verification": "CPU usage should return to normal levels (<70%)",
                "tags": ["cpu", "performance", "linux"],
                "last_updated": datetime.now() - timedelta(days=1)
            }
        ]

    def _initialize_stack_overflow(self) -> List[Dict[str, Any]]:
        """Initialize sample Stack Overflow posts"""
        return [
            {
                "id": "SO001",
                "title": "How to optimize PostgreSQL query performance?",
                "question": "I have a complex query that's running slowly...",
                "accepted_answer": """
                1. First, analyze the query using EXPLAIN ANALYZE
                2. Check for missing indexes
                3. Review query structure
                """,
                "score": 125,
                "tags": ["postgresql", "performance", "sql"],
                "timestamp": datetime.now() - timedelta(days=30)
            }
        ]

    def _initialize_documentation(self) -> List[Dict[str, Any]]:
        """Initialize sample documentation"""
        return [
            {
                "id": "DOC001",
                "title": "System Architecture Overview",
                "category": "Architecture",
                "content": """
                # System Architecture
                
                ## Components
                - Web Servers
                - Application Servers
                - Database Servers
                
                ## Network Layout
                - DMZ Configuration
                - Internal Network
                - Backup Systems
                """,
                "last_updated": datetime.now() - timedelta(days=10)
            }
        ]

    def search_articles(self, query: str) -> List[Dict[str, Any]]:
        """Search KB articles"""
        if not query:
            return []
        return [
            article for article in self._articles
            if query.lower() in article['title'].lower() or
               query.lower() in article['content'].lower() or
               any(query.lower() in tag.lower() for tag in article['tags'])
        ]

    def get_recent_articles(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get recent KB articles"""
        return sorted(
            self._articles,
            key=lambda x: x['last_updated'],
            reverse=True
        )[:limit]

    def search_guides(self, query: str) -> List[Dict[str, Any]]:
        """Search troubleshooting guides"""
        if not query:
            return []
        return [
            guide for guide in self._guides
            if query.lower() in guide['title'].lower() or
               query.lower() in guide['problem'].lower()
        ]

    def get_recent_guides(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get recent troubleshooting guides"""
        return sorted(
            self._guides,
            key=lambda x: x['last_updated'],
            reverse=True
        )[:limit]

    def search_stack_overflow(self, query: str) -> List[Dict[str, Any]]:
        """Search Stack Overflow posts"""
        if not query:
            return []
        return [
            post for post in self._stack_overflow
            if query.lower() in post['title'].lower() or
               query.lower() in post['question'].lower()
        ]

    def get_top_posts(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get top-rated Stack Overflow posts"""
        return sorted(
            self._stack_overflow,
            key=lambda x: x['score'],
            reverse=True
        )[:limit]

    def search_documentation(self, query: str) -> List[Dict[str, Any]]:
        """Search documentation"""
        if not query:
            return []
        return [
            doc for doc in self._documentation
            if query.lower() in doc['title'].lower() or
               query.lower() in doc['content'].lower()
        ]

    def get_recent_docs(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get recent documentation"""
        return sorted(
            self._documentation,
            key=lambda x: x['last_updated'],
            reverse=True
        )[:limit] 