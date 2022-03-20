from TSPAlgorithms import TSPAlgorithms
from DataHandler import DataHandler
import json
import tsplib95
import matplotlib.pyplot as plt
import networkx as nx


def main():
    filename = "bays29/bays29.tsp"
    # draw_graph(filename)

    algos = TSPAlgorithms(filename)

    # print(algos.k_random(10000))
    # print(algos.closest_neighbour())
    # print(algos.closest_neighbour_extended())
    AMOUNT = 100
    two_opt_answers = []
    for i in range(AMOUNT):
        if i % (AMOUNT//10) == 0:
            print(f"Done {(i/AMOUNT)*100}%")
        two_opt_answers.append(algos.two_opt())
    print(sorted(two_opt_answers, key=lambda x: x[1]))

    # test_hardcoded_solutions(
    #    [23, 27, 24, 8, 1, 28, 6, 12, 9, 5, 26, 29, 3, 2, 21, 20, 10, 4, 15, 18, 14, 22, 17, 11, 19, 16, 13, 25, 7],
    #    filename)


def test_hardcoded_solutions(solution: list, filename: str):
    data = DataHandler(filename)
    print(f"Weight of {json.dumps(solution)} is {data.calculate_goal(solution)}")


def draw_graph(filename: str):
    with open(filename) as file:
        graph = tsplib95.read(file).get_graph()
        nx.draw_shell(graph)
    plt.show()


if __name__ == "__main__":
    main()
