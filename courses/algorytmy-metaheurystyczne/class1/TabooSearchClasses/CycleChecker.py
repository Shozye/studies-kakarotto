import numpy as np


class CycleChecker:
    def __init__(self, AMOUNT_OF_REPETITIONS=4):
        self.__memory = dict()
        self.AMOUNT_OF_REPETITIONS = AMOUNT_OF_REPETITIONS
        self.cycled = False

    def update(self, solution: np.array):
        solution = tuple(solution)
        if self.__memory.get(solution) is not None:
            self.__memory[solution] += 1
            if self.__memory[solution] >= self.AMOUNT_OF_REPETITIONS:
                self.cycled = True
        else:
            self.__memory[solution] = 1

