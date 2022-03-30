import json
from matplotlib import pyplot as plt
import itertools

"""
Chce by na jednym obrazie byly 9 wykresy { dla k=1, k=10, k=100 }X{ sort_type = gen_rand, gen_asc, gen_desc }
Na każdym z wykresów mamy insertion sort, merge sort, quick sort
Potrzebne beda 4 obrazy by wyswietlic 
● średnią liczbę wykonanych porównań (c) w zależności od n,
● średnią liczbę przestawień kluczy (s) w zależności od n,
● iloraz c/n w zależności od n,
● iloraz s/n w zależności od n.
"""

def main():
    plt.rcParams.update({'font.size': 12})
    colors = {"insert_sort" : "blue", "merge_sort": "red", "quick_sort": "green", "hybrid_sort": "black"}
    with open("data_to_visualize.json") as file:
        data = json.load(file)
    xs = list(range(100,1001,50))
    main_titles = ["avg_comparisons__", "avg_displacements__", "avg_comparisons__divide", "avg_displacements__divide"]
    for main_title in main_titles:
        fig, axs = plt.subplots(3,3, figsize=(15,15))
        # tutaj bedziemy tworzyc 9 roznych subplotow
        value_type = main_title.split("__")[0]
        divide = "divide" in main_title
        fig.suptitle(f"Plots of {main_title} per different sort")
        subplot_index = 0
        for k, gen_type in itertools.product(['1', '10', '100'], ['gen_asc', 'gen_rand', 'gen_desc']):
            for sort_type in ['merge_sort', 'quick_sort', "hybrid_sort"]:
                # tutaj tworzymy 3 wykresy na jednym subplocie
                ys = list(map(lambda x: data[sort_type][gen_type][str(x)][k][value_type], xs))
                if divide:
                    for i in range(len(xs)):
                        ys[i] /= xs[i]
                axs[subplot_index//3][subplot_index%3].plot(xs, ys, color=colors[sort_type], label=sort_type)
                axs[subplot_index//3][subplot_index%3].set_title(f"k={k};gen_type={gen_type}")
                ylabel = value_type
                if divide:
                    ylabel += " divided by n"
                axs[subplot_index//3][subplot_index%3].set_ylabel(ylabel)
            axs[subplot_index//3][subplot_index%3].legend()
            subplot_index+=1
        fig.set_tight_layout(True)
        plt.savefig(f"plots/{main_title}.png")
        fig.clear()
    return 0

if __name__ == "__main__":
    main()