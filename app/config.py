import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load .env file if present
load_dotenv()

class Settings(BaseSettings):
    # Hindsight
    hindsight_api_key: str = os.getenv("HINDSIGHT_API_KEY", "")
    hindsight_base_url: str = os.getenv("HINDSIGHT_BASE_URL", "https://api.hindsight.vectorize.io")
    hindsight_namespace: str = os.getenv("HINDSIGHT_NAMESPACE", "customer_support")

    # Groq LLM
    groq_api_key: str = os.getenv("GROQ_API_KEY", "")
    groq_model: str = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

    # Database
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./support_agent.db")

    # Application
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    default_recall_limit: int = int(os.getenv("DEFAULT_RECALL_LIMIT", "5"))
    max_recall_limit: int = int(os.getenv("MAX_RECALL_LIMIT", "10"))

    class Config:
        env_file = ".env"
        case_sensitive = False

# Singleton settings instance
settings = Settings()