from collections import defaultdict


class Labels:
    """Class used to provide user with unique labels for Three Address Code"""

    def __init__(self):
        self.counts = defaultdict(int)

    def _get(self, name: str = ""):
        self.counts[name] += 1
        return f"E_{name.upper()}{self.counts[name] - 1}"

    def get(self):
        return self._get()
