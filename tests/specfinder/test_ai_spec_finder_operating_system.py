from unittest import TestCase

from specfinder.ai_spec_finder import AISpecFinder


class TestAISpecFinder(TestCase):
    finder = AISpecFinder("Qwen3.6-35B-A3B-4bit")

    def test_find_os_easy_windows_11_pro(self):
        self.assertEqual("Windows 11 Pro", self.finder.find_os_for([
            'ASUS ExpertBook B3 Flip B3402FVA-EC0065X Intel® Core™ i7 i7-1355U Ibrido (2 in 1) 35,6 cm (14") Touch screen Full HD 8 GB DDR4-SDRAM 512 GB SSD Wi-Fi 6 (802.11ax) Windows 11 Pro Nero cod. 90NX07N1-M00230'
        ]))
        self.assertEqual("Windows 11 Pro", self.finder.find_os_for([
            'ASUS ExpertBook B3 Flip B3402FVA-EC0065X Intel® Core™ i7 i7-1355U Ibrido (2 in 1) 35,6 cm (14") Touch screen Full HD 8 GB DDR4-SDRAM 512 GB SSD Wi-Fi 6 (802.11ax) Windows 11 Pro Nero cod. 90NX07N1-M00230'
        ]))

    def test_find_os_short_windows_11_pro(self):
        self.assertEqual("Windows 11 Pro", self.finder.find_os_for([
            'Lenovo ThinkPad L13 2-in-1 Gen 6 21RD - Design ruotabile - AMD Ryzen 5 Pro - 215 / fino a 4.7 GHz - Win 11 Pro - Radeon 740M - 16 GB RAM - 512 GB SSD TCG Opal Encryption 2, NVMe - 13.3 IPS touchscreen 1920 x 1200 - Wi-Fi 7, Bluetooth - grigio'
        ]))

    def test_find_os_shorter_windows_11_pro_multiple_descriptions(self):
        self.assertEqual("Windows 11 Pro", self.finder.find_os_for([
            'Microsoft SrfcLp C+PcBN 13.8 U5/16/256 ITW11P Plat - EP2-47624',
            'SrfcLp C+PcBN 13.8 U5/16/256 ITW11P Plat - SrfcLp C+PcBN 13.8 U5/16/256 ITW11P Plat',
            'LPT8 13.8 CU5/16/256 PLAT - Microsoft SrLpt13.8Int8Ed CU5/16/256 CM SC Italian Platinum Italy 1 License',
            'LP8 13.8 CU5/16/256 PLAT - LP8 13.8IntCU5/16/256 CM Win11 Platinum',
        ]))

    def test_find_os_easy_chrome_os(self):
        self.assertEqual("ChromeOS", self.finder.find_os_for([
            'ASUS Chromebook CM1402CM2A-NK0147 MediaTek Kompanio 520 35,6 cm (14") Full HD 8 GB LPDDR4x-SDRAM 128 GB eMMC Wi-Fi 6 (802.11ax) ChromeOS Grigio cod. 90NX0631-M005L0'
        ]))

    def test_find_os_easy_freedos(self):
        self.assertEqual("FreeDOS", self.finder.find_os_for([
            'HP ProBook 4 G1iR Intel® Core™ i5 i5-1334U Computer portatile 35,6 cm (14") WUXGA 8 GB DDR5-SDRAM 512 GB SSD Wi-Fi 6E (802.11ax) FreeDOS Argento cod. B39WTAT'
        ]))
