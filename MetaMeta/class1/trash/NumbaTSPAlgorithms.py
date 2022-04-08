import numpy as np
from numba.experimental import jitclass
from numba import types
from numba import int32
import numba
from MetaMeta.class1.neighbourings import invert, swap

spec = [
    ('edge_weights', types.Array),
    ('dimension', int32)
]


class NumbaTSPAlgorithms:
    def __init__(self, edge_weights: np.array, dimension: int):
        self.edge_weights = edge_weights
        self.dimension = dimension

    def get_closest_neighbour(self, node, neighbours):
        """ Function to get the closest neighbour from list of neighbours
        :param node: node of which we want closest neighbour
        :param neighbours: List of neighbours to take under consideration
        :return: list of node id and weight
        """
        lengths = list((map(lambda x: [x, self.getWeight(node, x)], neighbours)))
        return min(lengths, key=lambda x: x[1])

    def getWeight(self, node, x):
        return self.edge_weights[node][x]

    def goal(self, nodes: np.array):
        """Function that calculates goal function of certain list. It calculates list weight adding first element to end
        :param nodes: list of nodes
        :return: goal function
        """
        weight = 0
        for i in range(len(nodes) - 1):
            weight += self.getWeight(nodes[i], nodes[i + 1])
        return weight + self.getWeight(nodes[-1], nodes[0])

    def k_random(self, k: int):
        best_solution = [[], np.inf]
        random_solution = np.random.permutation(self.dimension)
        for _ in range(k):
            np.random.shuffle(random_solution)
            permutation = random_solution
            weight = self.goal(permutation)
            if weight < best_solution[1]:
                best_solution = [permutation, weight]
        return best_solution

    def closest_neighbour(self, start=-1):
        dimension = self.dimension
        not_visited = list(range(0, dimension))
        start_index = np.random.randint(0, dimension - 1) if start is -1 else start
        node_id = not_visited[start_index]
        visited = [node_id]
        not_visited.remove(node_id)

        summarize_goal_function = 0
        while len(not_visited) != 0:
            closest = self.get_closest_neighbour(node_id, not_visited)
            node_id = closest[0]
            visited.append(node_id)
            summarize_goal_function += closest[1]
            not_visited.remove(node_id)

        summarize_goal_function += self.getWeight(visited[-1], visited[0])
        return [visited, summarize_goal_function]

    def repetitive_closest_neighbour(self):
        starting_node_ids = list(range(0, self.dimension))
        answers = list(map(lambda start_pos: [start_pos] + self.closest_neighbour(start_pos), starting_node_ids))
        return min(answers, key=lambda x: x[2])[1:]

    def two_opt(self, solution=None, surrounding_function=invert):
        if solution is None:
            solution = np.random.permutation(self.dimension)
        solution = [solution, self.goal(solution)]
        can_find_better_solution = True
        while can_find_better_solution:
            new_solution = solution.copy()
            for possible_solution in surrounding_function(new_solution[0]):
                possible_cost = self.goal(possible_solution)
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
                            self.repetitive_two_opt(10)]
        best_solution = min(single_solutions, key=lambda x: x[1])
        return best_solution
