"""Module for load settings form `.env` or if server running with parameter
`dev` from `.env.dev`"""
import pathlib
from functools import lru_cache

import pydantic
from dotenv import find_dotenv
from pydantic.env_settings import BaseSettings
from pydantic.types import PositiveInt, SecretStr

__all__ = ["Settings", "get_settings"]


class _Settings(BaseSettings):
    class Config:
        """Configuration of settings."""

        #: str: env file encoding.
        env_file_encoding = "utf-8"
        #: str: allow custom fields in model.
        arbitrary_types_allowed = True


class Settings(_Settings):
    """Server settings.

    Formed from `.env` or `.env.dev`.
    """

    API_INSTANCE_APP_NAME: str
    X_API_TOKEN: SecretStr

    REDIS_HOST: str
    REDIS_PORT: PositiveInt
    REDIS_PASSWORD: SecretStr

    LOGGER_LEVEL: pydantic.StrictStr
    LOGGER_DIR_PATH: pathlib.Path
    LOGGER_DIR_PATH_INTERNAL: pathlib.Path


@lru_cache()
def get_settings(env_file: str = ".env") -> Settings:
    """Create settings instance."""
    return Settings(_env_file=find_dotenv(env_file))
