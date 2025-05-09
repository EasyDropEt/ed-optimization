from dataclasses import dataclass

from ed_domain.queues.ed_optimization.order_model import OrderModel
from rmediator.decorators import request
from rmediator.mediator import Request

from ed_optimization.application.common.responses.base_response import \
    BaseResponse


@request(BaseResponse[None])
@dataclass
class ProcessOrderCommand(Request):
    model: OrderModel
