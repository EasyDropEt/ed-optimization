from ed_domain.queues.ed_optimization.order_model import OrderModel
from ed_infrastructure.queues.rabbitmq.subscriber import RabbitMQSubscriber

from ed_optimization.common.generic_helpers import get_config
from ed_optimization.common.logging_helpers import get_logger
from ed_optimization.webapi.api import API

LOG = get_logger()


class Package:
    def __init__(self) -> None:
        config = get_config()
        self._subscriber = RabbitMQSubscriber[OrderModel](
            config["rabbitmq_url"],
            config["rabbitmq_queue"],
        )

        self._app = API()

    def start(self) -> None:
        self._app.start()

    def stop(self) -> None:
        self._app.stop()


if __name__ == "__main__":
    main = Package()
    main.start()
