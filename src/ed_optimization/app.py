from ed_domain.queues.order.order_model import OrderModel

from ed_optimization.application.features.order.handlers.commands.process_order_command_handler import \
    ProcessOrderCommandHandler
from ed_optimization.common.generic_helpers import get_config
from ed_optimization.common.logging_helpers import get_logger
from ed_optimization.infrastructure.persistence.db_client import DbClient
from ed_optimization.infrastructure.persistence.unit_of_work import UnitOfWork
from ed_optimization.infrastructure.rabbitmq.subscriber import \
    RabbitMQSubscriber

LOG = get_logger()


class App:
    def __init__(self) -> None:
        config = get_config()
        db_client = DbClient(
            config["mongo_db_connection_string"], config["db_name"])
        uow = UnitOfWork(db_client)

        self._subscriber = RabbitMQSubscriber[OrderModel](
            config["rabbitmq_url"],
            config["rabbitmq_queue"],
        )
        self._main_handler = ProcessOrderCommandHandler(uow, self._subscriber)

    def start(self) -> None:
        self._subscriber.start()

    def stop(self) -> None:
        self._subscriber.stop()
