from dependency_injector import containers, providers

from .redis import RedisRepository


class RedisRepositories(containers.DeclarativeContainer):
    redis_repository = providers.Factory(RedisRepository)
