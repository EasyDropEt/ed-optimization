from src.application.features.order.handlers.commands.process_order_command_handler import (
    ProcessOrderCommandHandler,
)
from src.common.generic_helpers import get_config
from src.common.logging_helpers import get_logger
from src.common.typing.config import TestMessage
from src.infrastructure.persistence.db_client import DbClient
from src.infrastructure.persistence.unit_of_work import UnitOfWork
from src.infrastructure.rabbitmq.subscriber import RabbitMQSubscriber

LOG = get_logger()


class App:
    def __init__(self) -> None:
        config = get_config()
        db_client = DbClient(config["mongo_db_connection_string"], config["db_name"])
        uow = UnitOfWork(db_client)

        self._subscriber = RabbitMQSubscriber[TestMessage](
            config["rabbitmq_url"],
            config["rabbitmq_queue"],
        )
        self._main_handler = ProcessOrderCommandHandler(uow, self._subscriber)

    def start(self) -> None:
        self._subscriber.start()

    def stop(self) -> None:
        self._subscriber.stop()
