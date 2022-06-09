import tsplib95
from FileGenerator import FileGenerator
from TSPAlgorithms import TSPAlgorithms
import networkx as nx
from matplotlib import pyplot as plt
import os
from DataHandler import DataHandler

PLOT_DIR = os.path.join(os.getcwd(), "aco_plots")


def draw_path(path, cost, problem: tsplib95.models.StandardProblem, name: str):
    graph = problem.get_graph()
    pos = dict()
    for key in (problem.node_coords.keys()):
        pos[int(key)] = tuple(problem.node_coords[key])
    if name == "ant_colony":
        path = [int(x) for x in path][:-1]

    if name == "two_opt":
        edges = [(path[i]+1, path[i + 1]+1) for i in range(len(path) - 1)]
        edges.append((path[len(path) - 1]+1, path[0]+1))
    else:
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        edges.append((path[len(path) - 1], path[0]))


    plt.title(f"algo_name={name} Cost: {cost}")
    nx.draw(graph, pos=pos, node_size=300, node_color="#ADD8E6", edgelist=edges, with_labels=True)
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_DIR, f"path_drawn_{name}.png"))
    plt.clf()

"""
for algorithm in algorithms_and_parameters:
    algo, parameter_list, ax = algorithm
    ax: plt.Axes
    function_label = f"{algo.__name__}({', '.join(list(map(str, parameter_list)))})"
    time_before = time.time()
    cost = algo(*parameter_list)
    time_after = time.time()
    print(
        f"{function_label} = {cost}, took {round(time_after - time_before, 2)} seconds")  # func(*params) = func(params[0], params[1],...,params[k])
    solution = algos.last_solution
    if verbose:
        print(f"Solution:", algos.last_solution)
        if data.isEuc2D():
            edges = [(solution[i], solution[i + 1]) for i in range(len(solution) - 1)]
            edges.append((solution[len(solution) - 1], solution[0]))
            nx.draw(data.getGraph(), ax=ax, pos=data.getPos(), with_labels=True, node_size=300, node_color="#ADD8E6")
            nx.draw_networkx_edges(data.getGraph(), pos=data.getPos(), ax=ax, edgelist=edges, width=2)
            ax.title.set_text(function_label + f"\n cost={algos.last_cost}")
if verbose and data.isEuc2D():
    fig.suptitle(f"Wykres algorytmów dla instancji {data.name}", fontsize=16)
    plt.tight_layout()
    plt.show()
"""

if __name__ == "__main__":
    berlin_path = "/home/shozy/PycharmProjects/studies-kakarotto/MetaMeta/class1/tsplib_problems/berlin52/berlin52.tsp"
    problem = tsplib95.load(berlin_path)
    problem: tsplib95.models.StandardProblem

    algos = TSPAlgorithms(problem)
    algos.ant_colony(time=1800, decay_power=1)

    draw_path(algos.last_solution, algos.last_cost, problem, "ant_colony")

    dataHandler = DataHandler(berlin_path)
    algos = TSPAlgorithms(dataHandler)
    algos.two_opt()
    draw_path(algos.last_solution, algos.last_cost, problem, "two_opt")
    eil_optimal = [1, 22, 8, 26, 31, 28, 3, 36, 35, 20, 2, 29, 21, 16, 50, 34, 30, 9, 49, 10, 39, 33, 45, 15, 44, 42, 40, 19, 41, 13, 25, 14, 24, 43, 7, 23, 48, 6, 27, 51, 46, 12, 47, 18, 4, 17, 37, 5, 38, 11, 32]
    eil_val = 326
    berlin_optimal = [1, 49, 32, 45, 19, 41, 8, 9, 10, 43, 33, 51, 11, 52, 14, 13, 47, 26, 27, 28, 12, 25, 4, 6, 15, 5, 24, 48, 38, 37, 40, 39, 36, 35, 34, 44, 46, 16, 29, 50, 20, 23, 30, 2, 7, 42, 21, 17, 3, 18, 31, 22]
    berlin_val = 7542
    draw_path(berlin_optimal, berlin_val, problem, "optimal")
