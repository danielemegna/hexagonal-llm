import textwrap

from common.prompt import Prompt


class FixInvalidJsonPrompt(Prompt):

    def __init__(self, invalid_json: str):
        self.invalid_json = invalid_json

    def __str__(self) -> str:
        return textwrap.dedent("""
        Fix this invalid json:
        
        {invalid_json}
        
        Some rules:
        - reply with the fixed json without any other character
        - focus on the json structure
        - typical problems are missing special characters escape and missing commas or brackets
        - do not change character, add only character to eventually escape special characters or add missing commas, brackets
        - do not use html encoding to escape special characters
        - pay attention to not double quote special characters with double slash
        """.format(invalid_json = self.invalid_json))
