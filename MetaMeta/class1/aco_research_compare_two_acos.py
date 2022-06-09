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
research_type = "Start_Ants"
AMOUNT_OF_TRIES_PER_N = 15
DATASET_SIZES = list(range(25, 61, 5))
MIN_ROUND_TRIPS = 200
FILENAME = f"aco_different_{research_type}_research_{AMOUNT_OF_TRIES_PER_N}_{MIN_ROUND_TRIPS}.json"



def ant_amount_research():
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

            algos = TSPAlgorithms(data)
            for ant_colony_type in ["normal", "different"]:
                algos.ant_colony(ant_colony_type=ant_colony_type,
                                 min_round_trips=MIN_ROUND_TRIPS,
                                 time=0,
                                 ant_count=-1,
                                 ant_speed=1,
                                 decay_power=3,
                                 best_path_smell=1.75,
                                 pheromone_power=1.25,
                                 distance_power=1)
                research_data[ant_colony_type][dataset_size] += (algos.last_cost / AMOUNT_OF_TRIES_PER_N)
    path_to_filename = os.path.join(DIR, FILENAME)
    with open(path_to_filename, 'w+') as file:
        file.write(json.dumps(research_data))


def visualise_ant_amount():
    PLOT_NAME = FILENAME.split(".")[0] + ".png"
    with open(os.path.join(DIR, FILENAME), 'r') as file:
        research_data = json.loads(file.read())
    research_keys = list(research_data.keys())
    dataset_sizes = sorted(list(research_data[research_keys[0]].keys()))

    for key in research_keys:
        data = []
        for dataset_size in dataset_sizes:
            data.append(research_data[key][dataset_size])
        label = f"{research_type} {key}"
        plt.plot(dataset_sizes, data, label=label)
    plt.legend()
    plt.xlabel("N - Size of file")
    plt.ylabel("Goal Function")
    plt.tight_layout()
    plot_path = os.path.join(PLOT_DIR, PLOT_NAME)
    plt.savefig(plot_path)


if __name__ == "__main__":
    ant_amount_research()
    visualise_ant_amount()
