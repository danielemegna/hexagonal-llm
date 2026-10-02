from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class PriceRange(Enum):
    UNDER_5000 = "< 5.000 €"
    FROM_5000_TO_7500 = "5.000-7.500 €"
    FROM_7500_TO_10000 = "7.500–10.000 €"
    FROM_10000_TO_15000 = "10.000–15.000 €"
    FROM_15000_TO_20000 = "15.000–20.000 €"
    FROM_20000_TO_30000 = "20.000–30.000 €"
    OVER_30000 = "> 30.000 €"
    NOT_AVAILABLE = "N/A"


class MotorcycleType(Enum):
    ADVENTURE = "Adventure"
    BAGGER = "Bagger"
    BOBBER = "Bobber"
    CAFE_RACER = "Cafe Racer"
    CARENATA = "Carenata"
    CLASSIC = "Classic"
    CRUISER = "Cruiser"
    ENDURO = "Enduro"
    MOTARD = "Motard"
    NAKED = "Naked"
    SCRAMBLER = "Scrambler"
    SPORT_TOURING = "Sport-Touring"
    SPORTBIKE = "Sportbike"
    TOURING = "Touring"


@dataclass
class MotorcycleSpecs:
  brand: str
  power_cv: float
  displacement_cc: int
  price_range: PriceRange
  types: list[MotorcycleType]
  year: int


class MotorcycleAdvertisementAnalyzer(ABC):

    @abstractmethod
    def analyze(self, advertisement: str) -> MotorcycleSpecs:
        pass
