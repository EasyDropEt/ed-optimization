from ed_optimization.app import App
from ed_optimization.common.logging_helpers import get_logger

LOG = get_logger()


class Package:
    def __init__(self) -> None:
        self._app = App()

    def start(self) -> None:
        self._app.start()

    def stop(self) -> None:
        self._app.stop()


if __name__ == "__main__":
    main = Package()
    main.start()
