from specfinder.spec_finder import SpecFinder, Spec


class AISpecFinder(SpecFinder):

    def find_os_for(self, descriptions: list[str]) -> str:
        return "Windows 11 Pro"

    def find_for(self, descriptions: list[str]) -> Spec:
        pass
