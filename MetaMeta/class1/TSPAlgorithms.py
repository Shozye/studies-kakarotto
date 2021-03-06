import random

from TabooSearch import TabooSearch
from neighbourings import *
import numpy as np
from DataHandler import DataHandler
import json
import logging
import AntColonyButDifferent
import AntColony
from utils import dist, calculate_goal
import tsplib95
from typing import Union

class TSPAlgorithms:
    """
    Klasa, która przez którą zyskujemy dostęp do każdego algorytmu.
    Wszystkie algorytmy powinny update'owac last_solution i last_cost
    W przypadku taboo searcha odwolujemy sie do klasy TabooSearch i uzywamy jej searcha
    Metoda taboo_search w takim razie jest tylko "wrapperem" na TabooSearch.search
    """
    data: DataHandler

    def __init__(self, dataHandler: Union[DataHandler, tsplib95.models.StandardProblem]):
        self.data = dataHandler
        self.last_solution = None
        self.last_cost = None
        self.time_running = 0

    def update(self, last_solution, last_cost):
        self.last_solution = last_solution
        self.last_cost = last_cost

    def taboo_search(self, TABOO_SEARCH_TYPE: str, neighboring_function=invert, starting_solution=np.array([]),
                     TABOO_LIST_SIZE=10, TIME=30):
        starting_solution = starting_solution if starting_solution != np.array([]) else np.random.permutation(
            self.data.dimension)
        taboo = TabooSearch(self.data)
        cost = taboo.search(TABOO_SEARCH_TYPE=TABOO_SEARCH_TYPE, neighboring_function=neighboring_function,
                            starting_solution=starting_solution, TABOO_LIST_SIZE=TABOO_LIST_SIZE, TIME=TIME)
        self.update(taboo.last_solution, cost)
        return cost

    def ant_colony(self, ant_colony_type="normal", **kwargs):
        node_coords = dict()
        for key in (self.data.node_coords.keys()):
            node_coords[str(key)] = tuple(self.data.node_coords[key])
        cities = list(sorted(node_coords.items()))
        if ant_colony_type == "normal":
            found_path = AntColony.AntColonyRunner(cities, verbose=False, **kwargs)
        else:
            found_path = AntColonyButDifferent.AntColonyRunner(cities, verbose=False, **kwargs)
        cost = calculate_goal(found_path)

        self.update([node[0] for node in found_path], cost)
        return cost

    def k_random(self, k=1000):
        best_solution = np.random.permutation(self.data.dimension)
        best_cost = self.data.cost(best_solution)
        solution = best_solution.copy()
        for _ in range(k):
            np.random.shuffle(solution)
            cost = self.data.cost(solution)
            if cost < best_cost:
                best_solution = solution
                best_cost = cost
        self.update(best_solution, best_cost)
        return best_cost

    def closest_neighbour(self, start=None):
        dimension = self.data.dimension
        visited = [False] * self.data.dimension
        node_id = random.randint(0, dimension - 1) if start is None else start
        tour = [node_id]
        visited[node_id] = True

        summarize_goal_function = 0
        while not all(visited):
            closest_node_id = 0
            closest_cost = np.inf
            for node_target in range(0, self.data.dimension):
                if not visited[node_target]:
                    node_cost = self.data.getCost(node_id, node_target)
                    if node_cost < closest_cost:
                        closest_cost = node_cost
                        closest_node_id = node_target

            node_id = closest_node_id
            tour.append(node_id)
            visited[node_id] = True
            summarize_goal_function += closest_cost
        summarize_goal_function += self.data.getCost(tour[-1], tour[0])
        self.update(np.array(tour, dtype=np.int), summarize_goal_function)
        return summarize_goal_function

    def repetitive_closest_neighbour(self):
        best_cost = np.inf
        best_solution = np.array([])
        for i in range(self.data.dimension):
            cost = self.closest_neighbour(i)
            if cost < best_cost:
                best_cost = cost
                best_solution = self.last_solution
        self.update(best_solution, best_cost)
        return best_cost

    def two_opt(self, neighboring_function=invert, starting_solution=np.array([])):
        logger = logging.getLogger("two_opt")
        best_solution = starting_solution if starting_solution != np.array([]) else np.random.permutation(
            self.data.dimension)
        best_cost = self.data.cost(best_solution)
        can_find_better_solution = True
        while can_find_better_solution:
            cost = best_cost
            solution = best_solution.copy()
            logger.debug(f"{str(cost)} {json.dumps([int(x) for x in solution])}")
            for i, j in possible_i_j(best_solution):
                neighbour_solution = neighboring_function(best_solution, i, j)
                neighbour_cost = self.data.cost(neighbour_solution)

                if neighbour_cost < cost:
                    cost = neighbour_cost
                    solution = neighbour_solution
            if cost < best_cost:
                best_solution = solution
                best_cost = cost
            else:
                can_find_better_solution = False
        self.update(best_solution, best_cost)
        return best_cost

    def repetitive_two_opt(self, amount_of_repetitions: int, neighbouring_function=invert):
        best_solution = np.array([])
        best_cost = np.inf
        for _ in range(amount_of_repetitions):
            cost = self.two_opt(neighboring_function=neighbouring_function)
            if cost < best_cost:
                best_cost = cost
                best_solution = self.last_solution
        self.update(best_solution, best_cost)
        return best_cost

    def two_opt_with_repetitive_closest_neighbour(self, neighbouring_function=invert):
        self.repetitive_closest_neighbour()
        return self.two_opt(neighboring_function=neighbouring_function, starting_solution=self.last_solution)

    def best(self):
        costs = [self.two_opt_with_repetitive_closest_neighbour(invert),
                 self.two_opt_with_repetitive_closest_neighbour(swap),
                 self.two_opt(invert),
                 self.two_opt(swap),
                 self.k_random(100)]
        return min(costs)
