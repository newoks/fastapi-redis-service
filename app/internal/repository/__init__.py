from dependency_injector import containers, providers

from . import redis
from .repository import BaseRepository

__all__ = ["Repositories"]


class Repositories(containers.DeclarativeContainer):
    redis = providers.Container(redis.RedisRepositories)
