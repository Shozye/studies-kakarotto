import logging
from collections import deque
import time
from DataHandler import DataHandler
from TabooSearchClasses.GoalCalculator import GoalCalculator
from neighbourings import *
from TabooSearchClasses.CycleChecker import CycleChecker
from TabooSearchClasses.StagnationChecker import StagnationChecker
from TabooSearchClasses.LongTermMemory import LongTermMemory
import sys
from TabooSearchClasses.TabooList import TabooList
import json
import random


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
        logger = logging.getLogger("basic")
        time_start = time.time()
        best_solution = starting_solution
        best_cost = self.data.cost(starting_solution)
        solution = best_solution.copy()
        cost = best_cost
        taboo_list = deque([], TABOO_LIST_SIZE)  # <- struktura listy tabu - Kolejka?
        taboo_list.append(solution)
        # END PREPARATIONS

        while time.time() - time_start < TIME:  # <- Warunek stopu = czas
            neighboring_best_solution = np.array([])
            neighboring_best_cost = np.inf
            logger.debug(f"{str(cost)} {json.dumps([int(x) for x in solution])}")

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
        TABOO_SEARCH_TYPES = ["basic", "accelerate", "cycled_accelerate", "stagnation_accelerate", "long_term_memory", "accelerate_moves"]
        if TABOO_SEARCH_TYPE not in TABOO_SEARCH_TYPES:
            raise Exception(f"TABOO_SEARCH_TYPE ({TABOO_SEARCH_TYPE}) should be in {TABOO_SEARCH_TYPES}")

        if TABOO_SEARCH_TYPE == "basic":
            return self.__basic_search(neighboring_function=neighboring_function, starting_solution=starting_solution,
                                       TABOO_LIST_SIZE=TABOO_LIST_SIZE, TIME=TIME)
        elif TABOO_SEARCH_TYPE == "accelerate":
            return self.__20_04_accelerated_search(neighboring_function=neighboring_function,
                                                   starting_solution=starting_solution,
                                                   TABOO_LIST_SIZE=TABOO_LIST_SIZE, TIME=TIME)
        elif TABOO_SEARCH_TYPE == "cycled_accelerate":
            return self.__28_04_accelerated_search_cycle_finder(neighboring_function=neighboring_function,
                                                                starting_solution=starting_solution,
                                                                TABOO_LIST_SIZE=TABOO_LIST_SIZE, TIME=TIME)
        elif TABOO_SEARCH_TYPE == "stagnation_accelerate":
            return self.__28_04_accelerated_search_stagnation_finder(neighboring_function=neighboring_function,
                                                                     starting_solution=starting_solution,
                                                                     TABOO_LIST_SIZE=TABOO_LIST_SIZE, TIME=TIME)
        elif TABOO_SEARCH_TYPE == "long_term_memory":
            return self.__28_04_accelerated_search_long_term_memory(neighboring_function=neighboring_function,
                                                                    starting_solution=starting_solution,
                                                                    TABOO_LIST_SIZE=TABOO_LIST_SIZE, TIME=TIME)

        elif TABOO_SEARCH_TYPE == "accelerate_moves":
            return self.__05_04_accelerated_moves_diverse_search(neighboring_function=neighboring_function,
                                                                 starting_solution=starting_solution,
                                                                 TABOO_LIST_SIZE=TABOO_LIST_SIZE, TIME=TIME)

    def __20_04_accelerated_search(self, neighboring_function, starting_solution: np.array, TIME=15,
                                   TABOO_LIST_SIZE=20):
        logger = logging.getLogger("accelerate")
        time_start = time.time()
        goal = GoalCalculator(self.data)
        best_solution = starting_solution
        best_cost = goal.basic_goal(starting_solution)

        solution = best_solution.copy()
        cost = best_cost
        goal.set_neighboring_function(neighboring_function.__name__)
        goal.set_main_solution(solution)
        taboo_list = deque([], TABOO_LIST_SIZE)  # <- struktura listy tabu - Kolejka?
        taboo_list.append(solution)

        while time.time() - time_start < TIME:  # <- Warunek stopu = czas
            neighboring_best_solution = np.array([])
            neighboring_best_cost = np.inf
            logger.debug(f"{str(cost)} {json.dumps([int(x) for x in solution])}")
            for i, j in possible_i_j(solution):
                neighboring_solution = neighboring_function(solution, i, j)
                if not any([x.all() for x in
                            neighboring_solution == taboo_list]):  # If neighboring solution is not in taboo list
                    neighboring_cost = goal(neighboring_solution, i, j)
                    if neighboring_cost < neighboring_best_cost:
                        neighboring_best_solution = neighboring_solution
                        neighboring_best_cost = neighboring_cost

            # The solution has been chosen here. It is being changed to best if possible
            solution = neighboring_best_solution
            cost = neighboring_best_cost
            if cost < best_cost:
                best_cost = cost
                best_solution = solution

            # Here it is processed to memory and others
            goal.set_main_solution(solution)
            taboo_list.append(solution)

        self.__update(best_solution, best_cost)
        return best_cost

    def __05_04_accelerated_moves_diverse_search(self, neighboring_function, starting_solution: np.array, TIME=15,
                                                 TABOO_LIST_SIZE=20):
        logger = logging.getLogger("accelerate_moves")
        time_start = time.time()
        goal = GoalCalculator(self.data)
        best_solution = starting_solution
        best_cost = goal.basic_goal(starting_solution)

        solution = best_solution.copy()
        cost = best_cost
        goal.set_neighboring_function(neighboring_function.__name__)
        goal.set_main_solution(solution)
        taboo_list = deque([], TABOO_LIST_SIZE)  # <- struktura listy tabu - Kolejka?

        stagnation_checker = StagnationChecker()
        while not stagnation_checker.stagnated and time.time() - time_start < TIME:  # <- Warunek stopu = cykl lub czas, jeżeli nie zacykli
            neighboring_best_cost = np.inf
            neighboring_best_solutions = list()
            logger.debug(f"{str(cost)} {json.dumps([int(x) for x in solution])}")
            for i, j in possible_i_j(solution):
                neighboring_solution = neighboring_function(solution, i, j)
                if not (i, j) in taboo_list:  # If neighboring solution is not in taboo list
                    neighboring_cost = goal(neighboring_solution, i, j)
                    if neighboring_cost < neighboring_best_cost:
                        neighboring_best_solutions = [(neighboring_solution, i, j)]
                        neighboring_best_cost = neighboring_cost
                    elif neighboring_cost == neighboring_best_cost:
                        neighboring_best_solutions.append((neighboring_solution, i, j))

            # The solution has been chosen here. It is being changed to best if possible

            solution, used_i, used_j = random.choice(neighboring_best_solutions)
            cost = neighboring_best_cost
            if cost < best_cost:
                best_cost = cost
                best_solution = solution

            # Here it is processed to memory and others
            goal.set_main_solution(solution)
            taboo_list.append((used_i, used_j))
            stagnation_checker.update(best_cost)

        self.__update(best_solution, best_cost)
        return best_cost

    def __28_04_accelerated_search_cycle_finder(self, neighboring_function, starting_solution: np.array,
                                                TIME=30, TABOO_LIST_SIZE=20):
        logger = logging.getLogger("cycled")
        time_start = time.time()
        goal = GoalCalculator(self.data)
        best_solution = starting_solution
        best_cost = goal.basic_goal(starting_solution)

        solution = best_solution.copy()
        cost = best_cost
        goal.set_neighboring_function(neighboring_function.__name__)
        goal.set_main_solution(solution)
        taboo_list = deque([], TABOO_LIST_SIZE)  # <- struktura listy tabu - Kolejka?
        taboo_list.append(solution)

        cycle_checker = CycleChecker()
        while not cycle_checker.cycled and time.time() - time_start < TIME:  # <- Warunek stopu = cykl lub czas, jeżeli nie zacykli
            neighboring_best_solution = np.array([])
            neighboring_best_cost = np.inf
            logger.debug(f"{str(cost)} {json.dumps([int(x) for x in solution])}")
            for i, j in possible_i_j(solution):
                neighboring_solution = neighboring_function(solution, i, j)
                if not any([x.all() for x in
                            neighboring_solution == taboo_list]):  # If neighboring solution is not in taboo list
                    neighboring_cost = goal(neighboring_solution, i, j)
                    if neighboring_cost < neighboring_best_cost:
                        neighboring_best_solution = neighboring_solution
                        neighboring_best_cost = neighboring_cost

            # The solution has been chosen here. It is being changed to best if possible
            solution = neighboring_best_solution
            cost = neighboring_best_cost
            if cost < best_cost:
                best_cost = cost
                best_solution = solution

            # Here it is processed to memory and others
            goal.set_main_solution(solution)
            taboo_list.append(solution)
            cycle_checker.update(solution)

        self.__update(best_solution, best_cost)
        return best_cost

    def __28_04_accelerated_search_stagnation_finder(self, neighboring_function, starting_solution: np.array,
                                                     TIME=60, TABOO_LIST_SIZE=20):
        logger = logging.getLogger("stagnation")
        time_start = time.time()
        goal = GoalCalculator(self.data)
        best_solution = starting_solution
        best_cost = goal.basic_goal(starting_solution)

        solution = best_solution.copy()
        cost = best_cost
        goal.set_neighboring_function(neighboring_function.__name__)
        goal.set_main_solution(solution)
        taboo_list = deque([], TABOO_LIST_SIZE)  # <- struktura listy tabu - Kolejka?
        taboo_list.append(solution)

        stagnation_checker = StagnationChecker()
        while not stagnation_checker.stagnated and time.time() - time_start < TIME:  # <- Warunek stopu = cykl lub czas, jeżeli nie zacykli
            neighboring_best_solution = np.array([])
            neighboring_best_cost = np.inf
            logger.debug(f"{str(cost)} {json.dumps([int(x) for x in solution])}")

            for i, j in possible_i_j(solution):
                neighboring_solution = neighboring_function(solution, i, j)
                if not any([x.all() for x in
                            neighboring_solution == taboo_list]):  # If neighboring solution is not in taboo list
                    neighboring_cost = goal(neighboring_solution, i, j)
                    if neighboring_cost < neighboring_best_cost:
                        neighboring_best_solution = neighboring_solution
                        neighboring_best_cost = neighboring_cost

            # The solution has been chosen here. It is being changed to best if possible
            solution = neighboring_best_solution
            cost = neighboring_best_cost
            if cost < best_cost:
                best_cost = cost
                best_solution = solution

            # Here it is processed to memory and others
            goal.set_main_solution(solution)
            taboo_list.append(solution)
            stagnation_checker.update(best_cost)  # we update stagnation checker to check if best solution found

        self.__update(best_solution, best_cost)
        return best_cost

    def __28_04_accelerated_search_long_term_memory(self, neighboring_function, starting_solution: np.array,
                                                    TIME=30, TABOO_LIST_SIZE=20):
        logger = logging.getLogger("long_term_memory")
        time_start = time.time()
        goal = GoalCalculator(self.data)
        long_term_memory = LongTermMemory(FUTURE_TABOO_TO_REMEMBER_LENGTH=50, TABOO_LENGTH=TABOO_LIST_SIZE)
        best_solution = starting_solution
        best_cost = goal.basic_goal(starting_solution)
        long_term_memory.update_new_best_solution(best_solution)

        solution = best_solution.copy()
        cost = best_cost
        goal.set_neighboring_function(neighboring_function.__name__)
        goal.set_main_solution(solution)
        taboo_list = TabooList(TABOO_LIST_SIZE)
        taboo_list.update(solution)
        move_taboo_list = deque([], TABOO_LIST_SIZE)  # <- struktura listy tabu - Kolejka?

        stagnation_checker = StagnationChecker()
        while time.time() - time_start < TIME and not long_term_memory.empty_flag:  # <- Warunek stopu = czas
            neighboring_best_cost = np.inf
            logger.debug(f"{str(cost)} {json.dumps([int(x) for x in solution])}")
            neighboring_best_solutions = list()

            for i, j in possible_i_j(solution):
                neighboring_solution = neighboring_function(solution, i, j)
                if (i, j) not in move_taboo_list:  # If neighboring solution is not in taboo list
                    neighboring_cost = goal(neighboring_solution, i, j)
                    if neighboring_cost < neighboring_best_cost:
                        neighboring_best_solutions = [(neighboring_solution, i, j)]
                        neighboring_best_cost = neighboring_cost
                    elif neighboring_cost == neighboring_best_cost:
                        neighboring_best_solutions.append((neighboring_solution, i, j))

            # The solution has been chosen here. It is being changed to best if possible
            solution, used_i, used_j = random.choice(neighboring_best_solutions)
            cost = neighboring_best_cost
            if cost < best_cost:
                best_cost = cost
                best_solution = solution
                long_term_memory.update_new_best_solution(solution)
            else:
                long_term_memory.update_solutions(solution)

            # Here it is processed to memory and others
            goal.set_main_solution(solution)
            taboo_list.update(solution)
            move_taboo_list.append((used_i, used_j))
            stagnation_checker.update(best_cost)  # we update stagnation checker to update stagnation flag

            if stagnation_checker.stagnated:
                solution_from_memory, taboo_list_from_memory = long_term_memory.take_last_solution()
                if solution_from_memory is None:
                    continue
                stagnation_checker.reset()
                stagnation_checker.update(goal.basic_goal(solution))
                taboo_list.reset()
                taboo_list.update_group(taboo_list_from_memory)
                solution = solution_from_memory
                goal.set_main_solution(solution)

        self.__update(best_solution, best_cost)
        return best_cost
