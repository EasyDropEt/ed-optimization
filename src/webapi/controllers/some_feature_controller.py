from fastapi import APIRouter, Depends
from rmediator.decorators.request_handler import Annotated
from rmediator.mediator import Mediator

from src.application.common.responses.base_response import BaseResponse
from src.common.logging_helpers import get_logger
from src.webapi.common.helpers import GenericResponse, rest_endpoint
from src.webapi.dependency_setup import mediator

LOG = get_logger()
router = APIRouter(prefix="/some-feature", tags=["Some Feature"])


@router.get("", response_model=GenericResponse[None])
@rest_endpoint
async def default(
    mediator: Annotated[Mediator, Depends(mediator)]
) -> BaseResponse[None]: ...
