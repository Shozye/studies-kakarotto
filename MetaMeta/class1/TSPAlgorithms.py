from DataHandler import DataHandler
from utils import *
import random
from two_opt_neighbourings import *


class TSPAlgorithms:
    def __init__(self, filename: str):
        self.data = DataHandler(filename)

    def k_random(self, k: int):
        weights = []
        dimension = self.data.get_dimension()
        for _ in range(k):
            permutation = get_random_solution(dimension)
            weights.append([permutation, self.data.calculate_goal(permutation)])
        return min(weights, key=lambda x: x[1])

    def closest_neighbour(self, start=None):
        dimension = self.data.get_dimension()
        not_visited = list(range(1, dimension + 1))
        start_index = random.randint(0, dimension) if start is None else start
        position = not_visited[start_index]
        visited = [position]
        not_visited.remove(position)

        summarize_goal_function = 0
        while len(not_visited) != 0:
            calculated = self.data.get_closest_neighbour(position, not_visited)
            position = calculated[0]
            visited.append(position)
            summarize_goal_function += calculated[1]
            not_visited.remove(position)
        summarize_goal_function += self.data.getWeight(visited[-1], visited[0])
        return [visited, summarize_goal_function]

    def closest_neighbour_extended(self):
        starting_positions = list(range(1, self.data.get_dimension()))
        answers = list(map(lambda start_pos: [start_pos, self.closest_neighbour(start_pos)], starting_positions))
        return min(answers, key=lambda x: x[1][1])

    def two_opt(self, surrounding_function=None):
        if surrounding_function is None:
            surrounding_function = invert
        solution = get_random_solution(self.data.get_dimension())
        solution = [solution, self.data.calculate_goal(solution)]
        can_find_better_solution = True
        while can_find_better_solution:
            surrounding = surrounding_function(solution[0])
            surrounding = list(map(lambda x: [x, self.data.calculate_goal(x)], surrounding))
            new_solution = min(surrounding, key=lambda x: x[1])
            if new_solution[1] >= solution[1]:
                can_find_better_solution = False
            else:
                solution = new_solution
        return solution
