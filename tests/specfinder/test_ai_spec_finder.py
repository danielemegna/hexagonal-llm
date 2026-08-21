from unittest import TestCase

from specfinder.ai_spec_finder import AISpecFinder
from specfinder.spec_finder import Spec


class TestAISpecFinder(TestCase):

    def test_find_spec_easy(self):
        finder = AISpecFinder()
        actual = finder.find_for(['ASUS ExpertBook B3 Flip B3402FVA-EC0065X Intel® Core™ i7 i7-1355U Ibrido (2 in 1) 35,6 cm (14") Touch screen Full HD 8 GB DDR4-SDRAM 512 GB SSD Wi-Fi 6 (802.11ax) Windows 11 Pro Nero cod. 90NX07N1-M00230'])
        expected = Spec(
            hdd_size="512 GB",
            hdd_type="SSD",
            display_size='35,6 cm (14")',
            processor_type='Intel® Core™ i7',
            ram_size="8 GB",
            operating_system="Windows 11 Pro"
        )
        self.assertEqual(expected, actual)
