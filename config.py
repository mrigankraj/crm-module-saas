import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Database configuration
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost:5432/crm_db')
    
    # JWT configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour
    
    # Email configuration
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
    SMTP_USERNAME = os.getenv('SMTP_USERNAME', 'your-email@gmail.com')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', 'your-app-password')
    
    # Application configuration
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    CHATBOT_API_KEY = os.getenv('CHATBOT_API_KEY', 'your-chatbot-api-key')
    
    # File upload configuration
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

config = Config()
