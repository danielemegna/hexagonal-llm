from unittest import TestCase

from aimotorcycle.ai_motorcycle_advertisement_analyzer import AIMotorcycleAdvertisementAnalyzer
from aimotorcycle.motorcycle_advertisement_analyzer import MotorcycleSpecs, PriceRange, MotorcycleType


class TestAIMotorcycleAdvertisementAnalyzer(TestCase):
    analyzer = AIMotorcycleAdvertisementAnalyzer("Qwen3.6-35B-A3B-4bit")

    def test_advertisement_1_yamaha_fz8_naked(self):
        actual = self.analyzer.analyze(
            "Se ti stai chiedendo quale sia la prossima moto da mettere in garage, la Yamaha FZ8 ha una risposta convincente. La Yamaha FZ8 è una naked bike, senza compromessi. Con i suoi 779 centimetri cubi di cilindrata, il motore offre una spinta corposa a ogni regime. Telaio e motore restano in vista, esibiti con orgoglio come in ogni naked che si rispetti.\n\nSi tratta della versione prodotta nel 2015. Parliamo di centosei cavalli: numeri che raccontano bene il carattere di questa moto. Il prezzo è di 7.690 euro. Vieni a provarla: il test ride è il modo migliore per innamorarsene."
        )
        expected = MotorcycleSpecs(
            brand="Yamaha",
            power_cv=106.0,
            displacement_cc=779,
            price_range=PriceRange.FROM_7500_TO_10000,
            types={MotorcycleType.NAKED},
            year=2015,
        )
        self.assertEqual(expected, actual)

    def test_advertisement_2_royal_enfield_continental_gt_650_cafe_racer_classic(self):
        actual = self.analyzer.analyze(
            "Presentiamo la Royal Enfield Continental GT 650, una moto che mette d'accordo testa e cuore. Chiamatela pure una café racer e una moto classica: la Continental GT 650 è tutto questo allo stesso tempo. I cerchi in lega leggera riducono le masse non sospese e migliorano l'agilità. Dai 648 centimetri cubi di cilindrata escono 47 CV (34,6 kW), erogati con una linearità esemplare. Le sospensioni lavorano con precisione e assorbono le asperità senza scomporre l'assetto. Le cromature e le linee senza tempo richiamano la tradizione, con componentistica moderna sotto la pelle.\n\nSemimanubri, codino monoposto e serbatoio scavato portano in strada lo spirito delle cafe racer. Il sound allo scarico è pieno e coinvolgente, senza risultare invadente nei lunghi tratti. Questa unità è uscita dalla fabbrica nel duemilaventitré. Gli specchietti offrono una visuale posteriore ampia e pulita, senza vibrazioni fastidiose. Il prezzo si colloca tra i cinquemila e i settemilacinquecento euro. Ti aspettiamo per farti vivere l'esperienza dal vivo."
        )
        expected = MotorcycleSpecs(
            brand="Royal Enfield",
            power_cv=47.0,
            displacement_cc=648,
            price_range=PriceRange.FROM_5000_TO_7500,
            types={MotorcycleType.CAFE_RACER, MotorcycleType.CLASSIC},
            year=2023,
        )
        self.assertEqual(expected, actual)

    def test_advertisement_3_ktm_690_enduro_r_enduro(self):
        actual = self.analyzer.analyze(
            "Oggi parliamo della KTM 690 Enduro R, una moto che si fa ricordare. La KTM 690 Enduro R è un'enduro, senza compromessi. Scheda tecnica alla mano: seicentonovantatré centimetri cubi di cilindrata e 74 cavalli di potenza massima. La manutenzione ha intervalli lunghi, un vantaggio concreto per chi usa la moto tutti i giorni. Model year 2022, con tutti gli aggiornamenti previsti per quella stagione. Sui sentieri sassosi l'enduro mostra la sua vera anima, leggera e precisa. Le pedane sono posizionate con cura, per non affaticare le gambe dopo ore di guida. Parliamo di una cifra fra 10.000 e 15.000 euro. Ti aspettiamo per farti vivere l'esperienza dal vivo."
        )
        expected = MotorcycleSpecs(
            brand="KTM",
            power_cv=74.0,
            displacement_cc=693,
            price_range=PriceRange.FROM_10000_TO_15000,
            types={MotorcycleType.ENDURO},
            year=2022,
        )
        self.assertEqual(expected, actual)

    def test_advertisement_4_moto_guzzi_california_1400_cruiser_touring(self):
        actual = self.analyzer.analyze(
            "Chi ha provato la Moto Guzzi California 1400 lo sa: scendere è la parte più difficile. Per categoria, la California 1400 è una power cruiser e una gran turismo allo stesso tempo, e lo dichiara già da ferma. I cerchi in lega leggera riducono le masse non sospese e migliorano l'agilità. Il sound allo scarico è pieno e coinvolgente, senza risultare invadente nei lunghi tratti. Il peso contenuto si avverte già nelle manovre da fermo e ancora di più in movimento. Le vibrazioni sono ben filtrate, così mani e piedi non si affaticano. Parliamo di novantasei cavalli: numeri che raccontano bene il carattere di questa moto. La presa USB sotto il cruscotto permette di ricaricare il telefono durante il tragitto. Il raggio di sterzata ridotto semplifica le inversioni e i parcheggi stretti. Immatricolabile come modello 2016, arriva con la dotazione completa di quell'anno.\n\nIl passeggero trova un posto comodo, con maniglie ben posizionate. Il cambio è preciso e, dove previsto, il quickshifter rende ogni cambiata rapidissima. La posizione di guida trova un buon equilibrio fra controllo e comfort sulle distanze medie. La connettività con lo smartphone consente di gestire navigazione, chiamate e musica senza distrazioni. I consumi sono ragionevoli per la categoria, a vantaggio dell'autonomia. La finanziaria del concessionario propone rate su misura per ogni esigenza. La cilindrata di 1.380 cc garantisce coppia piena e un suono inconfondibile. Il cruise control e le manopole riscaldabili fanno di ogni trasferimento un viaggio rilassato. Parliamo di una cifra nella fascia 15.000-20.000 €. Contattaci per fissare un appuntamento e scoprire tutte le condizioni."
        )
        expected = MotorcycleSpecs(
            brand="Moto Guzzi",
            power_cv=96.0,
            displacement_cc=1380,
            price_range=PriceRange.FROM_15000_TO_20000,
            types={MotorcycleType.CRUISER, MotorcycleType.TOURING},
            year=2016,
        )
        self.assertEqual(expected, actual)

    def test_advertisement_5_suzuki_gladius_650_naked_without_price(self):
        actual = self.analyzer.analyze(
            "Occasione da non perdere: la Suzuki Gladius 650 ti aspetta in concessionaria. Sotto ogni punto di vista la Gladius 650 è una naked. La garanzia ufficiale copre la moto per un periodo che offre tranquillità all'acquisto. Le mappature motore permettono di adattare la risposta del gas allo stile di guida e al fondo stradale. Il sound allo scarico è pieno e coinvolgente, senza risultare invadente nei lunghi tratti. La componentistica di qualità, dai cerchi alle pinze, è all'altezza delle aspettative. Con 72 cavalli a disposizione, i sorpassi diventano una formalità. La moto in questione è stata costruita nel 2015. La sella è imbottita con cura e resta comoda anche dopo un paio d'ore.\n\nIl comportamento su strada è prevedibile e trasmette fiducia anche a chi ha meno esperienza. Il cavalletto centrale e i ganci per le cinghie rendono semplice la vita di tutti i giorni. La frizione antisaltellamento rende le scalate più morbide e la guida più fluida. Il manubrio largo e la posizione eretta la rendono agile nel traffico e divertente tra le curve. Il peso contenuto si avverte già nelle manovre da fermo e ancora di più in movimento. Lo sterzo è leggero e preciso, e la moto va esattamente dove si guarda. Il cuore della moto è un'unità da 645 centimetri cubi, affidabile e generosa. Le pedane sono posizionate con cura, per non affaticare le gambe dopo ore di guida. Il resto lo scoprirai in sella."
        )
        expected = MotorcycleSpecs(
            brand="Suzuki",
            power_cv=72.0,
            displacement_cc=645,
            price_range=PriceRange.NOT_AVAILABLE,
            types={MotorcycleType.NAKED},
            year=2015,
        )
        self.assertEqual(expected, actual)

    def test_advertisement_6_harley_davidson_nightster_cruiser(self):
        actual = self.analyzer.analyze(
            "Ogni uscita in sella alla Harley-Davidson Nightster diventa un piccolo evento. Chi cerca una power cruiser trova nella Nightster la risposta giusta. Il cambio è preciso e, dove previsto, il quickshifter rende ogni cambiata rapidissima. Parliamo del modello 2023, con la dotazione di serie di quella stagione. Le mappature motore permettono di adattare la risposta del gas allo stile di guida e al fondo stradale. Si guida rilassati, con il motore che pulsa sotto di sé e il paesaggio che scorre lento. Nel traffico cittadino il calore del motore resta ben gestito, anche d'estate. I consumi sono ragionevoli per la categoria, a vantaggio dell'autonomia. L'illuminazione full LED migliora la visibilità di notte e dà al frontale un'identità precisa. Le colorazioni disponibili spaziano da tinte sobrie a livree più audaci. Dai 975 centimetri cubi di cilindrata escono 90 CV, erogati con una linearità esemplare. Tutto questo a 13.740 euro. Passa a trovarci in concessionaria e siediti in sella."
        )
        expected = MotorcycleSpecs(
            brand="Harley-Davidson",
            power_cv=90.0,
            displacement_cc=975,
            price_range=PriceRange.FROM_10000_TO_15000,
            types={MotorcycleType.CRUISER},
            year=2023,
        )
        self.assertEqual(expected, actual)

    def test_advertisement_7_honda_cb1000r_naked(self):
        actual = self.analyzer.analyze(
            "La Honda CB1000R non si limita a portarti da un punto all'altro: ti fa venire voglia di allungare la strada. Nata per essere una naked pura, la CB1000R mantiene la promessa appena si gira la chiave. La componentistica di qualità, dai cerchi alle pinze, è all'altezza delle aspettative. Scheda tecnica alla mano: 998 cc di cilindrata e 145 CV (106,6 kW) di potenza massima. La connettività con lo smartphone consente di gestire navigazione, chiamate e musica senza distrazioni. Si tratta della versione prodotta nel 2023. La garanzia ufficiale copre la moto per un periodo che offre tranquillità all'acquisto. Il ride-by-wire rende la risposta dell'acceleratore dolce ai bassi regimi e pronta quando si apre tutto. L'impianto frenante firmato da un marchio di riferimento assicura una staccata sicura. Le mappature motore permettono di adattare la risposta del gas allo stile di guida e al fondo stradale. La posizione di guida trova un buon equilibrio fra controllo e comfort sulle distanze medie. Le pedane sono posizionate con cura, per non affaticare le gambe dopo ore di guida. La finanziaria del concessionario propone rate su misura per ogni esigenza. Il sound allo scarico è pieno e coinvolgente, senza risultare invadente nei lunghi tratti. Il sistema di monitoraggio della pressione degli pneumatici avvisa subito in caso di anomalie. Il prezzo si colloca tra i 10.000 e i 15.000 euro. Scrivici per maggiori informazioni o per prenotare una prova su strada."
        )
        expected = MotorcycleSpecs(
            brand="Honda",
            power_cv=145.0,
            displacement_cc=998,
            price_range=PriceRange.FROM_10000_TO_15000,
            types={MotorcycleType.NAKED},
            year=2023,
        )
        self.assertEqual(expected, actual)

    def test_advertisement_8_mv_agusta_brutale_800_naked(self):
        actual = self.analyzer.analyze(
            "Accendi il motore della MV Agusta Brutale 800 e il resto del mondo passa in secondo piano. Chiamatela pure una naked pura: la Brutale 800 è tutto questo. Telaio e motore restano in vista, esibiti con orgoglio come in ogni naked che si rispetti. Il sistema di monitoraggio della pressione degli pneumatici avvisa subito in caso di anomalie. La finanziaria del concessionario propone rate su misura per ogni esigenza. Il comportamento su strada è prevedibile e trasmette fiducia anche a chi ha meno esperienza. La verniciatura resiste bene agli agenti atmosferici e mantiene la brillantezza nel tempo. Il cavalletto centrale e i ganci per le cinghie rendono semplice la vita di tutti i giorni. La chiave di prossimità evita di cercarla in tasca a ogni sosta.\n\nLa moto in questione è stata costruita nel 2020. Il motore da 798 cm³ sviluppa 110 cavalli, con una risposta pronta e fluida. Gli specchietti offrono una visuale posteriore ampia e pulita, senza vibrazioni fastidiose. La garanzia ufficiale copre la moto per un periodo che offre tranquillità all'acquisto. Gli accessori originali permettono di personalizzarla secondo i propri gusti. La connettività con lo smartphone consente di gestire navigazione, chiamate e musica senza distrazioni. La presa USB sotto il cruscotto permette di ricaricare il telefono durante il tragitto. Il prezzo si colloca tra i diecimila e i quindicimila euro. Ti aspettiamo per farti vivere l'esperienza dal vivo."
        )
        expected = MotorcycleSpecs(
            brand="MV Agusta",
            power_cv=110.0,
            displacement_cc=798,
            price_range=PriceRange.FROM_10000_TO_15000,
            types={MotorcycleType.NAKED},
            year=2020,
        )
        self.assertEqual(expected, actual)

    def test_advertisement_9_ducati_streetfighter_v4_naked(self):
        actual = self.analyzer.analyze(
            "Accendi il motore della Ducati Streetfighter V4 e il resto del mondo passa in secondo piano. Per categoria, la Streetfighter V4 è una naked pura, e lo dichiara già da ferma. Con 208 cv a disposizione, i sorpassi diventano una formalità. Il sound allo scarico è pieno e coinvolgente, senza risultare invadente nei lunghi tratti.\n\nIl propulsore ha una cilindrata di 1103 cm³. Immatricolabile come modello 2021, arriva con la dotazione completa di quell'anno. Tutto questo a € 21.900. Passa a trovarci in concessionaria e siediti in sella."
        )
        expected = MotorcycleSpecs(
            brand="Ducati",
            power_cv=208.0,
            displacement_cc=1103,
            price_range=PriceRange.FROM_20000_TO_30000,
            types={MotorcycleType.NAKED},
            year=2021,
        )
        self.assertEqual(expected, actual)

    def test_advertisement_10_ducati_monster_821_naked(self):
        actual = self.analyzer.analyze(
            "C'è una moto che fa girare la testa appena si accende, ed è la Ducati Monster 821. Sotto ogni punto di vista la Monster 821 è una naked pura. La qualità delle finiture si nota nei dettagli, dalle saldature del telaio ai comandi al manubrio. Il controllo di trazione regolabile e l'ABS cornering aiutano a guidare con serenità anche sul bagnato. 109 cv ricavati da ottocentoventuno centimetri cubi: un rapporto che la dice lunga sulla raffinatezza del progetto.\n\nI consumi sono ragionevoli per la categoria, a vantaggio dell'autonomia. La moto in questione è stata costruita nel 2018. La finanziaria del concessionario propone rate su misura per ogni esigenza. Il cavalletto centrale e i ganci per le cinghie rendono semplice la vita di tutti i giorni. Prezzo richiesto: 10.340 euro. Chiamaci oggi stesso: potrebbe essere la moto giusta per te."
        )
        expected = MotorcycleSpecs(
            brand="Ducati",
            power_cv=109.0,
            displacement_cc=821,
            price_range=PriceRange.FROM_10000_TO_15000,
            types={MotorcycleType.NAKED},
            year=2018,
        )
        self.assertEqual(expected, actual)

    def test_advertisement_11_ducati_multistrada(self):
        actual = self.analyzer.analyze(
            "C'è un momento, in ogni viaggio, in cui l'asfalto finisce e la strada diventa sterrato. La maggior parte delle moto ti costringe a scegliere se fermarti o tornare indietro, mentre la Ducati Multistrada V4 S del 2025 ti invita a proseguire. Borgo Panigale l'ha progettata per chi non vuole rinunciare a nulla: è un'adventure capace di affrontare le piste bianche del Marocco e, il giorno dopo, di macinare ottocento chilometri di autostrada con il comfort di una vera sport-touring. Il cuore è il V4 Granturismo da 1.158 cc, un motore che eroga 170 CV a 10.750 giri e che sa essere docile come un bicilindrico quando lo chiedi. A bassa velocità la disattivazione della bancata posteriore riduce calore e consumi, così il traffico cittadino smette di essere un tormento. Quando apri il gas sulla statale, la spinta arriva piena e continua, senza vuoti. Le sospensioni semiattive Skyhook leggono il fondo stradale e si adattano in tempo reale, mentre il radar anteriore e posteriore gestisce il cruise control adattivo e ti avvisa dei veicoli nell'angolo cieco. Il serbatoio da 22 litri garantisce un'autonomia generosa, la sella regolabile accoglie pilota e passeggero senza compromessi e il cupolino si alza con una mano mentre guidi. Il prezzo della versione S si colloca tra i 24.000 e i 30.000 euro, a seconda degli allestimenti scelti. È una cifra importante, che però compra una moto con cui si va ovunque, da soli o in due, per un weekend o per un mese. La Multistrada non chiede quale strada vuoi fare: ti chiede soltanto quanto lontano vuoi andare."
        )
        expected = MotorcycleSpecs(
            brand="Ducati",
            power_cv=170,
            displacement_cc=1158,
            price_range=PriceRange.FROM_20000_TO_30000,
            types={MotorcycleType.SPORT_TOURING, MotorcycleType.ADVENTURE},
            year=2025,
        )
        self.assertEqual(expected, actual)
