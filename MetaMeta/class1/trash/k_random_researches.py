import time
import json
from matplotlib import pyplot as plt
import math
from MetaMeta.class1.DataHandler import DataHandler
from MetaMeta.class1.FileGenerator import FileGenerator
from MetaMeta.class1.TSPAlgorithms import TSPAlgorithms
import numpy as np
from matplotlib.pyplot import figure
from tqdm import tqdm
from numba import jit


@jit(nopython=True)
def k_random_for_research(dimension, edge_weights, k=1000):
    smallest_cost = np.inf
    for _ in range(k):
        permutation = np.random.permutation(dimension)
        cost = sum([edge_weights[permutation[index]][permutation[index + 1]] for index in
                    range(len(permutation) - 1)]) + edge_weights[permutation[-1]][permutation[0]]
        if cost < smallest_cost:
            smallest_cost = cost
    return smallest_cost


def generate_k_random_research_data(n=30):
    AMOUNT_OF_FILES_PER_N = 100
    generator = FileGenerator()
    start = 10 ** 2
    end = 10 ** 4 * 5 + 1
    step = 10 ** 2
    full_data = dict()
    N_to_do = [30, 90, 150, 210]
    for n in N_to_do:
        full_data[n] = dict()
        data = full_data[n]
        for _ in range(start, end, step):
            data[_] = 0

        for _ in tqdm(range(AMOUNT_OF_FILES_PER_N), f"Generating file data for n={n}"):
            generator.rm_dataset_directory()
            generator.create_symmetric_dataset("FOR_K_RANDOM", n)
            _dataHandler = DataHandler(f"datasets/FOR_K_RANDOM{n}/FOR_K_RANDOM{n}.tsp")
            edge_weights = np.array(_dataHandler.get_edge_weights())
            best_k_random = np.inf
            for i in range(start, end, step):
                k_random_step = k_random_for_research(_dataHandler.dimension(), edge_weights, k=step)
                if k_random_step < best_k_random:
                    best_k_random = k_random_step
                data[i] += best_k_random

        for _ in range(start, end, step):
            data[_] /= AMOUNT_OF_FILES_PER_N

    with open(filename, 'w+') as file:
        file.write(json.dumps(full_data, indent=4))


def visualise_k_random_research_data():
    with open(filename, "r") as file:
        full_data = json.loads(file.read())
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    keys = list(map(str, [30, 90, 150, 210]))
    ax = [axs[0][0], axs[0][1], axs[1][0], axs[1][1]]
    ax = dict(list(zip(keys, ax)))
    for n in keys:
        data = full_data[n]
        Xs = list(map(int, list(data.keys())))
        Ys = list(data.values())
        ax[n].plot(Xs, Ys, color="blue", linewidth=3)
        ax[n].set_xticks(np.linspace(min(Xs), max(Xs), 7))
        ax[n].title.set_text(f"Zmieniajacy się best w k_random. N = {n}")
        ax[n].set_xlabel("K - ilość randomizacji ścieżki")
        ax[n].set_ylabel("Najmniejszy znaleziony koszt ścieżki przez algorytm")
    plt.tight_layout()
    plt.show()

def visualize_small_k_random_research_data():
    filename = "../data/k_random_research_small.json"
    with open(filename, "r") as file:
        full_data = json.loads(file.read())
    n = '30'
    data = full_data[n]
    Xs = list(map(int, list(data.keys())))
    Ys = list(data.values())
    plt.plot(Xs, Ys, color="blue", linewidth=3)
    plt.xticks(np.linspace(min(Xs), max(Xs), 7))
    plt.suptitle(f"Zmieniajacy się best w k_random. N = {n}")
    plt.xlabel("K - ilość randomizacji ścieżki")
    plt.ylabel("Najmniejszy znaleziony koszt ścieżki przez algorytm")
    plt.tight_layout()
    plt.show()




if __name__ == "__main__":
    filename = "../data/k_random_research_small.json"
    #generate_k_random_research_data()
    #visualise_k_random_research_data()
    visualize_small_k_random_research_data()