from ed_domain.common.logging import get_logger

from ed_optimization.webapi.dependency_setup import get_manual_dependency_setup

LOG = get_logger()


class App:
    def __init__(self) -> None:
        self._setup()

    def _setup(self) -> None:
        di = get_manual_dependency_setup()
        self._subscriber = di["subscriber"]
        self._producer = di["producer"]

    def start(self) -> None:
        self._subscriber.start()

    def stop(self) -> None:
        self._subscriber.stop()
