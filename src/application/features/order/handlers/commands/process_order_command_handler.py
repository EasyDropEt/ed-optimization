from rmediator.decorators import request_handler
from rmediator.types import RequestHandler

from src.application.common.responses.base_response import BaseResponse
from src.application.contracts.infrastructure.message_queue.abc_subscriber import (
    ABCSubscriber,
)
from src.application.contracts.infrastructure.persistence.abc_unit_of_work import (
    ABCUnitOfWork,
)
from src.application.features.order.requests.commands import ProcessOrderCommand
from src.common.exception_helpers import ApplicationException, Exceptions
from src.common.logging_helpers import get_logger
from src.common.typing.config import TestMessage

LOG = get_logger()


@request_handler(ProcessOrderCommand, BaseResponse[None])
class ProcessOrderCommandHandler(RequestHandler):
    def __init__(self, uow: ABCUnitOfWork, subscriber: ABCSubscriber[TestMessage]):
        self._uow = uow
        subscriber.add_callback_function(self.listener_callback)

    async def handle(self, request: ProcessOrderCommand) -> BaseResponse[None]: ...

    def listener_callback(self, message: TestMessage) -> None:
        print(message)
