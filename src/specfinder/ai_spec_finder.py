
from openai import OpenAI
from openai.types.chat import ChatCompletionUserMessageParam

from specfinder.prompts.operating_system_prompt import OperatingSystemPrompt
from specfinder.spec_finder import SpecFinder, Spec


class AISpecFinder(SpecFinder):

    def find_os_for(self, descriptions: list[str]) -> str:
        prompt = OperatingSystemPrompt(descriptions)
        client = OpenAI(
            base_url="http://127.0.0.1:8000/v1",
            api_key="omlx-xxxxxxxxxxx",
        )

        response = client.chat.completions.create(
            model="Qwen3.6-35B-A3B-4bit",
            messages=[ChatCompletionUserMessageParam(content=str(prompt), role="user")],
            reasoning_effort=None,
            extra_body={
                "chat_template_kwargs": { "enable_thinking": False, "thinking": False },
                "think": False,
                "thinking": {"type": "disabled"}
            }
        )

        return response.choices[0].message.content.__str__()

    def find_for(self, descriptions: list[str]) -> Spec:
        pass
