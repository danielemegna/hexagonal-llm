from unittest import TestCase

from specfinder.ai_spec_finder import AISpecFinder


class TestAISpecFinder(TestCase):

    def test_find_os_for(self):
        finder = AISpecFinder()
        actual = finder.find_os_for(['ASUS ExpertBook B3 Flip B3402FVA-EC0065X Intel® Core™ i7 i7-1355U Ibrido (2 in 1) 35,6 cm (14") Touch screen Full HD 8 GB DDR4-SDRAM 512 GB SSD Wi-Fi 6 (802.11ax) Windows 11 Pro Nero cod. 90NX07N1-M00230'])
        self.assertEqual("Windows 11 Pro", actual)
