from DataHandler import DataHandler
from utils import *
import random
from two_opt_neighbourings import *


class TSPAlgorithms:
    def __init__(self, filename: str):
        self.data = DataHandler(filename)

    def k_random(self, k: int):
        dimension = self.data.dimension()
        best_solution = [[], 99999999]
        for _ in range(k):
            permutation = get_random_solution(dimension)
            weight = self.data.goal(permutation)
            if weight < best_solution[1]:
                best_solution = [permutation, weight]
        return best_solution

    def closest_neighbour(self, start=None):
        dimension = self.data.dimension()
        not_visited = list(range(0, dimension))
        start_index = random.randint(0, dimension-1) if start is None else start
        node_id = not_visited[start_index]
        visited = [node_id]
        not_visited.remove(node_id)

        summarize_goal_function = 0
        while len(not_visited) != 0:
            closest = self.data.get_closest_neighbour(node_id, not_visited)
            node_id = closest[0]
            visited.append(node_id)
            summarize_goal_function += closest[1]
            not_visited.remove(node_id)

        summarize_goal_function += self.data.getWeight(visited[-1], visited[0])
        return [visited, summarize_goal_function]

    def repetitive_closest_neighbour(self):
        starting_node_ids = list(range(0, self.data.dimension()))
        answers = list(map(lambda start_pos: [start_pos] + self.closest_neighbour(start_pos), starting_node_ids))
        return min(answers, key=lambda x: x[2])[1:]

    def two_opt(self, surrounding_function=None):
        if surrounding_function is None:
            surrounding_function = invert
        solution = get_random_solution(self.data.dimension())
        solution = [solution, self.data.goal(solution)]
        can_find_better_solution = True
        while can_find_better_solution:
            surrounding = surrounding_function(solution[0])
            surrounding = list(map(lambda x: [x, self.data.goal(x)], surrounding))
            new_solution = min(surrounding, key=lambda x: x[1])
            if new_solution[1] >= solution[1]:
                can_find_better_solution = False
            else:
                solution = new_solution
        return solution
