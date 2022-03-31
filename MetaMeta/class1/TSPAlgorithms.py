import tsplib95.models


from DataHandler import DataHandler
import random
from two_opt_neighbourings import *
import numpy as np


def get_random_solution(max_incl: int) -> list:
    return list(np.random.permutation(max_incl))

class TSPAlgorithms:
    def __init__(self, problem_init):
        if type(problem_init) in [str, tsplib95.models.StandardProblem]:
            self.data = DataHandler(problem_init)
        else:
            raise Exception("Not str or StandardProblem")

    def k_random(self, k: int):
        dimension = self.data.dimension()
        best_solution = [[], np.inf]
        for _ in range(k):
            permutation = get_random_solution(dimension)
            weight = self.data.goal(permutation)
            if weight < best_solution[1]:
                best_solution = [permutation, weight]
        return best_solution

    def closest_neighbour(self, start=None):
        dimension = self.data.dimension()
        not_visited = list(range(0, dimension))
        start_index = random.randint(0, dimension - 1) if start is None else start
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

    def two_opt(self, solution=None, surrounding_function=invert):
        if solution is None:
            solution = get_random_solution(self.data.dimension())
        solution = [solution, self.data.goal(solution)]
        can_find_better_solution = True
        while can_find_better_solution:
            new_solution = np.array(solution[0].copy())
            for possible_solution in surrounding_function(new_solution):
                possible_cost = self.data.goal(possible_solution)
                if possible_cost < new_solution[1]:
                    new_solution = [possible_solution, possible_cost]
            if new_solution[1] >= solution[1]:
                can_find_better_solution = False
            else:
                solution = new_solution
        return solution

    def repetitive_two_opt(self, amount_of_repetitions: int, surrounding_function=None):
        solution_now = [[], np.inf]
        for _ in range(amount_of_repetitions):
            solution = self.two_opt(surrounding_function)
            if solution[1] < solution_now[1]:
                solution_now = solution
        return solution_now

    def two_opt_with_repetitive_closest_neighbour(self, surrounding_function=None):
        solution = self.repetitive_closest_neighbour()
        solution = self.two_opt(solution[0], surrounding_function)
        return solution

    def best(self):
        single_solutions = [self.two_opt_with_repetitive_closest_neighbour(invert),
                            self.two_opt_with_repetitive_closest_neighbour(swap),
                            self.k_random(100),
                            self.repetitive_two_opt(3)]
        best_solution = min(single_solutions, key=lambda x: x[1])
        return best_solution
