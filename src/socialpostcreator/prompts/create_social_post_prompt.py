import textwrap

from common.prompt import Prompt


class CreateSocialPostPrompt(Prompt):
    experience: str

    def __init__(self, experience: str):
        self.experience = experience

    def __str__(self) -> str:
        return textwrap.dedent("""
        Given the current story about an experience that i did:
        -------------
        {experience_text}
        -------------
        
        Generate a social post i can submit on my social network profiles (linkedin, twitter, facebook)
        
        Some rules:
        - answer with just the content of the post, no comments or other words;
        - stay under 1000 characters and use at least 180;
        - put at least 2 paragraph in the post, where a paragraph is one or more related sentences;
        - the paragraphs are separated by a blank line;
        - a paragraph should be maximum 3 sentences;
        - use some emoji to make the post interesting, i usually put an emoji at the end of every paragraph;
        - start with a short sentence that should attract my followers;
        - put a question as last sentence in order to involve people to comment under the post;
        - put the final question as separated last short paragraph;
        - if the experience is described in Italian, use the Italian for the post; use always the English otherwise;
        """.format(
            experience_text=self.experience
        ))
