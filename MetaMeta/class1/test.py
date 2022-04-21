from TSPAlgorithms import TSPAlgorithms
from DataHandler import DataHandler
import matplotlib.pyplot as plt
import networkx as nx
import neighbourings
from FileGenerator import FileGenerator
from typing import List
from neighbourings import *

def main():
    generator = FileGenerator()
    generator.rm_dataset_directory()
    generator.create_symmetric_EUC2D_dataset("GANGI", 52)
    dataHandler = DataHandler(generator.last_path)
    algos = TSPAlgorithms(dataHandler)
    algos.k_random()
    cost = algos.taboo_search(invert, algos.last_solution)
    # analyze_file(dataHandler, verbose=True)

def analyze_file(data: DataHandler, verbose=False):
    """
    Funkcja do szybkiej analizy pliku. Odpala wszystkie algorytmy i rysuje ich rozwiązania.
    :param data:
    :param verbose: Dla dokladniejszej analizy i rysowania trzeba podać argument True do funkcji
    """
    algos = TSPAlgorithms(data)
    K = 10000

    # only used in verbose and euc2d but need scope
    axs: List[List[plt.Axes]]
    fig: plt.Figure
    fig, axs = plt.subplots(4, 2, figsize=(20, 40))
    axs[0][1].remove()

    algorithms_and_parameters = [
        [algos.k_random, tuple([K]), axs[0][0]],
        [algos.closest_neighbour, tuple(), axs[1][0]],
        [algos.repetitive_closest_neighbour, tuple(), axs[1][1]],
        [algos.two_opt, tuple([neighbourings.invert]), axs[2][0]],
        [algos.two_opt, tuple([neighbourings.swap]), axs[2][1]],
        [algos.taboo_search, tuple([neighbourings.invert]), axs[3][0]],
        [algos.taboo_search, tuple([neighbourings.swap]), axs[3][1]]
    ]

    for algorithm in algorithms_and_parameters:
        algo, parameter_list, ax = algorithm
        ax: plt.Axes
        function_label = f"{algo.__name__}({', '.join(list(map(str, parameter_list)))})"
        print(f"{function_label} = {algo(*parameter_list)}")  # func(*params) = func(params[0], params[1],...,params[k])
        solution = algos.last_solution
        if verbose:
            print(f"Solution:", algos.last_solution)
            if data.isEuc2D():
                edges = [(solution[i], solution[i + 1]) for i in range(len(solution) - 1)]
                edges.append((solution[len(solution) - 1], solution[0]))
                nx.draw(data.getGraph(), ax=ax, pos=data.getPos(), with_labels=True,
                        node_size=300, node_color="#ADD8E6")
                nx.draw_networkx_edges(data.getGraph(), pos=data.getPos(), ax=ax,
                                       edgelist=edges, width=2)
                ax.title.set_text(function_label + f"\n cost={algos.last_cost}")
    if verbose and data.isEuc2D():
        fig.suptitle(f"Wykres algorytmów dla instancji {data.name}", fontsize=16)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()
