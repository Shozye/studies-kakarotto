from TSPAlgorithms import TSPAlgorithms
from DataHandler import DataHandler
import tsplib95
import matplotlib.pyplot as plt
import networkx as nx
import neighbourings
from FileGenerator import FileGenerator
import math
from typing import List
from neighbourings import *
from GoalCalculator import GoalCalculator
import time

def main():
    generator = FileGenerator()
    generator.rm_dataset_directory()
    generator.create_symmetric_EUC2D_dataset("GANGI", 52)
    dataHandler = DataHandler(generator.last_path)
    algos = TSPAlgorithms(dataHandler)

    # W tym momencie taboo search zaseeduje sobie z losowego rozwiazania
    cost = algos.taboo_search("basic")
    # W tym momencie taboo search zaseeduje z rozwiazania neareset neighbour
    algos.repetitive_closest_neighbour()
    cost = algos.taboo_search("basic", starting_solution=algos.last_solution)
    # Mogę też użyć przyśpieszonego Tab00 Searcha
    algos.k_random(100000)
    cost = algos.taboo_search("accelerate", starting_solution=algos.last_solution)

    analyze_file(dataHandler, verbose=True)


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
        [algos.taboo_search, tuple(["accelerate", neighbourings.invert]), axs[3][0]],
        [algos.taboo_search, tuple(["accelerate", neighbourings.swap]), axs[3][1]]
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

def goalCalculatorTest(neighbouring_function, i, j, N, is_symmetric, TIMES=1, should_print=False):
    generator = FileGenerator()
    generator.rm_dataset_directory()
    generator.create_symmetric_EUC2D_dataset("Test", N)
    dataHandler = DataHandler(generator.last_path)
    goal = GoalCalculator(dataHandler)

    algos = TSPAlgorithms(dataHandler)
    algos.k_random()
    main_solution = algos.last_solution

    goal.set_main_solution(main_solution)
    goal.set_neighboring_function(neighbouring_function)

    solution = neighbouring_function(main_solution, i, j)
    time_basic = time.time()
    solution_cost_basic = -2.0
    for _ in range(TIMES):
        solution_cost_basic = goal.basic_goal(solution)
    time_accelerated = time.time()
    solution_cost_accelerated = -1.0
    for _ in range(TIMES):
        solution_cost_accelerated = goal.goal(solution, i, j)
    if should_print:
        print(f"Calculate basic {neighbouring_function.__name__} symmetric={str(is_symmetric)} {TIMES} times took       {round(time.time() - time_basic, 4)} seconds")
        print(f"Calculate accelerated {neighbouring_function.__name__} symmetric={str(is_symmetric)} {TIMES} times took {round(time.time() - time_accelerated, 4)} seconds")
    assert round(solution_cost_basic, 5) == round(solution_cost_accelerated, 5), f"{solution_cost_basic} != {solution_cost_accelerated}"

def goalCalculatorTests():
    goalCalculatorTest(invert, 2, 6, 100, is_symmetric=True)
    goalCalculatorTest(invert, 0, 20, 100, is_symmetric=True)
    goalCalculatorTest(invert, 80, 99, 100, is_symmetric=True)
    goalCalculatorTest(invert, 80, 81, 100, is_symmetric=True)
    goalCalculatorTest(swap, 80, 81, 100, is_symmetric=True)
    goalCalculatorTest(swap, 2, 6, 100, is_symmetric=True)
    goalCalculatorTest(swap, 0, 20, 100, is_symmetric=True)
    goalCalculatorTest(swap, 80, 99, 100, is_symmetric=True)
    goalCalculatorTest(invert, 2, 6, 100, is_symmetric=False)
    goalCalculatorTest(invert, 0, 20, 100, is_symmetric=False)
    goalCalculatorTest(invert, 80, 99, 100, is_symmetric=False)
    goalCalculatorTest(invert, 80, 81, 100, is_symmetric=False)
    goalCalculatorTest(swap, 80, 81, 100, is_symmetric=False)
    goalCalculatorTest(swap, 2, 6, 100, is_symmetric=False)
    goalCalculatorTest(swap, 0, 20, 100, is_symmetric=False)
    goalCalculatorTest(swap, 80, 99, 100, is_symmetric=False)
    goalCalculatorTest(invert, 2, 9, 100, is_symmetric=True, TIMES=100000, should_print=True)
    goalCalculatorTest(swap, 2, 20, 100, is_symmetric=True, TIMES=100000, should_print=True)
    goalCalculatorTest(invert, 10, 15, 100, is_symmetric=False, TIMES=100000, should_print=True)
    goalCalculatorTest(swap, 30, 40, 100, is_symmetric=False, TIMES=100000, should_print=True)



if __name__ == "__main__":
    #goalCalculatorTests()
    main()
