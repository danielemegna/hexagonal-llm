import textwrap

from common.prompt import Prompt

class OperatingSystemPrompt(Prompt):
    descriptions: list[str]

    def __init__(self, descriptions: list[str]):
        self.descriptions = descriptions

    def __str__(self) -> str:
        return textwrap.dedent("""
        Dati questi possibili valori di sistema operativo (separati da carattere /):
        Android 10 / Android 4.1 / Android 4.2 / Android 4.2 (Jelly Bean) / Android 4.2.2, Jelly Bean / Android 4.3 / Android 4.4.2, KitKat / Android 5.1 / Android 5.1.1 / Android 6.0 / Android 7.1 / Android 8.0 / Android 8.1 / Android 9.0 / BlackBerry OS / BlackBerry Tablet OS / ChromeOS / DGX OS / DOSgratuito / Endless OS / FreeDOS / FreeDOS 2.0 / HP ThinPro OS / iOS / Linux / Linux Linpus / Linux Pantheon OS / Linux Ubuntu / Mac OS Catalina / Mac OS X 10.10 Yosemite / Mac OS X 10.11 El Capitan / Mac OS X 10.14 Mojave / Mac OS X 10.7 Lion / Mac OS X 10.8 Mountain Lion / Mac OS X 10.9 Mavericks / Mac OS X Lion Server / Mac OS X Mavericks / Mac OS X Server Snow Leopard / macOS Big Sur / macOS Catalina / macOS Catalina 10.15 / macOS High Sierra 10.13 / macOS Mojave / macOS Mojave 10.14 / macOS Monterey / macOS Sequoia / macOS Sierra / macOS Sierra 10.12 / macOS Sonoma / macOS Tahoe / macOS Ventura / Microsoft Windows 10 IoT Enterprise / No / Non specificato / Office 365 Personal 1-year / Steam OS / ThinOX 8 / ThinPro / Ubuntu / Ubuntu Linux / Windows / Windows 10 / Windows 10 Education / Windows 10 Enterprise / Windows 10 Family / Windows 10 Home / Windows 10 Home S / Windows 10 IoT / Windows 10 IoT Core / Windows 10 IoT Enterprise / Windows 10 IoT Enterprise LTSB / Windows 10 IoT Enterprise SAC / Windows 10 Pro / Windows 10 Pro Academic / Windows 10 Pro Education / Windows 10 Pro for Workstations / Windows 10 S / Windows 11 / Windows 11 Home / Windows 11 Home in S mode / Windows 11 IoT Enterprise / Windows 11 Pro / Windows 11 Pro Academic / Windows 11 Pro Education / Windows 11 Pro for Workstations / Windows 7 / Windows 7 Embedded / Windows 7 Home Basic / Windows 7 Home Premium / Windows 7 Pro / Windows 7 Professional / Windows 7 Professional 64 (available through downgrade rights from Windows 8.1 Pro) / Windows 7 Professional 64 (disponibile tramite diritti di downgrade da Windows 8 Pro 64) / Windows 7 Professional 64 (disponibile tramite diritti di downgrade da Windows 8.1 Pro 64) / Windows 7 Professional 64 (disponibile tramite diritti di downgrade da Windows 8.1 Pro) / Windows 7 Professional Preload / Windows 7 Starter / Windows 8 / Windows 8 Pro / Windows 8.1 / Windows 8.1 64 / Windows 8.1 con Bing 64 / Windows 8.1 Pro / Windows 8.1 Pro 32 / Windows 8.1 Pro 64 / Windows CE / Windows CE 6.0 / Windows Embedded POSReady 7 / Windows Embedded Standard 7 / Windows MultiPoint Server 2010 / Windows MultiPoint Server 2011 / Windows Phone / Windows POSReady 2009 / Windows RT / Windows Server 2012 / Windows Vista Business 
        
        Cerca di dedurre qual'è il valore più adatto per un dispositivo elettronico che ha queste descrizioni:
        {product_descriptions}
        
        Rispondi soltanto con il valore scelto senza aggiungere nessun'altra parola.\
        """).format(
            product_descriptions="\n".join(f"- {desc}" for desc in self.descriptions)
        )
