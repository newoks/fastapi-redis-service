from starlette import status

from app.pkg.models.base import BaseAPIException

__all__ = ["DataNotFound"]


class DataNotFound(BaseAPIException):
    message = "Empty result data by phone number"
    status_code = status.HTTP_404_NOT_FOUND
