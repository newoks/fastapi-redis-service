"""Redis connector."""

from contextlib import asynccontextmanager

import pydantic
from redis import Connection
from redis import asyncio as aioredis

from .base_connector import BaseConnector

__all__ = ["Redis"]


class Redis(BaseConnector):
    _host: str
    _port: pydantic.PositiveInt
    _password: pydantic.SecretStr

    def __init__(
        self,
        host: str,
        port: pydantic.PositiveInt,
        password: pydantic.SecretStr,
    ):
        """
        Args:
            host: the host where the redis is located.
            port: the port of redis server.
            password: redis password.
        """
        self._host = host
        self._port = port
        self._password = password

    def get_dsn(self):
        """Description of ``BaseConnector.get_dsn``."""
        return f"redis://:{self._password.get_secret_value()}@{self._host}:{self._port}"

    @asynccontextmanager
    async def get_connect(self) -> Connection:
        redis_dsn = self.get_dsn()
        async with aioredis.from_url(redis_dsn) as conn:
            yield conn
