from TSPAlgorithms import TSPAlgorithms
from DataHandler import DataHandler
import json
import tsplib95
import matplotlib.pyplot as plt
import networkx as nx
import two_opt_neighbourings
from FileGenerator import FileGenerator
from utils import *


def main():
    filename = f"tsplib_problems/bays29/bays29.tsp"
    algos = TSPAlgorithms(filename)
    for i in range(20):
        print(algos.two_opt(invert))


def test_hardcoded_solutions(solution: list, filename: str):
    data = DataHandler(filename)
    print(f"Weight of {json.dumps(solution)} is {data.goal(solution)}")


def analyze_file(filepath: str, verbose=False):
    K_RANDOM_AMOUNT = 10000
    NEIGHBOURING_ALGORITHM = two_opt_neighbourings.invert
    # Running algorithms
    algos = TSPAlgorithms(filepath)
    k_random = algos.k_random(K_RANDOM_AMOUNT)
    closest_neighbour = algos.closest_neighbour(0)
    repetitive_closest_neighbour = algos.repetitive_closest_neighbour()
    two_opt = algos.two_opt()
    # Printing out results of algorithms
    print(f"k_random({K_RANDOM_AMOUNT}): {k_random[1]}")
    if verbose:
        print(f"Found: {k_random[0]}")
    print(f"closest_neighbour(): {closest_neighbour}")
    if verbose:
        print(f"Found: {closest_neighbour[0]}")
    print(f"repetitive_closest_neighbour(): {repetitive_closest_neighbour}")
    if verbose:
        print(f"Found: {repetitive_closest_neighbour[0]}")
    print(f"two_opt({NEIGHBOURING_ALGORITHM.__name__}): {two_opt[1]}")
    if verbose:
        print(f"Found: {two_opt[0]}")


def draw_graph(filename: str):
    with open(filename) as file:
        graph = tsplib95.read(file).get_graph()
        nx.draw_shell(graph)
    plt.show()


if __name__ == "__main__":
    main()
