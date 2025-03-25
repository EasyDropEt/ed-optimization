from ed_optimization.application.contracts.infrastructure.persistence.abc_some_repository import (
    ABCSomeEntityRepository,
)
from ed_optimization.application.contracts.infrastructure.persistence.abc_unit_of_work import (
    ABCUnitOfWork,
)
from ed_optimization.infrastructure.persistence.db_client import DbClient
from ed_optimization.infrastructure.persistence.repositories.some_entity_repository import (
    SomeEntityRepository,
)


class UnitOfWork(ABCUnitOfWork):
    def __init__(self, db_client: DbClient) -> None:
        self._some_entity_repository = SomeEntityRepository(db_client)

    @property
    def some_entity_repository(self) -> ABCSomeEntityRepository:
        return self._some_entity_repository
