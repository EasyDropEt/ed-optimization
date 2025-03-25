from fastapi import APIRouter, Depends
from rmediator.decorators.request_handler import Annotated
from rmediator.mediator import Mediator

from ed_optimization.application.common.responses.base_response import BaseResponse
from ed_optimization.common.logging_helpers import get_logger
from ed_optimization.webapi.common.helpers import GenericResponse, rest_endpoint
from ed_optimization.webapi.dependency_setup import mediator

LOG = get_logger()
router = APIRouter(prefix="/some-feature", tags=["Some Feature"])


@router.get("", response_model=GenericResponse[None])
@rest_endpoint
async def default(
    mediator: Annotated[Mediator, Depends(mediator)]
) -> BaseResponse[None]: ...
