"""All connectors in declarative container."""

from dependency_injector import containers, providers

from app.pkg.settings import settings

from .redis import Redis

__all__ = ["Connectors"]


class Connectors(containers.DeclarativeContainer):
    """Declarative container with connectors."""

    configuration = providers.Configuration(
        name="settings",
        pydantic_settings=[settings],
    )

    redis = providers.Factory(
        Redis,
        host=configuration.REDIS_HOST,
        port=configuration.REDIS_PORT,
        password=configuration.REDIS_PASSWORD,
    )
