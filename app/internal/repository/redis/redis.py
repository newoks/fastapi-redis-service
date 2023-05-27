import datetime
from typing import Any, Optional, Union

from app.internal.repository.redis.connection import get_connection
from app.internal.repository.repository import Repository

__all__ = ["RedisRepository"]


class RedisRepository(Repository):
    default_expire_at: datetime.timedelta = datetime.timedelta(hours=24)

    async def get(self, key: Union[str, int]) -> Any:
        async with get_connection() as connect:
            return await connect.get(key)

    async def set(
        self,
        key: Union[str, int],
        value: Any,
        expire_at: Optional[datetime.timedelta] = None,
    ):
        if not expire_at:
            expire_at = self.default_expire_at

        async with get_connection() as connect:
            await connect.set(
                key,
                value,
            )
            await connect.expire(
                key,
                int(expire_at.total_seconds()),
            )

    async def delete(self, key: Union[str, int]):
        async with get_connection() as connect:
            await connect.delete(
                key,
            )

    async def pop(self, key: Union[str, int]):
        async with get_connection() as connect:
            if result := await connect.get(key):
                await connect.delete(key)
            return result
