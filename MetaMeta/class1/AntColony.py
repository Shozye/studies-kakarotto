from DataHandler import DataHandler
import numpy as np


class AntColony:
    def __init__(self, dataHandler: DataHandler):
        self.last_solution: np.array
        self.last_cost: int

        self.data = dataHandler

        for i, row in enumerate(self.data.edge_weights):
            for j, elem in enumerate(row):
                if elem == 0:
                    self.data.edge_weights[i][j] = np.inf

        self.last_solution = None
        self.last_cost = None

        self.amount_ants = None

    def __update(self, last_solution: np.array, last_cost: int):
        self.last_solution = last_solution
        self.last_cost = last_cost

    def search(self, ACO_SEARCH_TYPE="basic"):
        ACO_SEARCH_TYPES = ["basic"]
        if ACO_SEARCH_TYPE not in ACO_SEARCH_TYPES:
            raise Exception(f"ACO_SEARCH_TYPE ({ACO_SEARCH_TYPE}) should be in {ACO_SEARCH_TYPES}")

        if ACO_SEARCH_TYPE == "basic":
            return self.__basic_search()

    def __basic_search(self, n_ants=100, n_best=20, n_iterations=100, decay=0.95, alpha=1, beta=1):
        pheromone = np.ones(self.data.edge_weights.shape) / (self.data.dimension ** 2)
        all_ids = range(self.data.dimension)

        def spread_pheronome(_all_paths, _n_best):
            sorted_paths = sorted(_all_paths, key=lambda x: x[1])
            for path, dist in sorted_paths[:_n_best]:
                for move in path:
                    pheromone[move] += 1.0 / self.data.edge_weights[move]

        def gen_path_dist(path):
            total_dist = 0
            for ele in path:
                total_dist += self.data.edge_weights[ele]
            return total_dist

        def gen_all_paths():
            _all_paths = []
            for i in range(n_ants):
                path = gen_path(0)
                _all_paths.append((path, gen_path_dist(path)))
            return _all_paths

        def gen_path(start):
            path = []
            visited = set()
            visited.add(start)
            prev = start
            for _ in range(self.data.dimension-1):
                move = pick_move(pheromone[prev], self.data.edge_weights[prev], visited)
                path.append((prev, move))
                prev = move
                visited.add(move)
            path.append((prev, start))  # going back to where we started
            return path

        def pick_move(_pheromone, dist, visited):
            _pheromone = np.copy(_pheromone)
            _pheromone[list(visited)] = 0

            row = _pheromone ** alpha * ((1.0 / dist) ** beta)

            norm_row = row / row.sum()
            move = np.random.choice(all_ids, 1, p=norm_row)[0]
            return move

        all_time_shortest_path = ("placeholder", np.inf)
        for i in range(n_iterations):
            all_paths = gen_all_paths()
            spread_pheronome(all_paths, n_best)
            shortest_path = min(all_paths, key=lambda x: x[1])
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path
            pheromone = pheromone * decay
        self.__update(all_time_shortest_path[0], all_time_shortest_path[1])
        return all_time_shortest_path[1]
