from matplotlib import pyplot as plt
import json
from collections import defaultdict
from typing import List, Dict
from itertools import product
import os
import shutil

DATA = "data.json"
data: Dict[str, Dict[str, Dict[str, float]]]

with open(DATA, 'r') as file:
    data = json.loads(file.read())

INSERT_TYPES = list(data.keys())
Xs = list(data[INSERT_TYPES[0]].keys())
plot_keys = list(data[INSERT_TYPES[0]][Xs[0]].keys())
max_keys = []
mean_keys = []
for key in plot_keys:
    if "max" in key: max_keys.append(key)
    elif "mean" in key: mean_keys.append(key)
plot = defaultdict(list)

for insert_type in INSERT_TYPES:
    for x in Xs:
        for key, value in data[insert_type][x].items():
            plot[(insert_type, key)].append(value)

PLOTS = "PLOTS"
if os.path.isdir(PLOTS):
    shutil.rmtree(PLOTS)
os.mkdir(PLOTS)

LINEWIDTH=3
Xs = list(map(int, Xs))
for insert_type, keys_name in product(INSERT_TYPES, ["max", "mean"]):
    keys = max_keys if keys_name == "max" else mean_keys
    axs: List[List[plt.Axes]]
    fig: plt.Figure
    fig, axs = plt.subplots(len(keys), 1, figsize=(10, len(keys)*10))
    
    for i, key in enumerate(keys):
        axs[i].plot(Xs, plot[(insert_type, key)], label=f"{insert_type}_{key}", linewidth=LINEWIDTH, color='red')
        axs[i].legend()
    
    plot_path = os.path.join(PLOTS, f"plot_{insert_type}_{keys_name}.png")
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.clf()
    
