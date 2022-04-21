from collections import deque
import time
from DataHandler import DataHandler
from GoalCalculator import GoalCalculator
from neighbourings import *


class TabooSearch:
    """
    Klasa, w której będzie zawarty cały kod taboo searcha.
    Istnieją tutaj metody "search", które faktycznie szukają rozwiązania.
    Cała reszta metod powinna być wspomagająca do taboo searcha.
    Każdy search powinien zwracać funkcje celu ścieżki wyliczaną przez DataHandler
    Natomiast tuż przed zwróceniem powinno się odpalić "update",
    by uzupelnic znalezione rozwiazanie "last solution"
    """

    def __init__(self, dataHandler: DataHandler):
        self.last_solution: np.array
        self.last_cost: int

        self.data = dataHandler
        self.last_solution = None
        self.last_cost = None
        self.path_taken = list()

    def __update(self, last_solution: np.array, last_cost: int):
        self.last_solution = last_solution
        self.last_cost = last_cost

    def __basic_search(self, neighboring_function, starting_solution: np.array, TABOO_LIST_SIZE=20, TIME=30):
        # PREPARATIONS
        time_start = time.time()
        best_solution = starting_solution
        best_cost = self.data.cost(starting_solution)
        solution = best_solution.copy()
        taboo_list = deque([], TABOO_LIST_SIZE)  # <- struktura listy tabu - Kolejka?
        taboo_list.append(solution)
        # END PREPARATIONS

        while time.time() - time_start < TIME:  # <- Warunek stopu = czas
            neighboring_best_solution = np.array([])
            neighboring_best_cost = np.inf

            for i, j in possible_i_j(solution):
                neighboring_solution = neighboring_function(solution, i, j)
                if not any([x.all() for x in
                            neighboring_solution == taboo_list]):  # If neighboring solution is not in taboo list
                    neighboring_cost = self.data.cost(neighboring_solution)
                    if neighboring_cost < neighboring_best_cost:
                        neighboring_best_solution = neighboring_solution
                        neighboring_best_cost = neighboring_cost

            solution = neighboring_best_solution
            cost = neighboring_best_cost
            taboo_list.append(solution)

            if cost < best_cost:
                best_cost = cost
                best_solution = solution

        self.__update(best_solution, best_cost)
        return best_cost

    def search(self, TABOO_SEARCH_TYPE, neighboring_function, starting_solution, TABOO_LIST_SIZE=20, TIME=30):
        TABOO_SEARCH_TYPES = ["basic", "accelerate"]
        if TABOO_SEARCH_TYPE not in TABOO_SEARCH_TYPES:
            raise Exception(f"TABOO_SEARCH_TYPE ({TABOO_SEARCH_TYPE}) should be in {TABOO_SEARCH_TYPES}")

        if TABOO_SEARCH_TYPE == "basic":
            return self.__basic_search(neighboring_function=neighboring_function, starting_solution=starting_solution,
                                       TABOO_LIST_SIZE=TABOO_LIST_SIZE, TIME=TIME)
        elif TABOO_SEARCH_TYPE == "accelerate":
            return self.__20_04_accelerated_search(neighboring_function=neighboring_function,
                                                   starting_solution=starting_solution,
                                                   TABOO_LIST_SIZE=TABOO_LIST_SIZE, TIME=TIME)

    def __20_04_accelerated_search(self, neighboring_function, starting_solution: np.array, TABOO_LIST_SIZE=20,
                                   TIME=30):
        time_start = time.time()
        goal = GoalCalculator(self.data)
        best_solution = starting_solution
        best_cost = goal.basic_goal(starting_solution)

        solution = best_solution.copy()
        goal.set_neighboring_function(neighboring_function)
        goal.set_main_solution(solution)
        taboo_list = deque([], TABOO_LIST_SIZE)  # <- struktura listy tabu - Kolejka?
        taboo_list.append(solution)

        while time.time() - time_start < TIME:  # <- Warunek stopu = czas
            neighboring_best_solution = np.array([])
            neighboring_best_cost = np.inf

            for i, j in possible_i_j(solution):
                neighboring_solution = neighboring_function(solution, i, j)
                if not any([x.all() for x in
                            neighboring_solution == taboo_list]):  # If neighboring solution is not in taboo list
                    neighboring_cost = goal(neighboring_solution, i, j)
                    if neighboring_cost < neighboring_best_cost:
                        neighboring_best_solution = neighboring_solution
                        neighboring_best_cost = neighboring_cost

            solution = neighboring_best_solution
            goal.set_main_solution(solution)
            cost = neighboring_best_cost
            taboo_list.append(solution)

            if cost < best_cost:
                best_cost = cost
                best_solution = solution

        self.__update(best_solution, best_cost)
        return best_cost

    pass
