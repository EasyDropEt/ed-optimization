from ed_optimization.common.logging_helpers import get_logger
from ed_optimization.webapi.api import API

LOG = get_logger()


class Package:
    def __init__(self) -> None:
        self._app = API()

    def start(self) -> None:
        self._app.start()

    def stop(self) -> None:
        self._app.stop()


if __name__ == "__main__":
    main = Package()
    main.start()
