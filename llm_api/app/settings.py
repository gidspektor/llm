import enum
import os

from pydantic_settings import BaseSettings


class LogLevel(str, enum.Enum):
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    host: str = os.environ.get("API_HOST", "0.0.0.0")
    port: int = int(os.environ.get("API_PORT", "80"))
    # quantity of workers for uvicorn
    workers_count: int = int(os.environ.get("WORKER_COUNT", 1))
    # Enable uvicorn reloading
    reload: bool = bool(os.environ.get("DATA_API_RELOAD", False))
    # Current environment
    environment: str = os.environ.get("ENV", "dev")

    log_level: LogLevel = LogLevel.INFO

    temerature: float = os.environ.get("termperature", 0.7)
    n: int = os.environ.get("n", 1)
    llm_model: str = os.environ.get("llm_model", "gpt-4o-mini")
    llm_api_key: str = os.environ.get("llm_api_key", "")

    request_max_lenth: int = os.environ.get("REQUEST_MAX_LENGTH", 1000)

    news_api_token: str = os.environ.get("NEWS_API_TOKEN", "XTohyGdjVSiU7aBB1CLudoBTI0ZfgTh9MR7BiPho")
    news_api_base_url: str = os.environ.get("NEWS_API_BASE_URL", "https://api.thenewsapi.com/v1/news/all")
    news_language: str = os.environ.get("NEWS_LANGUAGE", "es")
    news_country: str = os.environ.get("NEWS_COUNTRY", "es")
    news_stories_limit: int = os.environ.get("NEWS_STORIES_LIMIT", 3)

settings = Settings()
