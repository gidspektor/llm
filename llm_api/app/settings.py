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
	port: int = int(os.environ.get("API_PORT", "8000"))
	# quantity of workers for uvicorn
	workers_count: int = int(os.environ.get("WORKER_COUNT", 1))
	# Enable uvicorn reloading
	reload: bool = bool(os.environ.get("DATA_API_RELOAD", False))
	# Current environment
	environment: str = os.environ.get("ENV", "dev")

	# Key to hit any endpoint
	app_api_key: str = os.environ.get("APP_API_KEY", "ea73b5fe-72ad-4f5a-8e44-c5768c861552")

	allowed_origins: list = os.environ.get("ALLOWED_HOSTS", ["http://localhost:3000"])
	allowed_headers: list = os.environ.get("ALLOWED_HEADERS", ["Authorization", "Content-Type", "X-Api-Key"])
	allowed_methods: list = os.environ.get("ALLOWED_METHODS", ["GET", "POST", "PUT", "DELETE", "OPTIONS"])

	log_level: LogLevel = LogLevel.INFO

	temerature: float = os.environ.get("termperature", 0.7)
	n: int = os.environ.get("n", 1)
	llm_model: str = os.environ.get("llm_model", "gpt-4o-mini")
	llm_api_key: str = os.environ.get("llm_api_key", "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")

	request_max_lenth: int = os.environ.get("REQUEST_MAX_LENGTH", 1000)

	news_api_token: str = os.environ.get("NEWS_API_TOKEN", "XTohyGdjVSiU7aBB1CLudoBTI0ZfgTh9MR7BiPho")
	news_api_base_url: str = os.environ.get("NEWS_API_BASE_URL", "https://api.thenewsapi.com/v1/news/all")
	news_language: str = os.environ.get("NEWS_LANGUAGE", "en")
	news_country: str = os.environ.get("NEWS_COUNTRY", "us")
	news_stories_limit: int = os.environ.get("NEWS_STORIES_LIMIT", 3)
	default_categories: str = os.environ.get("DEFAULT_CATEGORIES", "tech")
    
	countries_map: dict = os.environ.get("COUNTRIES_MAP", {
		"ar": "Argentina",
		"am": "Armenia",
		"au": "Australia",
		"at": "Austria",
		"by": "Belarus",
		"be": "Belgium",
		"bo": "Bolivia",
		"br": "Brazil",
		"bg": "Bulgaria",
		"ca": "Canada",
		"cl": "Chile",
		"cn": "China",
		"co": "Colombia",
		"hr": "Croatia",
		"cz": "Czechia",
		"ec": "Ecuador",
		"eg": "Egypt",
		"fr": "France",
		"de": "Germany",
		"gr": "Greece",
		"hn": "Honduras",
		"hk": "Hong Kong",
		"in": "India",
		"id": "Indonesia",
		"ir": "Iran",
		"ie": "Ireland",
		"il": "Israel",
		"it": "Italy",
		"jp": "Japan",
		"kr": "Korea",
		"mx": "Mexico",
		"nl": "Netherlands",
		"nz": "New Zealand",
		"ni": "Nicaragua",
		"pk": "Pakistan",
		"pa": "Panama",
		"pe": "Peru",
		"pl": "Poland",
		"pt": "Portugal",
		"qa": "Qatar",
		"ro": "Romania",
		"ru": "Russia",
		"sa": "Saudi Arabia",
		"za": "South Africa",
		"es": "Spain",
		"ch": "Switzerland",
		"sy": "Syria",
		"tw": "Taiwan",
		"th": "Thailand",
		"tr": "Turkey",
		"ua": "Ukraine",
		"gb": "United Kingdom",
		"us": "United States Of America",
		"uy": "Uruguay",
		"ve": "Venezuela",
	})

settings = Settings()
