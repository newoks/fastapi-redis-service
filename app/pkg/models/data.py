from pydantic.fields import Field

from app.pkg.models.base import BaseModel

__all__ = [
    "DataModel",
    "DataFields",
    "CreateDataCommand",
]


class DataFields:
    phone = Field(
        description="phone number",
        example="89090000000",
    )
    address = Field(description="Text address", example="Moscow, Lenin st.")


class BaseData(BaseModel):
    """Base model for data."""


class DataModel(BaseData):
    phone: str = DataFields.phone
    address: str = DataFields.address


# Commands.
class CreateDataCommand(BaseData):
    phone: str = DataFields.phone
    address: str = DataFields.address
