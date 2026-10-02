
import yaml

from aimotorcycle.motorcycle_advertisement_analyzer import MotorcycleAdvertisementAnalyzer, MotorcycleSpecs, PriceRange, \
    MotorcycleType
from aimotorcycle.prompts.grab_motorcycle_specs import GrabMotorcycleSpecs
from common.http_llm_client import HttpLLMClient


class AIMotorcycleAdvertisementAnalyzer(MotorcycleAdvertisementAnalyzer):
    llm_client: HttpLLMClient

    def __init__(self, model: str):
        self.llm_client = HttpLLMClient(model)

    def analyze(self, advertisement: str) -> MotorcycleSpecs:
        prompt = GrabMotorcycleSpecs(advertisement)

        response = self.llm_client.launch_prompt(prompt)
        data = yaml.safe_load(response)

        return MotorcycleSpecs(
            brand=data['brand'],
            power_cv=data['power_cv'],
            displacement_cc=data['displacement_cc'],
            price_range=PriceRange(data['price_range']),
            types=[MotorcycleType(t) for t in data['types']],
            year=data['year'],
        )
