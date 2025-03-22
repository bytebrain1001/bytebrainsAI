# Integrated Platform Environment (IPE) - System Architecture Documentation (Part 3)
________________________________________

## 5. Authentication & Security

### 5.1 Authentication System
```python:src/utils/auth.py
from datetime import datetime, timedelta
import jwt
from config.config import Config

class AuthenticationSystem:
    def __init__(self):
        self.secret_key = Config.JWT_SECRET_KEY
        self.token_expiry = timedelta(hours=8)
        self.refresh_token_expiry = timedelta(days=7)

    def generate_tokens(self, user_data: Dict[str, Any]) -> Dict[str, str]:
        """Generate access and refresh tokens"""
        access_token = jwt.encode(
            {
                **user_data,
                'exp': datetime.utcnow() + self.token_expiry,
                'type': 'access'
            },
            self.secret_key,
            algorithm='HS256'
        )
        
        refresh_token = jwt.encode(
            {
                'user_id': user_data['id'],
                'exp': datetime.utcnow() + self.refresh_token_expiry,
                'type': 'refresh'
            },
            self.secret_key,
            algorithm='HS256'
        )
        
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def validate_token(self, token: str) -> Dict[str, Any]:
        """Validate JWT token"""
        try:
            payload = jwt.decode(
                token,
                self.secret_key,
                algorithms=['HS256']
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise AuthenticationError("Token has expired")
        except jwt.InvalidTokenError:
            raise AuthenticationError("Invalid token")
```

### 5.2 Role-Based Access Control (RBAC)
```python:src/utils/rbac.py
from enum import Enum
from typing import Set, Dict

class Permission(Enum):
    VIEW_DASHBOARD = "view_dashboard"
    RUN_AUTOMATION = "run_automation"
    MODIFY_KB = "modify_kb"
    ADMIN_ACCESS = "admin_access"

class Role(Enum):
    ADMIN = "admin"
    SUPPORT = "support"
    VIEWER = "viewer"

class RBACSystem:
    def __init__(self):
        self.role_permissions: Dict[Role, Set[Permission]] = {
            Role.ADMIN: {
                Permission.VIEW_DASHBOARD,
                Permission.RUN_AUTOMATION,
                Permission.MODIFY_KB,
                Permission.ADMIN_ACCESS
            },
            Role.SUPPORT: {
                Permission.VIEW_DASHBOARD,
                Permission.RUN_AUTOMATION
            },
            Role.VIEWER: {
                Permission.VIEW_DASHBOARD
            }
        }

    def check_permission(self, 
                        user_role: Role, 
                        required_permission: Permission) -> bool:
        """Check if role has required permission"""
        return required_permission in self.role_permissions[user_role]
```

## 6. Configuration Management

### 6.1 Configuration System
```python:src/config/config.py
import os
from dotenv import load_dotenv
from typing import Dict, Any

class Config:
    # Load environment variables
    load_dotenv()

    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    
    # Security Configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    PASSWORD_SALT = os.getenv('PASSWORD_SALT')
    
    # Database Configuration
    VECTOR_DB_PATH = os.getenv('VECTOR_DB_PATH', './data/vector_store')
    
    # Application Configuration
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    # API Configuration
    API_TIMEOUT = int(os.getenv('API_TIMEOUT', '30'))
    MAX_RETRIES = int(os.getenv('MAX_RETRIES', '3'))

    @classmethod
    def get_openai_config(cls) -> Dict[str, Any]:
        """Get OpenAI configuration"""
        return {
            'api_key': cls.OPENAI_API_KEY,
            'model': cls.OPENAI_MODEL,
            'timeout': cls.API_TIMEOUT,
            'max_retries': cls.MAX_RETRIES
        }

    @classmethod
    def validate(cls) -> None:
        """Validate required configuration"""
        required_vars = [
            'OPENAI_API_KEY',
            'JWT_SECRET_KEY'
        ]
        
        missing = [var for var in required_vars if not getattr(cls, var)]
        if missing:
            raise ValueError(f"Missing required configuration: {', '.join(missing)}")
```

### 6.2 Logging System
```python:src/utils/logger.py
import logging
from datetime import datetime
from config.config import Config

class Logger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(Config.LOG_LEVEL)
        
        # File handler
        fh = logging.FileHandler(f'logs/{name}_{datetime.now().date()}.log')
        fh.setLevel(logging.DEBUG)
        
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def info(self, message: str):
        self.logger.info(message)

    def error(self, message: str, exc_info=True):
        self.logger.error(message, exc_info=exc_info)

    def debug(self, message: str):
        self.logger.debug(message)
```

## 7. Data Management

### 7.1 Vector Database Management
```python:src/utils/vector_db_manager.py
import chromadb
from typing import List, Dict, Any
from config.config import Config
from utils.logger import Logger

class VectorDBManager:
    def __init__(self):
        self.logger = Logger(__name__)
        self.client = chromadb.PersistentClient(
            path=Config.VECTOR_DB_PATH
        )
        self.collections = {}
        self._initialize_collections()

    def _initialize_collections(self):
        """Initialize ChromaDB collections"""
        collection_configs = {
            "incidents": {
                "metadata": {"type": "incident_data"}
            },
            "kb_articles": {
                "metadata": {"type": "knowledge_base"}
            },
            "telemetry": {
                "metadata": {"type": "system_metrics"}
            }
        }
        
        for name, config in collection_configs.items():
            try:
                self.collections[name] = self.client.get_or_create_collection(
                    name=name,
                    metadata=config["metadata"]
                )
                self.logger.info(f"Initialized collection: {name}")
            except Exception as e:
                self.logger.error(f"Error initializing collection {name}: {str(e)}")

    def add_documents(self, 
                     collection_name: str, 
                     documents: List[Dict[str, Any]],
                     embeddings: List[List[float]]):
        """Add documents to vector store"""
        try:
            collection = self.collections[collection_name]
            
            # Prepare document data
            ids = [str(i) for i in range(len(documents))]
            texts = [doc.get("text", "") for doc in documents]
            metadatas = [doc.get("metadata", {}) for doc in documents]
            
            # Add to collection
            collection.add(
                ids=ids,
                embeddings=embeddings,
                documents=texts,
                metadatas=metadatas
            )
            
            self.logger.info(
                f"Added {len(documents)} documents to {collection_name}"
            )
            
        except Exception as e:
            self.logger.error(
                f"Error adding documents to {collection_name}: {str(e)}"
            )
            raise

    def search(self, 
              collection_name: str,
              query_embedding: List[float],
              n_results: int = 5,
              filter_dict: Dict = None) -> Dict[str, Any]:
        """Search vector store"""
        try:
            collection = self.collections[collection_name]
            
            results = collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results,
                where=filter_dict
            )
            
            return results
            
        except Exception as e:
            self.logger.error(
                f"Error searching {collection_name}: {str(e)}"
            )
            raise
```

[Continued in Part 4...] 