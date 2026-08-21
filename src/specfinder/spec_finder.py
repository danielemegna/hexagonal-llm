from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Spec:
    hdd_size: str
    hdd_type: str
    display_size: str
    processor_type: str
    ram_size: str
    operating_system: str

class SpecFinder(ABC):

    @abstractmethod
    def find_for(self, descriptions: list[str]) -> Spec:
        pass

    @abstractmethod
    def find_os_for(self, descriptions: list[str]) -> str:
        pass
