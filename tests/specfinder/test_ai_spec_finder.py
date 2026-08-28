from unittest import TestCase, skip

from specfinder.ai_spec_finder import AISpecFinder
from specfinder.spec_finder import Spec


class TestAISpecFinder(TestCase):
    finder = AISpecFinder("Qwen3.6-35B-A3B-4bit")

    def test_find_spec_easy(self):
        actual = self.finder.find_for([
            'ASUS ExpertBook B3 Flip B3402FVA-EC0065X Intel® Core™ i7 i7-1355U Ibrido (2 in 1) 35,6 cm (14") ' +
            'Touch screen Full HD 8 GB DDR4-SDRAM 512 GB SSD Wi-Fi 6 (802.11ax) Windows 11 Pro Nero cod. 90NX07N1-M00230'
        ])
        expected = Spec(
            hdd_size="512 GB",
            hdd_type="SSD",
            display_size='35,6 cm (14")',
            processor_type='Intel® Core™ i7 i7-13xxU',
            ram_size="8 GB",
            operating_system="Windows 11 Pro"
        )
        self.assertEqual(expected, actual)

    @skip
    def test_find_spec_hard(self):
        actual = self.finder.find_for([
            'Microsoft SrfcLp C+PcBN 13.8 U5/16/256 ITW11P Plat - EP2-47624',
            'SrfcLp C+PcBN 13.8 U5/16/256 ITW11P Plat - SrfcLp C+PcBN 13.8 U5/16/256 ITW11P Plat',
            'LPT8 13.8 CU5/16/256 PLAT - Microsoft SrLpt13.8Int8Ed CU5/16/256 CM SC Italian Platinum Italy 1 License',
            'LP8 13.8 CU5/16/256 PLAT - LP8 13.8IntCU5/16/256 CM Win11 Platinum',
        ])
        expected = Spec(
            hdd_size="256 GB",
            hdd_type="SSD",
            display_size='35 cm (13.8")',
            processor_type='Intel Core Ultra 5',
            ram_size="16 GB",
            operating_system="Windows 11 Pro"
        )
        self.assertEqual(expected, actual)
