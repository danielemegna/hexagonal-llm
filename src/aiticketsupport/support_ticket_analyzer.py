from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto


class TicketCategory(Enum):
    WEBAPP_SUPPORT = auto()
    DEVICE_SUPPORT = auto()
    WEBAPP_DEFECT = auto()
    DEVICE_DEFECT = auto()
    COMMERCIAL_REQUEST = auto()
    OTHER = auto()


class Language(Enum):
    ITALIAN = auto()
    ENGLISH = auto()
    FRENCH = auto()


@dataclass
class SupportTicket:
    subject: str
    message: str


@dataclass
class TicketKind:
    category: TicketCategory
    language: Language


class SupportTicketAnalyzer(ABC):

    @abstractmethod
    def analyze(self, ticket: SupportTicket) -> TicketKind:
        pass
