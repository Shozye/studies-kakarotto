import time
import json
from matplotlib import pyplot as plt
import math
from MetaMeta.class1.DataHandler import DataHandler
from MetaMeta.class1.FileGenerator import FileGenerator
from MetaMeta.class1.TSPAlgorithms import TSPAlgorithms
import numpy as np

def complexity_data_maker():
    generator = FileGenerator()
    generator.rm_dataset_directory()

    start = 10
    end = 120
    step = 2
    for i in range(start, end, step):
        generator.create_symmetric_dataset("GANGI", i)
    data = {"two_opt": [], "k_random": [], "repetitive_closest_neighbour": [], "two_opt_and_repetitive_neighbour": []}
    timestamp = time.time()
    for i in range(start, end, step):
        if i in [x * end // 10 for x in range(10)]:
            print(f"Done i={i}. It took {time.time() - timestamp} from previous")
            timestamp = time.time()
        _data = DataHandler(f"datasets/GANGI{i}/GANGI{i}.tsp")
        algos = TSPAlgorithms(_data.get_edge_weights(), _data.dimension())
        map_algos = {"two_opt": algos.two_opt_invert, "k_random": algos.k_random,
                     "repetitive_closest_neighbour": algos.repetitive_closest_neighbour,
                     "two_opt_and_repetitive_neighbour": algos.two_opt_with_repetitive_closest_neighbour}
        for key in list(map_algos.keys()):
            mean = 0
            amount = 0
            for _ in range(20):
                time_start = time.time()
                map_algos[key]()
                time_duration = time.time() - time_start
                mean += time_duration
                amount += 1
            data[key].append((i, mean / amount))
    with open(f"data/{filename}", 'w+') as file:
        file.write(json.dumps(data))


def two_opt_with_repetitive_tester():
    generator = FileGenerator()
    generator.rm_dataset_directory()

    start = 10
    end = 120
    step = 1
    for i in range(start, end, step):
        generator.create_symmetric_dataset("GANGI", i)
    data = {"two_opt_and_repetitive_neighbour": []}
    timestamp = time.time()
    for i in range(start, end, step):
        if i in [x * end // 10 for x in range(10)]:
            print(f"Done i={i}. It took {time.time() - timestamp} from previous")
            timestamp = time.time()
        generator.rm_dataset_directory()
        generator.create_symmetric_dataset("GANGI", i)
        _data = DataHandler(f"datasets/GANGI{i}/GANGI{i}.tsp")
        algos = TSPAlgorithms(_data.get_edge_weights(), _data.dimension())
        map_algos = {"two_opt_and_repetitive_neighbour": algos.two_opt_with_repetitive_closest_neighbour}
        for key in list(map_algos.keys()):
            mean = 0
            amount = 0
            for _ in range(30):
                time_start = time.time()
                map_algos[key]()
                time_duration = time.time() - time_start
                mean += time_duration
                amount += 1
                generator.rm_dataset_directory()
                generator.create_symmetric_dataset("GANGI", i)
                _data = DataHandler(f"datasets/GANGI{i}/GANGI{i}.tsp")
                algos = TSPAlgorithms(_data.get_edge_weights(), _data.dimension())
                map_algos = {"two_opt_and_repetitive_neighbour": algos.two_opt_with_repetitive_closest_neighbour}
            data[key].append((i, mean / amount))
    with open(f"data/{filename}", 'w+') as file:
        file.write(json.dumps(data))


def two_opt_with_repetitive_visualize():
    with open(f"data/{filename}", 'r') as file:
        data = json.loads(file.read())
    Xs = [x[0] for x in data['two_opt_and_repetitive_neighbour']]
    Ys = [x[1] for x in data['two_opt_and_repetitive_neighbour']]
    plt.plot(Xs, Ys)
    plt.suptitle("Two opt seeded by Repetitive Closest neighbour")
    plt.tight_layout()
    plt.show()


def complexity_visualize():
    with open(f"../data/complexity_data_maker_end=120_rep=20_json", "r") as file:
        data = json.loads(file.read())
    with open(f"../data/repetitive_complexity_data_maker_end=120_rep=20_json", 'r') as file:
        data2 = json.loads(file.read())
    data['two_opt_and_repetitive_neighbour'] = data2['two_opt_and_repetitive_neighbour']
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    keys = list(data.keys())
    axes_for_keys = dict(zip(keys, [axs[0][0], axs[0][1], axs[1][0], axs[1][1]]))
    titles = {"two_opt": "Two Opt Invert",
              "k_random": "k_random for k=1000",
              "repetitive_closest_neighbour": "Repetitive Closest Neighbour",
              "two_opt_and_repetitive_neighbour": "Two opt seeded by Repetitive Closest neighbour"}
    for key in keys:
        Xs = [x[0] for x in data[key]]
        Ys = [x[1] for x in data[key]]
        axes_for_keys[key].plot(Xs, Ys, label=key, color="blue",linewidth='5')
        axes_for_keys[key].set_xlabel("N - dimension of the file")
        axes_for_keys[key].set_ylabel("Time[s]")
        axes_for_keys[key].title.set_text(titles[key])
        if key == "two_opt":
            function = np.zeros(len(Xs))
            function2 = np.zeros(len(Xs))
            function3 = np.zeros(len(Xs))
            for i in range(len(Xs)):
                function[i] = Xs[i]**3 / (math.log(Xs[i]) * 15000)
                function3[i] = Xs[i]**3 / 50000
            axes_for_keys[key].plot(Xs, function, label="y=x^3 / (log(x)*1.5*10^4)", color="red")
            axes_for_keys[key].plot(Xs, function3, label="y=x^3 / (5*10^4)", color="green")
        elif key == "k_random":
            function = np.zeros(len(Xs))
            for i in range(len(Xs)):
                function[i] = Xs[i] / 5600
            axes_for_keys[key].plot(Xs, function, label="y=x/(5.6*10^3)", color="red")
        elif key == "repetitive_closest_neighbour":
            function = np.zeros(len(Xs))
            for i in range(len(Xs)):
                function[i] = Xs[i] **3 / 25000000
            axes_for_keys[key].plot(Xs, function, label="y=x^3/(2.5*10^7)", color="red")
        elif key == "two_opt_and_repetitive_neighbour":
            function = np.zeros(len(Xs))
            for i in range(len(Xs)):
                function[i] = Xs[i] **3 / 500000
            axes_for_keys[key].plot(Xs, function, label="y=x^3 / (5*10^5)", color="red")
        axes_for_keys[key].legend()
    plt.tight_layout()
    plt.show()


def measure_k_random_effectiveness(n=50):
    data = []
    generator = FileGenerator()
    generator.rm_dataset_directory()


if __name__ == "__main__":
    filename = "repetitive_complexity_data_maker_end=120_rep=20_json"
    #two_opt_with_repetitive_tester()
    #two_opt_with_repetitive_visualize()
    # complexity_data_maker()
    complexity_visualize()
