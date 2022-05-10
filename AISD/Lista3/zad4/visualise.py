import os
import json
from matplotlib import pyplot as plt
from typing import List
import shutil
import math

def main():
    PLOTS="PLOTS"
    COLORS = {
        "inside": "darkred",
        "outside": "darkgreen",
        "first": "orange",
        "half": "darkblue",
        "last": "purple"
    }
    plotting = {
        "inside": dict(),
        "outside": dict(),
        "first": dict(),
        "half": dict(),
        "last": dict()
    }
    DATA = "data"
    possible_n = list(range(1000, 100001, 1000))
    for n in possible_n:
        plot_types = list(map(int, os.listdir(os.path.join(DATA, str(n)))))
        for plot_type in plot_types:
            plt_type_dict = {
                -1: "outside",
                -2: "inside",
                0: "first",
                (n-1): "last",
                n//2: "half"
            }
            plt_type = plt_type_dict[plot_type]
            folder_with_data = os.path.join(DATA, str(n), str(plot_type))
            filenames_with_data = os.listdir(folder_with_data)
            for filename in filenames_with_data:
                path_to_file = os.path.join(folder_with_data, filename)
                with open(path_to_file, 'r') as file:
                    text = file.read()[:-1]
                    words = text.split(" ")
                    _, comparisons, time_spent = list(map(float, words))
                    if plotting[plt_type].get(n) is None: plotting[plt_type][n] = dict()
                    if plotting[plt_type][n].get("comparisons") is None: plotting[plt_type][n]["comparisons"] = 0
                    if plotting[plt_type][n].get("time_spent") is None: plotting[plt_type][n]["time_spent"] = 0
                    plotting[plt_type][n]["time_spent"] += time_spent
                    plotting[plt_type][n]["comparisons"] += comparisons
            plotting[plt_type][n]["time_spent"] /= len(filenames_with_data)
            plotting[plt_type][n]["comparisons"] /= len(filenames_with_data)
    
    fig, axs = plt.subplots(5, 2, figsize=(10, 25))
    axs: List[List[plt.Axes]]
    fig: plt.Figure
    Xs = list(range(1000, 100001, 1000))
    comparisons = dict()
    time_spent = dict()
    plt_types = ["inside", "outside", "first", "last","half"]
    for plt_type in plt_types:
        comparisons[plt_type] = list()
        time_spent[plt_type] = list()
        
        for n in possible_n:
            comparisons[plt_type].append(plotting[plt_type][n]["comparisons"])
            time_spent[plt_type].append(plotting[plt_type][n]["time_spent"])
    
    LINEWIDTH=3
    plt_index = 0
    
    comparison_arguments = {
        "first":[3,0],
        "half":[2.95,0],
        "last":[2.95,0],
        "inside":[2.7,0],
        "outside":[3,0],
    }
    time_spent_arguments = {
        "first":[0.0035,0],
        "half":[0.0037,0],
        "last":[0.0038,0],
        "inside":[0.0033,0],
        "outside":[0.0036,0],
    }
    
    for plt_type in plt_types:
        # function = a*log_2(n)+b
        a_1, b_1 = comparison_arguments[plt_type]
        a_2, b_2 = time_spent_arguments[plt_type]
        
        f1 = [a_1*math.log2(x)+b_1 for x in Xs]
        f2 = [a_2*math.log2(x)+b_2 for x in Xs]
        
        axs[plt_index][0].plot(Xs, comparisons[plt_type],label="real",linewidth=LINEWIDTH, color=COLORS[plt_type])
        axs[plt_index][0].title.set_text(f"Comparisons when search elem is {plt_type}")
        axs[plt_index][0].plot(Xs, f1,label=f"f(n) = {a_1}*log_2(n)+{b_1}",linewidth=LINEWIDTH, color="black")
        
        axs[plt_index][0].legend()
        
        axs[plt_index][1].plot(Xs, time_spent[plt_type],label="real", linewidth=LINEWIDTH, color=COLORS[plt_type])
        axs[plt_index][1].title.set_text(f"Time spent when search elem is {plt_type}")
        axs[plt_index][1].plot(Xs, f2,label=f"f(n) = {a_2}*log_2(n)+{b_2}", linewidth=LINEWIDTH, color="black")
        
        axs[plt_index][1].legend()
        plt_index += 1
        
        
    if PLOTS in os.listdir():  # If plots directory exist in current directory
        shutil.rmtree(PLOTS)   # Delete it
    os.mkdir(PLOTS)            # Make new 
    
    plot_path = os.path.join(PLOTS, f"plots.png")
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.clf()
    
    
if __name__ == "__main__":
    main()