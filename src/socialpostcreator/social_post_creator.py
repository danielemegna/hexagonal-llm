from abc import ABC, abstractmethod

from common.http_llm_client import HttpLLMClient
from socialpostcreator.prompts.create_social_post_prompt import CreateSocialPostPrompt


class SocialPostCreator(ABC):
    @abstractmethod
    def generate_for(self, experience: str) -> str:
        pass

class AISocialPostCreator(SocialPostCreator):
    llm_client: HttpLLMClient

    def __init__(self, model: str):
        self.llm_client = HttpLLMClient(model)

    def generate_for(self, experience: str) -> str:
        prompt = CreateSocialPostPrompt(experience)
        return self.llm_client.launch_prompt(prompt)
