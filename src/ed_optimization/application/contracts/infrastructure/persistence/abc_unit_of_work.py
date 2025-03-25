from abc import ABCMeta, abstractmethod

from ed_optimization.application.contracts.infrastructure.persistence.abc_some_repository import (
    ABCSomeEntityRepository,
)


class ABCUnitOfWork(metaclass=ABCMeta):
    @property
    @abstractmethod
    def some_entity_repository(self) -> ABCSomeEntityRepository:
        pass
