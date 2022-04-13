import numpy as np
from collections import deque
import time
from DataHandler import DataHandler


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
        self.data = dataHandler
        self.last_solution = None
        self.last_cost = None

    def __update(self, last_solution: np.array, last_cost: int):
        self.last_solution = last_solution
        self.last_cost = last_cost

    def __basic_search(self, neighboring_function, starting_solution: np.array):
        time_start = time.time()
        best_solution = starting_solution
        best_cost = self.data.cost(starting_solution)

        solution = best_solution.copy()
        taboo_list = deque([], 20) # <- struktura listy tabu - Kolejka?
        taboo_list.append(solution)
        while time.time() - time_start < 30: # <- Warunek stopu = czas
            neighboring_best_solution = np.array([])
            neighboring_best_cost = np.inf

            for neighboring_solution in neighboring_function(solution):
                if not any([x.all() for x in neighboring_solution == taboo_list]): # If neighboring solution is not in taboo list
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

    pass

    def search(self, neighboring_function, starting_solution):
        return self.__basic_search(neighboring_function=neighboring_function, starting_solution=starting_solution)
