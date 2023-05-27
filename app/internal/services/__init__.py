from dependency_injector import containers, providers

from app.internal.repository import Repositories, redis
from app.internal.services.data import DataService
from app.pkg.settings import settings


class Services(containers.DeclarativeContainer):
    """Containers with services."""

    configuration = providers.Configuration(
        name="settings",
        pydantic_settings=[settings],
    )

    redis_repositories: redis.RedisRepositories = providers.Container(
        Repositories.redis,
    )

    data_service = providers.Factory(
        DataService,
        redis=redis_repositories.redis_repository,
    )
