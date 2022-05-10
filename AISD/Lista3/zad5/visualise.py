import os
import json
from matplotlib import pyplot as plt
from typing import List
import shutil
import math
import numpy as np

def main():
    PLOTS="PLOTS"
    plot_path = os.path.join(PLOTS, "plot.png")
    #if PLOTS in os.listdir():  # If plots directory exist in current directory
    #    shutil.rmtree(PLOTS)   # Delete it
    #os.mkdir(PLOTS)            # Make new 
    
    DATA = "data"
    dp_quicksort_names = ["dual_pivot_quicksort", "dual_pivot_quicksort_select"]
    quicksort_names = ["quicksort", "quicksort_select"]
    algo_names = ["dual_pivot_quicksort", "dual_pivot_quicksort_select", "quicksort", "quicksort_select"]
    gen_types = ["gen_rand", "gen_asc", "gen_desc"]
    COLORS = ["darkgreen", "darkred"]
    COLORS_OPT = ["purple", "black"]
    MAX_M = 10
    MIN_M = 1
    possible_m = list(range(1, MAX_M+1))
    
    ROWS=3
    COLS=4
    fig, axs = plt.subplots(ROWS, COLS, figsize=(COLS*5, ROWS*5))
    axs: List[List[plt.Axes]]
    fig: plt.Figure
    Xs = list(range(100, 10001, 100))
    data = dict()
    for gen_type in gen_types:
        data[gen_type] = dict()
        for name in algo_names:
            data[gen_type][name] = dict()
            data[gen_type][name]["comparisons"] = list()
            data[gen_type][name]["displacements"] = list()
    for gen_type in gen_types:
        for name in algo_names:
            for x in Xs:
                data[gen_type][name]["comparisons"].append(0)
                data[gen_type][name]["displacements"].append(0)
                for m in possible_m:
                    with open(f"data/{name}_{gen_type}_{x}_{m}", 'r') as file:
                        comparisons, displacements = list(map(int, file.read()[:-1].split(" ")))
                        data[gen_type][name]["comparisons"][-1] += comparisons
                        data[gen_type][name]["displacements"][-1] += displacements
                data[gen_type][name]["comparisons"][-1] /= MAX_M
                data[gen_type][name]["displacements"][-1] /= MAX_M
                
    for gen_type_index, gen_type in enumerate(gen_types):
        LINEWIDTH=3
        axs[gen_type_index][0].title.set_text(f"{gen_type} for comparisons dual pivot quicksort")
        for sort_index, name in enumerate(dp_quicksort_names):
            axs[gen_type_index][0].plot(Xs, data[gen_type][name]["comparisons"], label=f"{name}", color=COLORS[sort_index], linewidth=LINEWIDTH)
        
        axs[gen_type_index][1].title.set_text(f"{gen_type} for displacements dual pivot quicksort")
        for sort_index, name in enumerate(dp_quicksort_names):
            axs[gen_type_index][1].plot(Xs, data[gen_type][name]["displacements"], label=f"{name}", color=COLORS[sort_index], linewidth=LINEWIDTH)
        
        axs[gen_type_index][2].title.set_text(f"{gen_type} for comparisons quicksort")
        for sort_index, name in enumerate(quicksort_names):
            axs[gen_type_index][2].plot(Xs, data[gen_type][name]["comparisons"], label=f"{name}", color=COLORS[sort_index], linewidth=LINEWIDTH)
        axs[gen_type_index][3].title.set_text(f"{gen_type} for displacements quicksort")
        for sort_index, name in enumerate(quicksort_names):
            axs[gen_type_index][3].plot(Xs, data[gen_type][name]["displacements"], label=f"{name}", color=COLORS[sort_index], linewidth=LINEWIDTH)

        
    LINEWIDTH=1.5
    Xs= np.array(Xs)
    gen_type_index = 0
    axs[gen_type_index][0].plot(Xs, 14*Xs*np.log2(Xs), label=f"f(n)=14nlog2(n)", color=COLORS_OPT[0], linewidth=LINEWIDTH)
    axs[gen_type_index][0].plot(Xs, 24*Xs, label=f"f(n)=24n", color=COLORS_OPT[1], linewidth=LINEWIDTH)
    axs[gen_type_index][1].plot(Xs, 10*Xs*np.log2(Xs), label=f"f(n)=10nlog2(n)", color=COLORS_OPT[0], linewidth=LINEWIDTH)
    axs[gen_type_index][1].plot(Xs, 20*Xs, label=f"f(n)=20n", color=COLORS_OPT[1], linewidth=LINEWIDTH)
    axs[gen_type_index][2].plot(Xs, 9*Xs*np.log2(Xs), label=f"f(n)=9nlog2(n)", color=COLORS_OPT[0], linewidth=LINEWIDTH)
    axs[gen_type_index][2].plot(Xs, 28*Xs, label=f"f(n)=28n", color=COLORS_OPT[1], linewidth=LINEWIDTH)
    axs[gen_type_index][3].plot(Xs, 7.5*Xs*np.log2(Xs), label=f"f(n)=7.5nlog2(n)", color=COLORS_OPT[0], linewidth=LINEWIDTH)
    axs[gen_type_index][3].plot(Xs, 24*Xs, label=f"f(n)=24n", color=COLORS_OPT[1], linewidth=LINEWIDTH)
    gen_type_index = 1
    axs[gen_type_index][0].plot(Xs, 0.46*Xs*Xs, label=f"f(n)=0.46n^2", color=COLORS_OPT[0], linewidth=LINEWIDTH)
    axs[gen_type_index][0].plot(Xs, 0.02*Xs*Xs, label=f"f(n)=0.02n^2", color=COLORS_OPT[1], linewidth=LINEWIDTH)
    axs[gen_type_index][1].plot(Xs, 9*Xs*np.log2(Xs), label=f"f(n)=9nlog2(n)", color=COLORS_OPT[0], linewidth=LINEWIDTH)
    axs[gen_type_index][1].plot(Xs, 5*Xs, label=f"f(n)=5n", color=COLORS_OPT[1], linewidth=LINEWIDTH)
    axs[gen_type_index][2].plot(Xs, 10*Xs, label=f"f(n)=10n", color=COLORS_OPT[0], linewidth=LINEWIDTH)
    axs[gen_type_index][2].plot(Xs, 0.75*Xs*Xs, label=f"f(n)=0.75n^2", color=COLORS_OPT[1], linewidth=LINEWIDTH)
    axs[gen_type_index][3].plot(Xs, 10*Xs*np.log2(Xs), label=f"f(n)=10nlog2(n)", color=COLORS_OPT[0], linewidth=LINEWIDTH)
    axs[gen_type_index][3].plot(Xs, 1.1*Xs*Xs, label=f"f(n)=n^2", color=COLORS_OPT[1], linewidth=LINEWIDTH)
    gen_type_index = 2
    axs[gen_type_index][0].plot(Xs, 0.02*Xs*Xs, label=f"f(n)=0.02n^2", color=COLORS_OPT[0], linewidth=LINEWIDTH)
    axs[gen_type_index][0].plot(Xs, 0.4*Xs*Xs, label=f"f(n)=0.4n^2", color=COLORS_OPT[1], linewidth=LINEWIDTH)
    axs[gen_type_index][1].plot(Xs, 0.02*Xs*Xs, label=f"f(n)=0.02n^2", color=COLORS_OPT[0], linewidth=LINEWIDTH)
    axs[gen_type_index][1].plot(Xs, 0.3*Xs*Xs, label=f"f(n)=0.3n^2", color=COLORS_OPT[1], linewidth=LINEWIDTH)
    axs[gen_type_index][2].plot(Xs, 10*Xs, label=f"f(n)=10n", color=COLORS_OPT[0], linewidth=LINEWIDTH)
    axs[gen_type_index][2].plot(Xs, 0.95*Xs*Xs, label=f"f(n)=0.95n^2", color=COLORS_OPT[1], linewidth=LINEWIDTH)
    axs[gen_type_index][3].plot(Xs, 10*Xs, label=f"f(n)=10n", color=COLORS_OPT[0], linewidth=LINEWIDTH)
    axs[gen_type_index][3].plot(Xs, 0.6*Xs*Xs, label=f"f(n)=0.6n^2", color=COLORS_OPT[1], linewidth=LINEWIDTH)
    
    for i in range(ROWS):    
        for j in range(COLS):
            axs[i][j].legend()
        

    plt.tight_layout()
    plt.savefig(plot_path)
    plt.clf()
if __name__ == "__main__":
    main()