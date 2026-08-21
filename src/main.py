from pprint import pprint

from specfinder.ai_spec_finder import AISpecFinder


def main() -> None:
    print("============= AI Food Facts =============")

    print("Finding Specs...")
    spec_finder = AISpecFinder()
    spec = spec_finder.find_for([
        'ASUS ExpertBook B3 Flip B3402FVA-EC0065X Intel® Core™ i7 i7-1355U Ibrido (2 in 1) 35,6 cm (14") Touch screen Full HD 8 GB DDR4-SDRAM 512 GB SSD Wi-Fi 6 (802.11ax) Windows 11 Pro Nero cod. 90NX07N1-M00230'
    ])

    pprint(spec)

    print("================= Done ==================")


if __name__ == "__main__":
    main()
