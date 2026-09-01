import yaml

from aifoodfacts.foodfacts_interpreter import FoodFactsInterpreter, InterpretedFoodFacts
from aifoodfacts.openfoodfacts_client import OpenFoodFacts
from aifoodfacts.prompts.StructureFoodFacts import StructureFoodFacts
from common.http_llm_client import HttpLLMClient


class AIFoodFactsInterpreter(FoodFactsInterpreter):
    llm_client: HttpLLMClient

    def __init__(self, model: str):
        self.llm_client = HttpLLMClient(model)

    def transform(self, open_food_facts: OpenFoodFacts) -> InterpretedFoodFacts:
        prompt = StructureFoodFacts(open_food_facts)
        response = self.llm_client.launch_prompt(prompt)

        data: list[str] = yaml.safe_load(response)

        return InterpretedFoodFacts(
            ingredients=data,
            allergens=['glutine', 'latte', 'noci', 'soia'],
            additives=["e322", "e500", "e500ii"]
        )
