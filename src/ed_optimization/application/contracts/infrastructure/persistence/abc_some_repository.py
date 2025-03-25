from abc import ABCMeta

from ed_optimization.application.contracts.infrastructure.persistence.abc_generic_repository import (
    ABCGenericRepository,
)
from ed_optimization.domain.entities.some_entity import SomeEntity


class ABCSomeEntityRepository(
    ABCGenericRepository[SomeEntity],
    metaclass=ABCMeta,
): ...
