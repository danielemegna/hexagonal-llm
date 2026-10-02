import textwrap

from common.prompt import Prompt


class GrabMotorcycleSpecs(Prompt):
    advertisement: str

    def __init__(self, advertisement: str):
        self.advertisement = advertisement

    def __str__(self) -> str:
        return textwrap.dedent("""
        You are a data extractor. Given this advertisement for a motorcycle:
        ```
        {adv}
        ```
        
        Provide me a yaml object with the following keys:
        - brand (string)
        - power_cv (number)
        - displacement_cc (number)
        - price_range (one of the following: `< 5.000 €`, `5.000-7.500 €`, `7.500–10.000 €`, `10.000–15.000 €`, `15.000–20.000 €`, `20.000–30.000 €`, `> 30.000 €`, `N/A`)
        - types (list of strings from the following: `Adventure`, `Bagger`, `Bobber`, `Cafe Racer`, `Carenata`, `Classic`, `Cruiser`, `Enduro`, `Motard`, `Naked`, `Scrambler`, `Sport-Touring`, `Sportbike`, `Touring`)
        - year (integer)
        
        Some other rules:
        - Answer only with the yaml content without any other word or symbol (no markdown, no comments, no yaml block code quotes)
        - If the price is not specified, use N/A
        - Price ranges are closed on the left and open on the right
        - In the text, the price may be stated exactly in numerals, exactly in words, expressed as a range, or omitted
        """).format(
            adv=self.advertisement
        )
