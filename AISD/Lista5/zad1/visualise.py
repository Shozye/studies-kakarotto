import json
from matplotlib import pyplot as plt
from typing import List
import sys

COLORS = ["blue", "orange", "green", "red", "purple", "brown", "pink", "gray", "olive", "cyan"]
TITLES = ["Amount of displacements for different sorts", "Amount of Comparisons for different sorts"]
SORT_TYPES = ["insert_sort", "merge_sort", "dual_pivot_quick_sort", "quick_sort", "hybrid_sort" ,"max_heap_test"]
YLABELS = ["Amount of displacements", "Amount of comparisons"]
KEYS = ["displacements", "comparisons"]
XLABEL = "N - amount of numbers in array"
LINEWIDTH = 3
FIGURE_SIZE = 5
NOINSERT = len(sys.argv) > 1
PLOTS_PATH = "plots.png" if NOINSERT == False else "plots_noinsert.png"

with open("data.json") as file:
    data = json.loads(file.read())

axs: List[plt.Axes]
fig: plt.Figure

fig, axs = plt.subplots(2, 1, figsize=(FIGURE_SIZE, 2*FIGURE_SIZE))

for sort_index, sort_type in enumerate(SORT_TYPES):
    if NOINSERT and sort_type == 'insert_sort':
        continue
    for i in range(len(KEYS)):
        ylabel = YLABELS[i]
        key = KEYS[i]
        title = TITLES[i]
        Xs = data[sort_type]["Xs"]
        Ys = data[sort_type][key]
        
        if sort_type == "max_heap_test":
            axs[i].plot(Xs, Ys, label=sort_type, linewidth=LINEWIDTH+2)
        else:
            axs[i].plot(Xs, Ys, label=sort_type, linewidth=LINEWIDTH)
        axs[i].set_title(title)
        axs[i].set_ylabel(ylabel)
        axs[i].legend()

plt.tight_layout()

plt.savefig(PLOTS_PATH)
plt.clf()