from TSPAlgorithms import TSPAlgorithms
from DataHandler import DataHandler
import tsplib95
import matplotlib.pyplot as plt
import networkx as nx
import neighbourings
from FileGenerator import FileGenerator


def main():
    generator = FileGenerator()
    generator.rm_dataset_directory()

    generator.create_symmetric_dataset("GANGI", 10)
    data = DataHandler("datasets/GANGI10/GANGI10.tsp")

    analyze_file(data, verbose=True)


def analyze_file(data: DataHandler, verbose=False):
    K_RANDOM_AMOUNT = 10000
    algos = TSPAlgorithms(data.get_edge_weights(), data.dimension())
    print(f"k_random({K_RANDOM_AMOUNT}): {algos.k_random(K_RANDOM_AMOUNT)}")
    if verbose:
        print(f"Found: {algos.last_solution}")
    print(f"closest_neighbour(): {algos.closest_neighbour()}")
    if verbose:
        print(f"Found: {algos.last_solution}")
    print(f"repetitive_closest_neighbour(): {algos.repetitive_closest_neighbour()}")
    if verbose:
        print(f"Found: {algos.last_solution}")
    print(f"two_opt(invert): {algos.two_opt(neighbourings.invert)}")
    if verbose:
        print(f"Found: {algos.last_solution}")
    print(f"two_opt(swap): {algos.two_opt(neighbourings.swap)}")
    if verbose:
        print(f"Found: {algos.last_solution}")


def draw_graph(filename: str):
    with open(filename) as file:
        graph = tsplib95.read(file).get_graph()
        nx.draw_shell(graph)
    plt.show()


if __name__ == "__main__":
    main()
