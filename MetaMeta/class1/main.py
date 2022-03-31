from TSPAlgorithms import TSPAlgorithms
from DataHandler import DataHandler
import json
import tsplib95
import matplotlib.pyplot as plt
import networkx as nx
import two_opt_neighbourings
from FileGenerator import FileGenerator
from utils import *
import time


def main():
    generator = FileGenerator()
    generator.rm_dataset_directory()

    start=10
    end=50
    step = 3
    for i in range(start, end, step):
        generator.create_symmetric_dataset("GANGI", i)
    data_for_k_random_100 = []
    data_for_2_opt = []
    data_for_best = []
    data_for_repet_neighbour = []
    start_time = time.time()

    for i in range(start, end, step):
        algos = TSPAlgorithms(f"datasets/GANGI{i}/GANGI{i}.tsp")
        data_for_k_random_100.append(algos.k_random(10000)[1])
        data_for_2_opt.append(algos.two_opt()[1])
        data_for_best.append(algos.best()[1])
        data_for_repet_neighbour.append(algos.repetitive_closest_neighbour()[1])
    print(f"Zajelo {time.time() - start_time}")

    Xs = range(start,end, step)
    plt.plot(Xs, data_for_k_random_100, color='red', label='k_random_10000')
    plt.plot(Xs, data_for_2_opt, color='yellow', label='two_opt')
    plt.plot(Xs, data_for_best, color='green', label='best')
    plt.plot(Xs, data_for_repet_neighbour, color='black', label='repetitive')
    plt.xlabel('n')
    plt.ylabel('found_solution')
    plt.legend()
    plt.tight_layout()

    plt.show()


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
