import numpy as np


class TabooList:
    def __init__(self, BASE_TENURE):
        self.BASE_TENURE = BASE_TENURE
        self.taboo = dict()

    def get(self):
        keys = list(self.taboo.keys())
        return [np.array(key) for key in keys]

    def update_tenures(self):
        to_del = []
        for key, value in self.taboo.items():
            if value < 0:
                to_del.append(key)
            else:
                self.taboo[key] -= 1
        for key_to_del in to_del:
            del self.taboo[key_to_del]

    def update(self, solution: np.array):
        self.update_tenures()
        self.taboo[tuple(solution)] = self.BASE_TENURE

    def update_group(self, solutions: list):
        self.update_tenures()
        for solution in solutions:
            self.taboo[tuple(solution)] = self.BASE_TENURE

    def reset(self):
        self.taboo = dict()
