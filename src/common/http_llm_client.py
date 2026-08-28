from openai import OpenAI
from openai.types.chat import ChatCompletionUserMessageParam

from common.prompt import Prompt


class HttpLLMClient:
    model: str

    def __init__(self, model: str):
        self.model = model

    def launch_prompt(self, prompt: Prompt) -> str:
        client = OpenAI(
            base_url="http://127.0.0.1:8000/v1",
            api_key="omlx-r2ubkki3rkidk34d",
        )

        response = client.chat.completions.create(
            model=self.model,
            messages=[ChatCompletionUserMessageParam(content=str(prompt), role="user")],
            reasoning_effort=None,
            extra_body={
                "chat_template_kwargs": { "enable_thinking": False, "thinking": False },
                "think": False,
                "thinking": {"type": "disabled"}
            }
        )

        return response.choices[0].message.content.__str__()
