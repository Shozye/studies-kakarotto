import tsplib95.models

import random
from neighbourings import *
import numpy as np


def get_random_solution(max_incl: int) -> np.array:
    return np.random.permutation(max_incl)


class TSPAlgorithms:
    def __init__(self, edge_weights: np.array, dimension: int):
        self.edge_weights = edge_weights
        self.dimension = dimension
        self.last_solution = np.array(np.random.permutation(self.dimension))
        self.last_cost = self.goal(self.last_solution)

    def getWeight(self, node1: int, node2: int) -> int:
        return self.edge_weights[node1][node2]

    def goal(self, nodes: np.array) -> int:
        return sum(
            [self.getWeight(nodes[index], nodes[index + 1]) for index in range(len(nodes) - 1)]) + self.getWeight(
            nodes[-1], nodes[0])

    def update(self, last_solution: np.array, last_cost: int):
        self.last_solution = last_solution
        self.last_cost = last_cost

    def k_random(self, k=1000):
        best_solution = np.random.permutation(self.dimension)
        best_cost = self.goal(best_solution)
        solution = best_solution.copy()
        for _ in range(k):
            np.random.shuffle(solution)
            cost = self.goal(solution)
            if cost < best_cost:
                best_solution = solution
                best_cost = cost
        self.update(best_solution, best_cost)
        return best_cost

    def closest_neighbour(self, start=None):
        dimension = self.dimension
        visited = [False] * self.dimension
        node_id = random.randint(0, dimension - 1) if start is None else start
        tour = [node_id]
        visited[node_id] = True

        summarize_goal_function = 0
        while not all(visited):
            closest_node_id = 0
            closest_cost = np.inf
            for node_target in range(0, self.dimension):
                if not visited[node_target]:
                    node_cost = self.getWeight(node_id, node_target)
                    if node_cost < closest_cost:
                        closest_cost = node_cost
                        closest_node_id = node_target

            node_id = closest_node_id
            tour.append(node_id)
            visited[node_id] = True
            summarize_goal_function += closest_cost
        summarize_goal_function += self.getWeight(tour[-1], tour[0])
        self.update(tour, summarize_goal_function)
        return summarize_goal_function

    def repetitive_closest_neighbour(self):
        best_cost = np.inf
        best_solution = np.array([])
        for i in range(self.dimension):
            cost = self.closest_neighbour(i)
            if cost < best_cost:
                best_cost = cost
                best_solution = self.last_solution
        self.update(best_solution, best_cost)
        return best_cost

    def two_opt(self, neighboring_function=invert, starting_solution=np.array([])):
        best_solution = starting_solution if starting_solution != np.array([]) else np.random.permutation(
            self.dimension)
        best_cost = self.goal(best_solution)
        can_find_better_solution = True
        while can_find_better_solution:
            cost = best_cost
            solution = best_solution.copy()
            for neighbour_solution in neighboring_function(best_solution):
                neighbour_cost = self.goal(neighbour_solution)

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
