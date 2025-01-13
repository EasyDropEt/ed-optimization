from dataclasses import dataclass

from rmediator.decorators import request
from rmediator.mediator import Request

from src.application.common.responses.base_response import BaseResponse


@request(BaseResponse[None])
@dataclass
class ProcessOrderCommand(Request): ...
