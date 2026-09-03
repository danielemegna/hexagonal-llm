from unittest import TestCase

from aiticketsupport.ai_support_ticket_analyzer import AISupportTicketAnalyzer
from aiticketsupport.support_ticket_analyzer import SupportTicket, TicketKind, TicketCategory, Language


class TestAISupportTicketAnalyzer(TestCase):
    analyzer = AISupportTicketAnalyzer("Qwen3.8-27B-4bit")

    def test_ticket_1_webapp_support_italian(self):
        actual = self.analyzer.analyze(SupportTicket(
            subject="Come creare un nuovo progetto?",
            message="Ho appena installato l'applicazione ma non riesco a capire dove si trova il pulsante per avviare una nuova attività. Ho esaminato la schermata principale ma non vedo l'opzione per aggiungere elementi alla lista. Potreste indicarmi il percorso esatto per iniziare? Spero di non aver saltato un passaggio di configurazione iniziale.",
        ))
        expected = TicketKind(
            category=TicketCategory.WEBAPP_SUPPORT,
            language=Language.ITALIAN,
        )
        self.assertEqual(expected, actual)

    def test_ticket_2_device_problem_italian(self):
        actual = self.analyzer.analyze(SupportTicket(
            subject="Device non si accende",
            message="Il mio dispositivo smette di rispondere completamente dopo poche ore di utilizzo, indipendentemente dalla batteria residua. Ho provato a reinserirlo nella base di ricarica ma la luce di stato resta spenta. Non ho riscontrato problemi prima di questo episodio recente. Chiedo cortesemente assistenza per diagnosticare il guasto hardware.",
        ))
        expected = TicketKind(
            category=TicketCategory.DEVICE_DEFECT,
            language=Language.ITALIAN,
        )
        self.assertEqual(expected, actual)

    def test_ticket_3_commercial_request_english(self):
        actual = self.analyzer.analyze(SupportTicket(
            subject="Upgrade subscription plan",
            message="I am currently subscribed to the basic tier but I need access to the advanced analytics features. Could you please explain the process for upgrading my account to the premium plan? I would like to complete the payment via credit card. Thank you for your assistance with this billing inquiry.",
        ))
        expected = TicketKind(
            category=TicketCategory.COMMERCIAL_REQUEST,
            language=Language.ENGLISH,
        )
        self.assertEqual(expected, actual)

    def test_ticket_4_device_support_french(self):
        actual = self.analyzer.analyze(SupportTicket(
            subject="Comment associer les device ?",
            message="Je ne comprends pas comment lier mon appareil physique à l'application sur mon téléphone. J'ai suivi les instructions mais le code QR n'apparait pas sur l'écran du device. Pourriez-vous m'expliquer la procédure étape par étape ? J'ai déjà redémarré les deux appareils sans succès.",
        ))
        expected = TicketKind(
            category=TicketCategory.DEVICE_SUPPORT,
            language=Language.FRENCH,
        )
        self.assertEqual(expected, actual)

    def test_ticket_5_webapp_problem_italian(self):
        actual = self.analyzer.analyze(SupportTicket(
            subject="App lenta nel caricamento",
            message="Da ieri sera la webapp impiega minuti interi per caricare le dashboard, rendendo l'uso quasi impossibile. La connessione internet risulta stabile e veloce anche su altre pagine web. Non ho apportato alcuna modifica alla mia configurazione recente. Vi prego di verificare se ci sono problemi lato server.",
        ))
        expected = TicketKind(
            category=TicketCategory.WEBAPP_DEFECT,
            language=Language.ITALIAN,
        )
        self.assertEqual(expected, actual)

    def test_ticket_6_webapp_support_italian(self):
        actual = self.analyzer.analyze(SupportTicket(
            subject="Come funziona la modalità offline?",
            message="Non sono sicuro di come configurare l'applicazione per operare senza connessione a internet. Ogni volta che provo a creare un nuovo record, il sistema mi richiede un link attivo. Potreste indicarmi dove attivare le impostazioni per la modalità offline? Mi serve poter lavorare anche in zone con segnale debole.",
        ))
        expected = TicketKind(
            category=TicketCategory.WEBAPP_SUPPORT,
            language=Language.ITALIAN,
        )
        self.assertEqual(expected, actual)

    def test_ticket_7_device_problem_english(self):
        actual = self.analyzer.analyze(SupportTicket(
            subject="Bluetooth connection fails",
            message="The physical device fails to pair with my smartphone despite being in range. It shows as detected but immediately disconnects after a few seconds. I have tried updating both the app and the device firmware without success. Please advise on the next troubleshooting steps.",
        ))
        expected = TicketKind(
            category=TicketCategory.DEVICE_DEFECT,
            language=Language.ENGLISH,
        )
        self.assertEqual(expected, actual)

    def test_ticket_8_commercial_request_italian(self):
        actual = self.analyzer.analyze(SupportTicket(
            subject="Estensione abbonamento aziendale",
            message="Il mio contratto aziendale scade tra due settimane e desidero rinnovarlo per i prossimi dodici mesi. Potreste inviarci l'offerta migliore disponibile per il nostro numero di utenti? Sarebbe gradita una fattura elettronica dedicata all'ufficio acquisti. In attesa di un vostro gentile riscontro.",
        ))
        expected = TicketKind(
            category=TicketCategory.COMMERCIAL_REQUEST,
            language=Language.ITALIAN,
        )
        self.assertEqual(expected, actual)

    def test_ticket_9_device_support_italian(self):
        actual = self.analyzer.analyze(SupportTicket(
            subject="Come pulire la lente?",
            message="Non sono sicuro di quale panno o soluzione utilizzare per pulire la lente del sensore senza graffiarla. Il manuale non fornisce indicazioni specifiche sulla manutenzione della superficie ottica. Sono preoccupato per eventuali danni permanenti al dispositivo. Potreste confermare i materiali approvati per la pulizia?",
        ))
        expected = TicketKind(
            category=TicketCategory.DEVICE_SUPPORT,
            language=Language.ITALIAN,
        )
        self.assertEqual(expected, actual)

    def test_ticket_10_other_english(self):
        actual = self.analyzer.analyze(SupportTicket(
            subject="API documentation request",
            message="I am a developer interested in integrating your platform with our internal system. I cannot find comprehensive documentation for the public API endpoints in the current version of the app. Could you direct me to the latest developer portal or SDK? This is a general inquiry, not a bug report.",
        ))
        expected = TicketKind(
            category=TicketCategory.OTHER,
            language=Language.ENGLISH,
        )
        self.assertEqual(expected, actual)
