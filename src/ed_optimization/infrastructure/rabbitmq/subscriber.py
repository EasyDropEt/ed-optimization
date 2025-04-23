from typing import Generic, TypeVar

import jsons
from pika import ConnectionParameters, URLParameters, spec
from pika.adapters import BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel

from ed_optimization.application.contracts.infrastructure.message_queue.abc_subscriber import (
    ABCSubscriber, CallbackFunction)
from ed_optimization.common.logging_helpers import get_logger

LOG = get_logger()
TMessageSchema = TypeVar("TMessageSchema")


class RabbitMQSubscriber(Generic[TMessageSchema], ABCSubscriber[TMessageSchema]):
    def __init__(
        self,
        url: str,
        queue: str,
    ) -> None:
        self._queue = queue
        self._connection = self._connect_with_url_parameters(url)
        self._callback_functions: list[CallbackFunction] = []

    def add_callback_function(self, callback_function: CallbackFunction) -> None:
        self._callback_functions.append(callback_function)

    def start(self) -> None:
        LOG.info("Starting subscriber...")
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self._queue, durable=True)

        self._channel.basic_consume(
            queue=self._queue, on_message_callback=self._callback, auto_ack=False
        )
        self._channel.start_consuming()

    def stop(self) -> None:
        LOG.info("Stopping subscriber")
        self._connection.close()

    def _connect_with_connection_parameters(
        self, host: str, port: int
    ) -> BlockingConnection:
        connection_parameters = ConnectionParameters(host, port)
        return BlockingConnection(connection_parameters)

    def _connect_with_url_parameters(self, url: str) -> BlockingConnection:
        connection_parameters = URLParameters(url)
        return BlockingConnection(connection_parameters)

    def _callback(
        self,
        channel: BlockingChannel,
        method: spec.Basic.Deliver,
        properties: spec.BasicProperties,
        body: bytes,
    ) -> None:
        try:
            message: TMessageSchema = jsons.loads(body.decode("utf-8"))

            for fn in self._callback_functions:
                fn(message)

        except jsons.DeserializationError as e:
            LOG.error(f"Failed to deserialize message: {e}")

        except KeyError as e:
            LOG.error(f"Missing key in message: {e}")
