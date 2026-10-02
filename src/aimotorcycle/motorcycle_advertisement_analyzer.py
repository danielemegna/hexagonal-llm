from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class MotorcycleSpecs:
  brand: str
  power_cv: float
  displacement_cc: int
  price_range: str #(one of the following: ` < 5.000 €`, `5.000 - 7.500 €`, `7.500–10.000 €`, `10.000–15.000 €`, `15.000–20.000 €`, `20.000–30.000 €`, ` > 30.000 €`, `N / A`)
  types: list[str] #(list of strings from the following: `Adventure`, `Bagger`, `Bobber`, `Cafe Racer `, `Carenata`, `Classic`, `Cruiser`, `Enduro`, `Motard`, `Naked`, `Scrambler`, `Sport - Touring`, `Sportbike`, `Touring`)
  year: int


class MotorcycleAdvertisementAnalyzer(ABC):

    @abstractmethod
    def analyze(self, advertisement: str) -> MotorcycleSpecs:
        pass
