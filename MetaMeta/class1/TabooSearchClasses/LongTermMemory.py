import numpy as np
import collections


class LongTermMemory:
    def __init__(self, FUTURE_TABOO_TO_REMEMBER_LENGTH=100, TABOO_LENGTH=20):
        self.FUTURE_TABOO_TO_REMEMBER_LENGTH = FUTURE_TABOO_TO_REMEMBER_LENGTH
        self.solutions = list()
        self.solutions_duration = list()
        self.solutions_taboo_list = list()
        self.last_solutions = collections.deque([], TABOO_LENGTH)
        self.empty_flag = False

    def update_solutions(self, solution: np.array):
        self.last_solutions.append(solution)
        for i in range(len(self.solutions)):
            if self.solutions_duration[i] > 0:
                self.solutions_taboo_list[i].append(solution)
            self.solutions_duration[i] -= 1

    def update_new_best_solution(self, solution: np.array):
        self.update_solutions(solution)
        self.solutions.append(solution)
        self.solutions_duration.append(self.FUTURE_TABOO_TO_REMEMBER_LENGTH)
        self.solutions_taboo_list.append(list(self.last_solutions))

    def take_last_solution(self):
        if len(self.solutions) != 0:
            last_solution = self.solutions[-1]
            last_taboo_list = self.solutions_taboo_list[-1]
            del self.solutions[-1]
            del self.solutions_taboo_list[-1]
            del self.solutions_duration[-1]
            return [last_solution, last_taboo_list]
        else:
            self.empty_flag = True
            return [None, None]