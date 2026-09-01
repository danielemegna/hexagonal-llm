import textwrap

from aifoodfacts.openfoodfacts_client import OpenFoodFacts
from common.prompt import Prompt


class StructureFoodFacts(Prompt):
    facts: OpenFoodFacts

    def __init__(self, facts: OpenFoodFacts):
        self.facts = facts

    def __str__(self) -> str:
        return textwrap.dedent("""
        Given this information about the ingredients of a certain product, provided in multiple languages:
        ```
        {ingredients}
        ```
        
        Provide me a yaml version in which the ingredients are elements of a simple array
        containing only the ingredient name in Italian, without quantities or percentages.
        Put in the yaml just an array with no key wrapping it.
        
        Some other rules:
        - Answer only with the yaml content without any other word or symbol (no markdown, no comments)
        - I don't expect to find duplicate ingredients (with the exact same name)
        - You can use the Italian description as your primary reference, and use the other versions only to cross-check the result
        - If you’re unsure about two ingredients that seem to refer to the same thing, avoid removing duplicates and leave both ingredients with their two different names
        - If one of the ingredients also appears to be an allergen, be sure to keep it, do not remove it from the ingredients 
        """).format(
            ingredients=self.facts.ingredients_text
        )
