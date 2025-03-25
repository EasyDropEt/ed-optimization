from typing import Annotated

from fastapi import Depends
from rmediator.mediator import Mediator

from ed_optimization.application.contracts.infrastructure.message_queue.abc_producer import (
    ABCProducer,
)
from ed_optimization.application.contracts.infrastructure.message_queue.abc_subscriber import (
    ABCSubscriber,
)
from ed_optimization.application.contracts.infrastructure.persistence.abc_unit_of_work import (
    ABCUnitOfWork,
)
from ed_optimization.application.features.order.handlers.commands.process_order_command_handler import (
    ProcessOrderCommandHandler,
)
from ed_optimization.application.features.order.requests.commands.process_order_command import (
    ProcessOrderCommand,
)
from ed_optimization.common.generic_helpers import get_config
from ed_optimization.common.typing.config import Config, TestMessage
from ed_optimization.infrastructure.persistence.db_client import DbClient
from ed_optimization.infrastructure.persistence.unit_of_work import UnitOfWork
from ed_optimization.infrastructure.rabbitmq.producer import RabbitMQProducer
from ed_optimization.infrastructure.rabbitmq.subscriber import RabbitMQSubscriber


def get_db_client(config: Annotated[Config, Depends(get_config)]) -> DbClient:
    return DbClient(
        config["mongo_db_connection_string"],
        config["db_name"],
    )


def get_uow(db_client: Annotated[DbClient, Depends(get_db_client)]) -> ABCUnitOfWork:
    return UnitOfWork(db_client)


def get_producer(config: Annotated[Config, Depends(get_config)]) -> ABCProducer:
    producer = RabbitMQProducer[TestMessage](
        config["rabbitmq_url"],
        config["rabbitmq_queue"],
    )
    producer.start()

    return producer


def get_subscriber(config: Annotated[Config, Depends(get_config)]) -> ABCSubscriber:
    subscriber = RabbitMQSubscriber[TestMessage](
        config["rabbitmq_url"],
        config["rabbitmq_queue"],
    )
    subscriber.start()

    return subscriber


def mediator(
    uow: Annotated[ABCUnitOfWork, Depends(get_uow)],
    producer: Annotated[ABCProducer, Depends(get_producer)],
    subscriber: Annotated[ABCSubscriber, Depends(get_subscriber)],
) -> Mediator:
    mediator = Mediator()

    handlers = [(ProcessOrderCommand, ProcessOrderCommandHandler(uow, subscriber))]
    for command, handler in handlers:
        mediator.register_handler(command, handler)

    return mediator
