# app/config.py

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables / .env file."""

    app_name: str = "FastAPI Deployments App"
    environment: str = "local"  # e.g. local, dev, prod
    log_level: str = "INFO"  # e.g. DEBUG, INFO, WARNING, ERROR

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings() -> Settings:
    # Cached so it’s only constructed once
    return Settings()


# Convenience singleton for simple use cases
settings = get_settings()
