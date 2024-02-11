from abc import ABC, abstractmethod
from typing import Generic, TypeVar


T = TypeVar("T")
U = TypeVar("U")


class IUseCase(Generic[T, U], ABC):
    @abstractmethod
    def execute(self, params: T) -> U:
        pass
