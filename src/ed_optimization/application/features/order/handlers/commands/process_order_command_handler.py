from ed_domain.queues.order.order_model import OrderModel
from rmediator.decorators import request_handler
from rmediator.types import RequestHandler

from ed_optimization.application.common.responses.base_response import BaseResponse
from ed_optimization.application.contracts.infrastructure.message_queue.abc_subscriber import (
    ABCSubscriber,
)
from ed_optimization.application.contracts.infrastructure.persistence.abc_unit_of_work import (
    ABCUnitOfWork,
)
from ed_optimization.application.features.order.requests.commands import ProcessOrderCommand
from ed_optimization.common.logging_helpers import get_logger

LOG = get_logger()


@request_handler(ProcessOrderCommand, BaseResponse[None])
class ProcessOrderCommandHandler(RequestHandler):
    def __init__(self, uow: ABCUnitOfWork, subscriber: ABCSubscriber[OrderModel]):
        self._uow = uow
        subscriber.add_callback_function(self.listener_callback)

    async def handle(self, request: ProcessOrderCommand) -> BaseResponse[None]: ...

    def listener_callback(self, message: OrderModel) -> None:
        print(message)
