import os
from datetime import datetime
import json
from DataHandler import DataHandler
from FileGenerator import FileGenerator
from TSPAlgorithms import TSPAlgorithms
from matplotlib import pyplot as plt
from neighbourings import invert, swap

def research_taboo_search(neighboring_function, filename=None, TABOO_LIST_SIZE=20, TIME=30): # dodać starting_solution: np.array,
    if not filename:
        filename = "taboo_researches/taboo_" + "_".join(str(datetime.now()).split(" ")).split(".")[0] + ".json"
    if ".json" not in filename:
        filename += ".json"
    if "taboo_researches/" not in filename:
        filename = "taboo_researches/" + filename
    generator = FileGenerator()

    data_for_different_n = dict()
    for n in range(START_RANGE, END_RANGE, STEP_RANGE):
        print(n)
        data_for_different_n[n] = 0
        for _ in range(AMOUNT_FOR_N):
            generator.rm_dataset_directory()
            generator.create_symmetric_EUC2D_dataset("RESEARCH", n)
            data = DataHandler(generator.last_path)
            algos = TSPAlgorithms(data)
            algos.two_opt()
            print(algos.last_cost)
            cost = algos.taboo_search(neighboring_function, algos.last_solution, TIME)
            print(cost)
            data_for_different_n[n] += cost
        data_for_different_n[n] /= AMOUNT_FOR_N

    with open(filename, 'w+') as file:
        file.write(json.dumps(data_for_different_n))

def draw_all_researches():
    filenames = os.listdir("taboo_researches/")

    for filename in filenames:
        filepath = "taboo_researches/" + filename
        with open(filepath) as file:
            data = json.loads(file.read())
            keys = list(data.keys())
            values = [data[key] for key in keys]
            plt.plot(keys, values, label=filename)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    START_RANGE = 30
    END_RANGE = 35
    STEP_RANGE = 1
    AMOUNT_FOR_N = 5
    # research_taboo_search(swap, "BasicTaboo_Invert_Deque30_Time30", 30, 1)
    # research_taboo_search(swap, "BasicTaboo_Swap_Deque30_Time30", 30, 1)
    # research_taboo_search(invert, "BasicTaboo_Invert_Deque20_Time30", 20, 1)
    # research_taboo_search(swap, "BasicTaboo_Swap_Deque20_Time30", 20, 1)
    # research_taboo_search(invert, "BasicTaboo_Invert_Deque10_Time30", 10, 1)
    # research_taboo_search(swap, "BasicTaboo_Swap_Deque10_Time30", 10, 1)
    draw_all_researches()