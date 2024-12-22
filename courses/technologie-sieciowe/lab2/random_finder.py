import networkx as nx
from copy import deepcopy
from graph_creator import *
import time


def create_better_topology(vector_amount=20, edge_amount_begin=29):
    is_topology_better = False
    graph = None
    while not is_topology_better:
        graph = create_random_topology(vector_amount=vector_amount, edge_amount_begin=edge_amount_begin)
        bad = False
        for node in graph.nodes():
            if len(list(graph.adj[node].keys())) < 2 or len(list(graph.adj[node].keys())) > 3:
                bad = True
                break
        if not bad:
            is_topology_better = True
    return graph


def test_topology(graph: nx.Graph, repetitions=100, k=0.95, vector_amount=20):
    how_many_times_until_stop = []
    edges = deepcopy(graph.edges())
    for _ in range(repetitions):
        N = create_random_intensity(vector_amount=vector_amount)
        calculateA(graph, N)
        setC(graph)
        alive = 0
        degrade(graph, k=k)
        while fine(graph):
            alive += 1
            calculateA(graph, N)
            degrade(graph, k=k)
        how_many_times_until_stop.append(alive)
        for edge in edges:
            graph.add_edge(edge[0], edge[1])
    return sum(how_many_times_until_stop) / len(how_many_times_until_stop)


def find_best_topology_k_random_random(k: int, vector_amount=20, edge_amount=29):
    best_graph = None
    best_index = 0
    best_resistance = 0
    best_time = 0
    for i in range(k):
        if i in [x * k // 10 for x in range(10)]:
            print(f"I am on i={i}")
        graph = create_random_topology(vector_amount=20, edge_amount_begin=edge_amount)
        save(f"Tests_TotallyRandom_{i}", graph)
        start = time.time()
        resistance = test_topology(graph, repetitions=5, k=0.95, vector_amount=vector_amount)
        # print(f"k={i}, Test topology took {round(time.time() - start, 2)}")
        if resistance > best_resistance:
            best_graph = graph
            best_resistance = resistance
            best_index = i
            best_time = time.time() - start
    print(f"Best resistance {best_resistance} was acquired by index={best_index}, time={best_time}")
    draw(best_graph, check_overload=False)


def find_best_topology_k_random_better(k: int, vector_amount=20, edge_amount=29):
    best_graph = None
    best_index = 0
    best_resistance = 0
    best_time = 0
    for i in range(k):
        if i in [x * k // 10 for x in range(10)]:
            print(f"I am on i={i}")
        graph = create_better_topology(vector_amount=20, edge_amount_begin=edge_amount)
        save(f"TestsMin2EdgesMax3Edges_{i}", graph)
        start = time.time()
        resistance = test_topology(graph, repetitions=5, k=0.95, vector_amount=vector_amount)
        # print(f"k={i}, Test topology took {round(time.time() - start, 2)}")
        if resistance > best_resistance:
            best_graph = graph
            best_resistance = resistance
            best_index = i
            best_time = time.time() - start
    print(f"Best resistance {best_resistance} was acquired by index={best_index}, time={best_time}")
    draw(best_graph, check_overload=False)


def find_best_topology_k_random_good(k: int, vector_amount=20, edge_amount=29):
    best_graph = None
    best_index = 0
    best_resistance = 0
    best_time = 0
    for i in range(k):
        if i in [x * k // 10 for x in range(10)]:
            print(f"I am on i={i}")
        graph = create_good_topology(vector_amount=20, edge_amount_begin=edge_amount)
        save(f"TestsGoodTopology_{i}", graph)
        start = time.time()
        resistance = test_topology(graph, repetitions=10, k=0.95, vector_amount=vector_amount)
        if resistance > best_resistance:
            best_graph = graph
            best_resistance = resistance
            best_index = i
            best_time = time.time() - start
    print(f"Best resistance {best_resistance} was acquired by index={best_index}, time={best_time}")
    draw(best_graph, check_overload=False)


def main():
    start_time = time.time()
    find_best_topology_k_random_good(100)
    print(time.time() - start_time)


if __name__ == "__main__":
    main()
