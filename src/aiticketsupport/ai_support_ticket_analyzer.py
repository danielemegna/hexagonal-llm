import yaml

from aiticketsupport.prompts.recognize_support_ticket import RecognizeSupportTicket
from aiticketsupport.support_ticket_analyzer import SupportTicketAnalyzer, SupportTicket, TicketKind, TicketCategory, Language
from common.http_llm_client import HttpLLMClient


class AISupportTicketAnalyzer(SupportTicketAnalyzer):
    llm_client: HttpLLMClient

    def __init__(self, model: str):
        self.llm_client = HttpLLMClient(model)

    def analyze(self, ticket: SupportTicket) -> TicketKind:
        prompt = RecognizeSupportTicket(ticket)

        response = self.llm_client.launch_prompt(prompt)
        data = yaml.safe_load(response)

        return TicketKind(
           category=TicketCategory[data['category']],
           language=Language[data['language']]
        )

