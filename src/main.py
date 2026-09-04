from pathlib import Path
from pprint import pprint

from aifoodfacts.ai_foodfacts_interpreter import AIFoodFactsInterpreter
from aifoodfacts.foodfacts_interpreter import FoodFactsInterpreter
from aifoodfacts.openfoodfacts_client import OpenFoodFactsClient, HttpOpenFoodFactsClient
from aiticketsupport.ai_support_ticket_analyzer import AISupportTicketAnalyzer
from aiticketsupport.support_ticket_analyzer import SupportTicket
from socialpostcreator.social_post_creator import AISocialPostCreator
from specfinder.ai_spec_finder import AISpecFinder


def main() -> None:
    print("============= LLM as Hexagonal Architecture Port =============\n")

    print("Finding ingredients from openfoodfacts...")
    openfoodfacts_client: OpenFoodFactsClient = HttpOpenFoodFactsClient()
    foodfacts = openfoodfacts_client.fetch_for(8000500248744)
    foodfacts_interpreter: FoodFactsInterpreter = AIFoodFactsInterpreter("Qwen3.6-35B-A3B-4bit")
    interpreted_foodfacts = foodfacts_interpreter.transform(foodfacts)
    pprint(interpreted_foodfacts)

    print("\n===================================\n")

    print("Finding Specs of a personal computer...")
    spec_finder = AISpecFinder("Qwen3.6-35B-A3B-4bit")
    spec = spec_finder.find_for([
        'ASUS ExpertBook B3 Flip B3402FVA-EC0065X Intel® Core™ i7 i7-1355U Ibrido (2 in 1) 35,6 cm (14") Touch screen Full HD 8 GB DDR4-SDRAM 512 GB SSD Wi-Fi 6 (802.11ax) Windows 11 Pro Nero cod. 90NX07N1-M00230'
    ])
    pprint(spec)

    print("\n===================================\n")

    print("Finding ticket kind of a support request...")
    analyzer = AISupportTicketAnalyzer("Qwen3.6-35B-A3B-4bit")
    ticket_kind = analyzer.analyze(SupportTicket(
        subject="Device non si accende",
        message="Il mio dispositivo smette di rispondere completamente dopo poche ore di utilizzo, indipendentemente dalla batteria residua. Ho provato a reinserirlo nella base di ricarica ma la luce di stato resta spenta. Non ho riscontrato problemi prima di questo episodio recente. Chiedo cortesemente assistenza per diagnosticare il guasto hardware.",
    ))
    pprint(ticket_kind)

    print("\n===================================\n")

    print("Generating a social post for your recent experience...")
    social_post_creator = AISocialPostCreator("Qwen3.8-27B-4bit")
    social_post_content = social_post_creator.generate_for(
        experience=Path("src/socialpostcreator/socrates_italia_experience.txt").read_text()
    )
    print(social_post_content)

    print("\n================= Done ==================")


if __name__ == "__main__":
    main()
