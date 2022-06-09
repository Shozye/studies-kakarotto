import tsplib95
from TSPAlgorithms import TSPAlgorithms
from FileGenerator import FileGenerator
import os
from collections import defaultdict
import json
from tqdm import tqdm
from matplotlib import pyplot as plt

DIR = os.path.join(os.getcwd(), "aco_research")
PLOT_DIR = os.path.join(os.getcwd(), "aco_plots")


def ant_amount_research():
    DIFFERENT_ANT_COUNTS = [16, 32, 64, -1]
    DATASET_SIZES = list(range(10, 41, 5))
    FILE_NAME = f"aco_ant_size_research_{AMOUNT_OF_TRIES_PER_N}_{TIME}.json"
    research_data = defaultdict(lambda: defaultdict(int))

    generator = FileGenerator()
    pbar = tqdm(range(AMOUNT_OF_TRIES_PER_N))
    for _ in pbar:
        for dataset_size in DATASET_SIZES:
            pbar.set_description(f"Researching {_}-th time dataset_size = {dataset_size}")
            generator.rm_dataset_directory()
            generator.create_symmetric_EUC2D_dataset("GANGI", dataset_size)
            data = tsplib95.load(generator.last_path)
            data: tsplib95.models.StandardProblem

            for ant_count in DIFFERENT_ANT_COUNTS:
                _ant_count = dataset_size if ant_count == -1 else ant_count
                algos = TSPAlgorithms(data)
                algos.ant_colony(min_round_trips=0,
                                 time=TIME,
                                 ant_count=_ant_count,
                                 ant_speed=1,
                                 decay_power=0,
                                 best_path_smell=2,
                                 pheromone_power=1.25,
                                 distance_power=1)
                research_data[ant_count][dataset_size] += (algos.last_cost / AMOUNT_OF_TRIES_PER_N)
    path_to_filename = os.path.join(DIR, FILE_NAME)
    with open(path_to_filename, 'w+') as file:
        file.write(json.dumps(research_data))


def visualise_ant_amount():
    FILENAME = f"aco_ant_size_research_{AMOUNT_OF_TRIES_PER_N}_{TIME}.json"
    PLOT_NAME = FILENAME.split(".")[0] + ".png"
    with open(os.path.join(DIR, FILENAME), 'r') as file:
        research_data = json.loads(file.read())
    ant_counts = list(research_data.keys())
    dataset_sizes = sorted(list(research_data[ant_counts[0]].keys()))

    for ant_count in ant_counts:
        data = []
        for dataset_size in dataset_sizes:
            data.append(research_data[ant_count][dataset_size])
        label = "ant_count " + ("len(dataset)" if ant_count == "-1" else ant_count)
        plt.plot(dataset_sizes, data, label=label)
    plt.legend()
    plt.xlabel("N - Size of file")
    plt.ylabel("Goal Function")
    plt.tight_layout()
    plot_path = os.path.join(PLOT_DIR, PLOT_NAME)
    plt.savefig(plot_path)


if __name__ == "__main__":
    AMOUNT_OF_TRIES_PER_N = 50
    TIME = 0.25
    ant_amount_research()
    visualise_ant_amount()
