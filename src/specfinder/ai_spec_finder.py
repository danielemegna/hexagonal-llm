
import yaml

from common.http_llm_client import HttpLLMClient
from specfinder.prompts.operating_system_prompt import OperatingSystemPrompt
from specfinder.prompts.total_spec_prompt import TotalSpecPrompt
from specfinder.spec_finder import SpecFinder, Spec


class AISpecFinder(SpecFinder):
    llm_client: HttpLLMClient

    def __init__(self, model: str):
        self.llm_client = HttpLLMClient(model)

    def find_os_for(self, descriptions: list[str]) -> str:
        prompt = OperatingSystemPrompt(descriptions)
        return self.llm_client.launch_prompt(prompt)

    def find_for(self, descriptions: list[str]) -> Spec:
        prompt = TotalSpecPrompt(descriptions)
        response = self.llm_client.launch_prompt(prompt)

        data = yaml.safe_load(response)

        return Spec(
            hdd_size=data["hdd_size"],
            hdd_type=data["hdd_type"],
            display_size=data["display_size"],
            processor_type=data["processor_type"],
            ram_size=data["ram_size"],
            operating_system=data["operating_system"]
        )
