import tsplib95.models

from DataHandler import DataHandler
import random
from two_opt_neighbourings import *
import numpy as np


def get_random_solution(max_incl: int) -> np.array:
    return np.random.permutation(max_incl)


class TSPAlgorithms:
    def __init__(self, edge_weights: np.array, dimension: int):
        self.edge_weights = edge_weights
        self.dimension = dimension

    def getWeight(self, node1: int, node2: int) -> int:
        return self.edge_weights[node1][node2]

    def goal(self, nodes: np.array) -> int:
        return sum(
            [self.getWeight(nodes[index], nodes[index + 1]) for index in range(len(nodes) - 1)]) + self.getWeight(
            nodes[-1], nodes[0])

    def k_random(self, k=1000):
        dimension = self.dimension
        best_solution = [[], np.inf]
        for _ in range(k):
            permutation = get_random_solution(dimension)
            weight = self.goal(permutation)
            if weight < best_solution[1]:
                best_solution = [permutation, weight]
        return best_solution

    def closest_neighbour(self, start=None):
        dimension = self.dimension
        not_visited = list(range(0, dimension))
        start_index = random.randint(0, dimension - 1) if start is None else start
        node_id = not_visited[start_index]
        tour = [node_id]
        not_visited.remove(node_id)

        summarize_goal_function = 0
        while len(not_visited) != 0:
            closest_node_id = 0
            closest_cost = np.inf
            for node_target in not_visited:
                node_cost = self.getWeight(node_id, node_target)
                if node_cost < closest_cost:
                    closest_cost = node_cost
                    closest_node_id = node_target
            node_id = closest_node_id
            tour.append(node_id)
            not_visited.remove(node_id)
            summarize_goal_function += closest_cost
        summarize_goal_function += self.getWeight(tour[-1], tour[0])
        return [tour, summarize_goal_function]

    def repetitive_closest_neighbour(self):
        best_tour = []
        best_goal = np.inf
        for i in range(self.dimension):
            tour, goal = self.closest_neighbour(i)
            if goal < best_goal:
                best_tour = tour
                best_goal = goal
        return [best_tour, best_goal]

    def two_opt_invert(self, starting_solution=np.array([])):
        best_solution = starting_solution if starting_solution != np.array([]) else get_random_solution(self.dimension)
        best_cost = self.goal(best_solution)

        can_find_better_solution = True
        while can_find_better_solution:
            left = 0
            right = 0
            cost = np.inf
            for temp_left in range(self.dimension):
                for temp_right in range(left + 1, self.dimension):
                    temp_cost = 0
                    indexes = list(range(self.dimension))
                    indexes = indexes[:temp_left] + indexes[temp_left:temp_right + 1][::-1] + indexes[temp_right + 1:]
                    for index in range(len(indexes) - 1):
                        temp_cost += self.getWeight(best_solution[indexes[index]], best_solution[indexes[index + 1]])
                    temp_cost += self.getWeight(best_solution[indexes[-1]], best_solution[indexes[0]])

                    if temp_cost < cost:
                        left = temp_left
                        right = temp_right
                        cost = temp_cost
            best_solution = list(best_solution)
            if cost < best_cost:
                best_solution = np.array(
                    best_solution[:left] + best_solution[left:right + 1][::-1] + best_solution[right + 1:])
                best_cost = cost
            else:
                can_find_better_solution = False
        return [best_solution, best_cost]

    def repetitive_two_opt(self, amount_of_repetitions: int):
        solution_now = [[], np.inf]
        for _ in range(amount_of_repetitions):
            solution = self.two_opt_invert()
            if solution[1] < solution_now[1]:
                solution_now = solution
        return solution_now

    def two_opt_with_repetitive_closest_neighbour(self):
        solution = self.repetitive_closest_neighbour()
        solution = self.two_opt_invert(solution[0])
        return solution

    def best(self):
        single_solutions = [self.two_opt_with_repetitive_closest_neighbour(),
                            self.k_random(100),
                            self.repetitive_two_opt(10)]
        best_solution = min(single_solutions, key=lambda x: x[1])
        return best_solution
