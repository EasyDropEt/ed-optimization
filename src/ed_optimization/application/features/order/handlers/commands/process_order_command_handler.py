from ed_domain.core.entities.delivery_job import DeliveryJobStatus
from ed_domain.core.repositories.abc_unit_of_work import ABCUnitOfWork
from ed_domain.queues.common.abc_subscriber import ABCSubscriber
from ed_domain.queues.ed_optimization.order_model import OrderModel
from rmediator.decorators import request_handler
from rmediator.types import RequestHandler

from ed_optimization.application.common.responses.base_response import \
    BaseResponse
from ed_optimization.application.features.order.handlers.commands import orders
from ed_optimization.application.features.order.requests.commands import \
    ProcessOrderCommand
from ed_optimization.common.logging_helpers import get_logger

LOG = get_logger()


@request_handler(ProcessOrderCommand, BaseResponse[None])
class ProcessOrderCommandHandler(RequestHandler):
    def __init__(self, uow: ABCUnitOfWork, subscriber: ABCSubscriber[OrderModel]):
        self._uow = uow
        subscriber.add_callback_function(self._listener_callback)

    async def handle(
        self, request: ProcessOrderCommand) -> BaseResponse[None]: ...

    def _listener_callback(self, message: OrderModel) -> None:
        LOG.info(f"order: {message}")

        # Get all available delivery jobs
        available_delivery_jobs = self._uow.delivery_job_repository.get_all(
            status=DeliveryJobStatus.AVAILABLE
        )

        # TODO: try to assign the order to a delivery job

        # If there are no available delivery jobs, add order to a redis queue

        # Once there are available delivery jobs, assign the order to a delivery job
