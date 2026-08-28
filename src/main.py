from pprint import pprint

from aifoodfacts.foodfacts_interpreter import FoodFactsInterpreter, HttpAIFoodFactsInterpreter
from aifoodfacts.openfoodfacts_client import OpenFoodFactsClient, HttpOpenFoodFactsClient
from specfinder.ai_spec_finder import AISpecFinder


def main() -> None:
    print("============= LLM as Hexagonal Architecture Port =============")

    print("Finding ingredients from openfoodfacts...")
    openfoodfacts_client: OpenFoodFactsClient = HttpOpenFoodFactsClient()
    foodfacts = openfoodfacts_client.fetch_for(8000500248744)
    foodfacts_interpreter: FoodFactsInterpreter = HttpAIFoodFactsInterpreter()
    interpreted_foodfacts = foodfacts_interpreter.transform(foodfacts)
    pprint(interpreted_foodfacts)

    print("===================================")

    print("Finding Specs of ASUS ExpertBook ...")
    spec_finder = AISpecFinder("Qwen3.6-35B-A3B-4bit")
    spec = spec_finder.find_for([
        'ASUS ExpertBook B3 Flip B3402FVA-EC0065X Intel® Core™ i7 i7-1355U Ibrido (2 in 1) 35,6 cm (14") Touch screen Full HD 8 GB DDR4-SDRAM 512 GB SSD Wi-Fi 6 (802.11ax) Windows 11 Pro Nero cod. 90NX07N1-M00230'
    ])
    pprint(spec)

    print("================= Done ==================")


if __name__ == "__main__":
    main()
