from pathlib import Path
from pprint import pprint

from aifoodfacts.ai_foodfacts_interpreter import AIFoodFactsInterpreter
from aifoodfacts.foodfacts_interpreter import FoodFactsInterpreter
from aifoodfacts.openfoodfacts_client import OpenFoodFactsClient, HttpOpenFoodFactsClient
from aimotorcycle.ai_motorcycle_advertisement_analyzer import AIMotorcycleAdvertisementAnalyzer
from aiticketsupport.ai_support_ticket_analyzer import AISupportTicketAnalyzer
from aiticketsupport.support_ticket_analyzer import SupportTicket
from fine_tuning import fine_tuning
from socialpostcreator.social_post_creator import AISocialPostCreator
from specfinder.ai_spec_finder import AISpecFinder

def main() -> None:
    demo()
    #fine_tuning()

def demo() -> None:
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
    social_post_creator = AISocialPostCreator("gemma-4-E2B-it-MLX-8bit")
    social_post_content = social_post_creator.generate_for(
        experience=Path("src/socialpostcreator/socrates_italia_experience.txt").read_text()
    )
    print(social_post_content)

    print("\n===================================\n")

    print("Finding motorcycle specs from advertisement...")
    analyzer = AIMotorcycleAdvertisementAnalyzer("Qwen2.5-3B-Instruct-4bit-motorcycle")
    motorcycle_specs = analyzer.analyze(
        "Il marchio Yamaha firma con la MT-03 una delle sue interpretazioni più riuscite. Per categoria, la MT-03 è una naked bike, e lo dichiara già da ferma. Nel traffico cittadino il calore del motore resta ben gestito, anche d'estate. I freni offrono una frenata potente e ben modulabile, anche nelle staccate più decise. Il raggio di sterzata ridotto semplifica le inversioni e i parcheggi stretti. Il sound allo scarico è pieno e coinvolgente, senza risultare invadente nei lunghi tratti. Il ride-by-wire rende la risposta dell'acceleratore dolce ai bassi regimi e pronta quando si apre tutto. Immatricolabile come modello 2016, arriva con la dotazione completa di quell'anno. Il telaio garantisce stabilità alle alte velocità e precisione nei cambi di direzione. La garanzia ufficiale copre la moto per un periodo che offre tranquillità all'acquisto. Il sistema di monitoraggio della pressione degli pneumatici avvisa subito in caso di anomalie. La posizione di guida trova un buon equilibrio fra controllo e comfort sulle distanze medie. Gli specchietti offrono una visuale posteriore ampia e pulita, senza vibrazioni fastidiose. L'illuminazione full LED migliora la visibilità di notte e dà al frontale un'identità precisa. La componentistica di qualità, dai cerchi alle pinze, è all'altezza delle aspettative. La fanaleria posteriore compatta pulisce la linea del codone. Scheda tecnica alla mano: 321 cc di cilindrata e quarantadue cavalli di potenza massima. Il cavalletto centrale e i ganci per le cinghie rendono semplice la vita di tutti i giorni. La finanziaria del concessionario propone rate su misura per ogni esigenza. La frizione antisaltellamento rende le scalate più morbide e la guida più fluida. La verniciatura resiste bene agli agenti atmosferici e mantiene la brillantezza nel tempo. L'investimento richiesto è meno di 5.000 €. Contattaci per fissare un appuntamento e scoprire tutte le condizioni."
    )
    pprint(motorcycle_specs)

    print("\n================= Done ==================")

if __name__ == "__main__":
    main()
