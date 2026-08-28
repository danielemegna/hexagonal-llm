from abc import ABC, abstractmethod


class Prompt(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass
