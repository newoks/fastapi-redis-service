"""User service."""
import logging

from redis.exceptions import RedisError

from app.internal.repository.redis import redis as redis_repository
from app.pkg import models

__all__ = ["DataService"]

from app.pkg.logger import get_logger
from app.pkg.models.exceptions.data import DataNotFound


class DataService:
    __logger: logging.Logger
    redis: redis_repository.RedisRepository

    def __init__(
        self,
        redis: redis_repository.RedisRepository,
    ):
        self.redis = redis
        self.__logger = get_logger(__name__)

    async def check_data_by_phone(
        self, cmd: models.DataFields.phone
    ) -> models.DataModel:
        try:
            address = await self.redis.get(key=cmd)
        except RedisError as re:
            raise re

        if not address:
            raise DataNotFound

        return models.DataModel(
            phone=cmd,
            address=address.decode(),
        )

    async def write_data(self, cmd: models.CreateDataCommand) -> None:
        try:
            await self.redis.set(key=cmd.phone, value=cmd.address)
        except RedisError as re:
            raise re
