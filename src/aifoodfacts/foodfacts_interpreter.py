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


class HttpAIFoodFactsInterpreter(FoodFactsInterpreter):
    def transform(self, open_food_facts: OpenFoodFacts) -> InterpretedFoodFacts:
        return InterpretedFoodFacts(
            ingredients=[
                "cioccolato al latte",
                "zucchero",
                "burro di cacao",
                "massa di cacao",
                "latte scremato in polvere",
                "burro concentrato",
                "lecitine",
                "nocciole",
                "olio di palma",
                "farina di frumento",
                "siero di latte in polvere",
                "cacao a ridotto contenuto di grasso",
                "bicarbonato di sodio",
                "sale",
                "vanillina"
            ],
            allergens=['glutine', 'latte', 'noci', 'soia'],
            additives=["e322", "e500", "e500ii"]
        )
