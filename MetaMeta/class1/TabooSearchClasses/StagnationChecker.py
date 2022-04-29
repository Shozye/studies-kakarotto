import numpy as np


class StagnationChecker:
    def __init__(self, STAGNATION_MAX_COUNTER=80):
        self.stagnated = False
        self.counter = 0
        self.best_solution = np.array([])
        self.best_solution: np.array
        self.STAGNATION_MAX = STAGNATION_MAX_COUNTER

    def reset(self):
        self.stagnated = False
        self.counter = 0
        self.best_solution = np.array([])

    def update(self, solution: np.array):
        if np.array_equal(self.best_solution, solution):
            self.counter += 1
            if self.counter >= self.STAGNATION_MAX:
                self.stagnated = True
        else:
            self.best_solution = solution
            self.counter = 0
