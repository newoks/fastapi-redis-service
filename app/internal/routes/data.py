from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.internal.services import Services
from app.internal.services.data import DataService
from app.pkg import models

__all__ = ["router"]

router = APIRouter(tags=["Data"])


@router.get(
    "/check_data",
    response_model=models.DataModel,
    status_code=status.HTTP_200_OK,
    description="Get data by phone",
)
@inject
async def check_data(
    phone: str,
    data_service: DataService = Depends(Provide[Services.data_service]),
):
    return await data_service.check_data_by_phone(cmd=phone)


@router.post(
    "/write_data",
    status_code=status.HTTP_201_CREATED,
    description="Write data",
)
@inject
async def write_data(
    cmd: models.CreateDataCommand,
    data_service: DataService = Depends(Provide[Services.data_service]),
):
    return await data_service.write_data(cmd=cmd)
