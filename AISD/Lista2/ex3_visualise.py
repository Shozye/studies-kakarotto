import json
from matplotlib import pyplot as plt
import itertools
import math

def main():
    colors = {"dual_pivot_quick_sort" : "blue", "n_ln_n": "red", "quick_sort": "green"}
    xs = list(range(100,1001, 50))
    with open("data_to_visualize.json") as file:
        data = json.load(file)
    k="100"   
    fig,axs = plt.subplots(2,3, figsize=(15,15))
    fig.suptitle("Plots to differentiate quicksort from DP quicksort")

    subplot_index = 0
    for gen_type, value_type in itertools.product(["gen_asc", 'gen_rand', 'gen_desc'], ['avg_comparisons', 'avg_displacements']):
        plot_now = axs[subplot_index//3][subplot_index%3]
        plot_now.set_title(f"value_type={value_type};gen_type={gen_type}")
        plot_now.set_ylabel(value_type)
        for sort_type in ['quick_sort', 'dual_pivot_quick_sort']:
            ys = list(map(lambda x: data[sort_type][gen_type][str(x)][k][value_type], xs))
            plot_now.plot(xs, ys, color=colors[sort_type], label=sort_type, linewidth=10.0)
        constant = 1
        nlogn_ys = list(map(lambda x: constant*x*math.log2(x), xs))
        plot_now.plot(xs, nlogn_ys, color=colors["n_ln_n"], label=f"{constant}*n*log_2(n)")
        plot_now.legend()
        subplot_index += 1
    fig.set_tight_layout(True)
    plt.savefig(f"plots/dp_qs_quicksort_research.png")
    return 0
        
if __name__ == "__main__":
    main()