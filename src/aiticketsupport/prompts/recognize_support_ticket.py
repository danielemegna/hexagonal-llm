import textwrap

from aiticketsupport.support_ticket_analyzer import SupportTicket
from common.prompt import Prompt


class RecognizeSupportTicket(Prompt):
    ticket: SupportTicket

    def __init__(self, ticket: SupportTicket):
        self.ticket = ticket

    def __str__(self) -> str:
        return textwrap.dedent("""
        Given this ticket support content:
        - Subject: "{subject}"
        - Message: "{message}"
        
        Provide me a yaml with two keys only in this form:
        language: [ ITALIAN | ENGLISH | FRENCH ]
        category: [ WEBAPP_SUPPORT | DEVICE_SUPPORT | WEBAPP_DEFECT | DEVICE_DEFECT | COMMERCIAL_REQUEST | OTHER ]
        
        Some other rules:
        - Answer only with the yaml content without any other word or symbol (no markdown symbols, no comments)
        - Use only the allowed values between square brackets
        - Prefer "*_DEFECT" categories for malfunction issues and "*_SUPPORT" categories for request asking for help with the usage unrelated to malfunction issues
        """).format(
            subject=self.ticket.subject,
            message=self.ticket.message,
        )
