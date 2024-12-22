import numpy as np


class StagnationChecker:
    def __init__(self, STAGNATION_MAX_COUNTER=40):
        self.stagnated = False
        self.counter = 0
        self.best_cost = np.inf
        self.best_cost : float
        self.STAGNATION_MAX = STAGNATION_MAX_COUNTER

    def reset(self):
        self.stagnated = False
        self.counter = 0
        self.best_cost = np.inf

    def update(self, cost: float):
        if np.array_equal(self.best_cost, cost):
            self.counter += 1
            if self.counter >= self.STAGNATION_MAX:
                self.stagnated = True
        else:
            self.best_cost = cost
            self.counter = 0
