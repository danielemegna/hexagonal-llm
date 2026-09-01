from abc import ABC, abstractmethod
from dataclasses import dataclass

from aifoodfacts.openfoodfacts_client import OpenFoodFacts


@dataclass
class InterpretedFoodFacts:
    ingredients: list[str]
    allergens: list[str]
    additives: list[str]


class FoodFactsInterpreter(ABC):
    @abstractmethod
    def transform(self, open_food_facts: OpenFoodFacts) -> InterpretedFoodFacts:
        pass
