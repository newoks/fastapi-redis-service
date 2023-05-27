from contextlib import asynccontextmanager

from dependency_injector.wiring import Provide, inject
from redis.connection import Connection

from app.pkg.connectors import Connectors
from app.pkg.connectors.redis import Redis

__all__ = ["get_connection"]


@asynccontextmanager
@inject
async def get_connection(
    redis: Redis = Provide[Connectors.redis],
) -> Connection:
    """Get async connection to postgresql of pool."""
    async with redis.get_connect() as connection:
        yield connection
