from typing import Annotated, TypedDict

from ed_domain.core.repositories.abc_unit_of_work import ABCUnitOfWork
from ed_domain.queues.common.abc_producer import ABCProducer
from ed_domain.queues.common.abc_subscriber import ABCSubscriber
from ed_infrastructure.persistence.mongo_db.db_client import DbClient
from ed_infrastructure.persistence.mongo_db.unit_of_work import UnitOfWork
from ed_infrastructure.queues.rabbitmq import (RabbitMQProducer,
                                               RabbitMQSubscriber)
from fastapi import Depends
from rmediator.mediator import Mediator

from ed_optimization.application.features.order.handlers.commands import \
    ProcessOrderCommandHandler
from ed_optimization.application.features.order.requests.commands import \
    ProcessOrderCommand
from ed_optimization.common.generic_helpers import get_config
from ed_optimization.common.typing.config import Config, TestMessage


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

    return producer


def get_subscriber(config: Annotated[Config, Depends(get_config)]) -> ABCSubscriber:
    subscriber = RabbitMQSubscriber[TestMessage](
        config["rabbitmq_url"],
        config["rabbitmq_queue"],
    )

    return subscriber


class ReturnType(TypedDict):
    producer: ABCProducer
    subscriber: ABCSubscriber


def get_mediator(
    uow: Annotated[ABCUnitOfWork, Depends(get_uow)],
    producer: Annotated[ABCProducer, Depends(get_producer)],
    subscriber: Annotated[ABCSubscriber, Depends(get_subscriber)],
) -> ReturnType:
    mediator = Mediator()

    handlers = [
        (ProcessOrderCommand, ProcessOrderCommandHandler(uow, subscriber))]
    for command, handler in handlers:
        mediator.register_handler(command, handler)

    return {
        "producer": producer,
        "subscriber": subscriber,
    }


def get_manual_dependency_setup() -> ReturnType:
    config = get_config()
    db_client = get_db_client(config)
    uow = get_uow(db_client)
    producer = get_producer(config)
    subscriber = get_subscriber(config)

    mediator = get_mediator(uow, producer, subscriber)

    return mediator
