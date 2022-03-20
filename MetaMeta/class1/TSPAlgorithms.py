from DataHandler import DataHandler
from utils import *
import random


class TSPAlgorithms:
    def __init__(self, filename: str):
        self.data = DataHandler(filename)

    def k_random(self, k: int):
        weights = []
        dimension = self.data.get_dimensions()
        for _ in range(k):
            permutation = get_random_permutation(dimension)
            weights.append([permutation, self.data.calculate_goal(permutation)])
        return min(weights, key=lambda x: x[1])

    def closest_neighbour(self, start=None):
        dimension = self.data.get_dimensions()
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

    def super_closest_neighbour(self):
        starting_positions = list(range(1, self.data.get_dimensions()))
        answers = list(map(lambda start_pos: [start_pos, self.closest_neighbour(start_pos)], starting_positions))
        return min(answers, key=lambda x: x[1][1])
