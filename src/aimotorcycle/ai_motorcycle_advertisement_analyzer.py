
import yaml

from aimotorcycle.motorcycle_advertisement_analyzer import MotorcycleAdvertisementAnalyzer, MotorcycleSpecs
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

        return MotorcycleSpecs(**data)
