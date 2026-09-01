from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class OpenFoodFacts:
    ingredients_text: list[dict[str, str]]
    allergens_tags: list[str]
    additives_tags: list[str]


class OpenFoodFactsClient(ABC):
    @abstractmethod
    def fetch_for(self, gtin: int) -> OpenFoodFacts:
        pass


class HttpOpenFoodFactsClient(OpenFoodFactsClient):
    def fetch_for(self, gtin: int) -> OpenFoodFacts:
        # fake data simulating remote http fetch
        return OpenFoodFacts(
            ingredients_text=[{
                "lang": "main",
                "text": "MILK chocolate 30% (sugar, cocoa butter, cocoa mass, skimmed MILK powder, concentrated BUTTER, emulsifier: lecithins (SOYA), vanillin), HAZELNUTS (28.5%), sugar, palm oil, WHEAT flour, whey powder (MILK), fat-reduced cocoa, Emulsifier: lecithins (SOYA), raising agent (sodium bicarbonate), salt, vanillin"
            }, {
                "lang": "it",
                "text": "30% di cioccolato al latte (zucchero, burro di cacao, massa di cacao, latte scremato in polvere, burro concentrato, emulsionante: lecitine (<span class=\"allergen\">soia</span>), vanillina), <span class=\"allergen\">nocciole</span> (28,5%), zucchero, olio di palma, <span class=\"allergen\">farina di frumento</span>, siero di latte in polvere (<span class=\"allergen\">latte</span>), cacao a ridotto contenuto di grasso, emulsionante: lecitine (<span class=\"allergen\">soya</span>), agente lievitante (bicarbonato di sodio), sale, vanillina"
            }, {
                "lang": "de",
                "text": "MILCHSCHOKOLADE 30% (Zucker, Kakaobutter, Kakaomasse, MAGERMILCHPULVER, BUTTERREINFETT, Emulgator: Lecithine (SOJA); Vanillin), HASELNÜSSE (28.5%), Zucker, Palmöl, WEIZENMEHL, SÜSSMOLKENPULVER, fettarmer Kakao, Emulgator: Lecithine (SOJA), Backtriebmittel (Natriumhydrogencarbonat), Salz, Vanillin"
            }, {
                "lang": "en",
                "text": "<span class=\"allergen\">MILK</span> </span>chocolate 30% (sugar, cocoa butter, cocoa mass, skimmed <span class=\"allergen\">MILK</span> </span>powder, concentrated <span class=\"allergen\">BUTTER</span>, emulsifier: lecithins (<span class=\"allergen\">SOYA</span>), vanillin), <span class=\"allergen\">HAZELNUTS</span> (28.5%), sugar, palm oil, <span class=\"allergen\">WHEAT</span> </span>flour, whey powder (<span class=\"allergen\">MILK</span>), fat-reduced cocoa, Emulsifier: lecithins (<span class=\"allergen\">SOYA</span>), raising agent (sodium bicarbonate), salt, vanillin"
            }, {
                "lang": "hr",
                "text": "MLIJEČNA čokolada 30% (šećer, kakaov maslac, kakaova masa, obrano MLIJEKO u prahu, bezvodna MLIJEČNA mast, emulgator: lecitini (SOJA); vanilin), LJEŠNJACI (28,5%), šećer, palmino ulje, PŠENIČNO brašno, SIRUTKA u prahu, kakao smanjene masti, emulgator: lecitini (SOJA), tvar za rahljenje (natrijev hidrogen karbonat), kuhinjska sol, vanilin."
            }, {
                "lang": "fr",
                "text": "Chocolat au lait 30% (sucre, beurre de cacao, pâte de cacao lait écrémé en poudre, beurre concentré, émulsifiant : lécithines (soja); vanilline), noisettes (28,5%), sucre, huile de palme, farine de froment, lactosérum en poudre, cacao maigre, émulsifiant : lécithines (soja), poudre à lever : carbonate acide de sodium, sel, vanilline."
            }, {
                "lang": "hr",
                "text": "MLIJEČNA čokolada 30% (šećer, kakaov maslac, kakaova masa, obrano <span class=\"allergen\">MLIJEKO</span> </span>u prahu, bezvodna MLIJEČNA mast, emulgator: lecitini (<span class=\"allergen\">SOJA</span>); vanilin), <span class=\"allergen\">LJEŠNJACI</span> (28,5%), šećer, palmino ulje, <span class=\"allergen\">PŠENIČNO brašno</span>, <span class=\"allergen\">SIRUTKA</span> </span>u prahu, kakao smanjene masti, emulgator: lecitini (<span class=\"allergen\">SOJA</span>), tvar za rahljenje (natrijev hidrogen karbonat), kuhinjska sol, vanilin."
            }, {
                "lang": "fr",
                "text": "Chocolat au lait 30% (sucre, beurre de cacao, pâte de cacao lait écrémé en poudre, <span class=\"allergen\">beurre concentré</span>, émulsifiant : lécithines (<span class=\"allergen\">soja</span>); vanilline), <span class=\"allergen\">noisettes</span> (28,5%), sucre, huile de palme, farine de <span class=\"allergen\">froment</span>, lactosérum en poudre, cacao maigre, émulsifiant : lécithines (<span class=\"allergen\">soja</span>), poudre à lever : carbonate acide de sodium, sel, vanilline."
            }, {
                "lang": "en",
                "text": "MILK chocolate 30% (sugar, cocoa butter, cocoa mass, skimmed MILK powder, concentrated BUTTER, emulsifier: lecithins (SOYA), vanillin), HAZELNUTS (28.5%), sugar, palm oil, WHEAT flour, whey powder (MILK), fat-reduced cocoa, Emulsifier: lecithins (SOYA), raising agent (sodium bicarbonate), salt, vanillin"
            }, {
                "lang": "it",
                "text": "30% di cioccolato al latte (zucchero, burro di cacao, massa di cacao, latte scremato in polvere, burro concentrato, emulsionante: lecitine (soia), vanillina), nocciole (28,5%), zucchero, olio di palma, farina di frumento, siero di latte in polvere (latte), cacao a ridotto contenuto di grasso, emulsionante: lecitine (soya), agente lievitante (bicarbonato di sodio), sale, vanillina",
            }, {
                "lang": "de",
                "text": "<span class=\"allergen\">MILCHSCHOKOLADE</span> </span>30% (Zucker, Kakaobutter, Kakaomasse, <span class=\"allergen\">MAGERMILCHPULVER</span>, <span class=\"allergen\">BUTTERREINFETT</span>, Emulgator: Lecithine (<span class=\"allergen\">SOJA</span>); Vanillin), <span class=\"allergen\">HASELNÜSSE</span> (28.5%), Zucker, Palmöl, <span class=\"allergen\">WEIZENMEHL</span>, <span class=\"allergen\">SÜSSMOLKENPULVER</span>, fettarmer Kakao, Emulgator: Lecithine (<span class=\"allergen\">SOJA</span>), Backtriebmittel (Natriumhydrogencarbonat), Salz, Vanillin"
            }],
            allergens_tags=[
                "en:gluten",
                "en:milk",
                "en:nuts",
                "en:soybeans"
            ],
            additives_tags=[
                "en:e322",
                "en:e500",
                "en:e500ii"
            ]
        )
