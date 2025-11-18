# app/config.py
from functools import lru_cache
from pathlib import Path
import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FastAPI Deployments App"
    environment: str = "local"  # e.g. local | dev | prod
    log_level: str = "INFO"  # e.g. DEBUG | INFO | WARNING | ERROR

    # For Phase 2
    database_url: str = "sqlite:///./data/app.db"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="", extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    """
    Load settings with support for:
    1) ENV_FILE env var (highest priority)
    2) .env
    3) .env.{environment} if it exists
    """

    # 1) If ENV_FILE is set, always use that file.
    env_file = os.getenv("ENV_FILE")
    if env_file:
        return Settings(_env_file=env_file)

    # 2) Try to load base .env if it exists.
    if Path(".env").is_file():
        base = Settings(_env_file=".env")
    else:
        base = Settings()

    # 3) If a more specific .env.{environment} exists, load from that instead.
    env_specific = Path(f".env.{base.environment}")
    if env_specific.is_file():
        return Settings(_env_file=env_specific)

    return base


settings = get_settings()
