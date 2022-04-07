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
import time


def generate_quality_research_data():
    data = dict()
    generator = FileGenerator()

    algos_names = ["k_random", "repetitive_closest_neighbour", "two_opt",
             "two_opt_with_repetitive_closest_neighbour"]
    for algo in algos_names:
        data[algo] = dict()
    for i in range(TIME_AMOUNT):
        data["k_random"][i] = 0
        data["two_opt"][i] = 0
    for i in [1, TIME_AMOUNT]:
        data["two_opt_with_repetitive_closest_neighbour"][i] = 0
        data["repetitive_closest_neighbour"][i] = 0
    DIFF_FILE_TRIES = 10
    for _ in range(DIFF_FILE_TRIES):
        generator.rm_dataset_directory()
        generator.create_symmetric_dataset("GANGI", 50)
        _dataHandler = DataHandler(f"datasets/GANGI50/GANGI50.tsp")
        algos = TSPAlgorithms(_dataHandler.get_edge_weights(), _dataHandler.dimension())
        start_time = time.time()
        data_small = np.zeros(TIME_AMOUNT)
        best_cost = np.inf
        while True:
            solution = algos.k_random()
            if solution[1] < best_cost:
                best_cost = solution[1]
            time_passes = round(time.time() - start_time)
            if time_passes >= TIME_AMOUNT:
                break
            else:
                if data_small[time_passes] != 0:
                    if data_small[time_passes] > best_cost:
                        data_small[time_passes] = best_cost
                else:
                    data_small[time_passes] = best_cost
                for nexts in range(time_passes + 1, TIME_AMOUNT):
                    data_small[nexts] = data_small[time_passes]

        for i in range(TIME_AMOUNT):
            data["k_random"][i] += data_small[i]

        data["repetitive_closest_neighbour"][1] += algos.repetitive_closest_neighbour()[1]
        data["repetitive_closest_neighbour"][TIME_AMOUNT] += algos.repetitive_closest_neighbour()[1]

        start_time = time.time()
        data_small = np.zeros(TIME_AMOUNT)
        best_cost = np.inf
        while True:
            solution = algos.two_opt_invert()
            if solution[1] < best_cost:
                best_cost = solution[1]
            time_passes = round(time.time() - start_time)
            if time_passes >= TIME_AMOUNT:
                break
            else:
                if data_small[time_passes] != 0:
                    if data_small[time_passes] > best_cost:
                        data_small[time_passes] = best_cost
                else:
                    data_small[time_passes] = best_cost
                for nexts in range(time_passes + 1, TIME_AMOUNT):
                    data_small[nexts] = data_small[time_passes]
        for i in range(TIME_AMOUNT):
            data["two_opt"][i] += data_small[i]

        data["two_opt_with_repetitive_closest_neighbour"][1] += algos.two_opt_with_repetitive_closest_neighbour()[1]
        data["two_opt_with_repetitive_closest_neighbour"][TIME_AMOUNT] += algos.two_opt_with_repetitive_closest_neighbour()[
            1]
    for algo in algos_names:
        for key in list(data[algo].keys()):
            data[algo][key] /= DIFF_FILE_TRIES
    with open(filename, 'w+') as file:
        file.write(json.dumps(data))


def visualise_quality_research_data():
    with open(filename) as file:
        data = json.loads(file.read())
    algos = ["k_random", "repetitive_closest_neighbour", "two_opt",
             "two_opt_with_repetitive_closest_neighbour"]

    for algo in algos:
        Xs = list(data[algo].keys())
        Ys = [data[algo][x] for x in Xs]
        to_del = []
        for i in range(len(Ys)):
            if Ys[i] == 0:
                to_del.append(i)
        for d in to_del[::-1]:
            del Ys[d]
            del Xs[d]
        plt.plot(list(map(float, Xs)), Ys, label=algo)
    plt.suptitle("Wykresy czasu do najlepszego znalezienia algorytmu dla n=50")
    plt.xlabel("Czas[s]")
    plt.ylabel("Koszt ścieżki")

    plt.xticks(np.linspace(0, TIME_AMOUNT, 5))
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    TIME_AMOUNT = 180
    filename = "data/quality_research.json"
    generate_quality_research_data()
    visualise_quality_research_data()
