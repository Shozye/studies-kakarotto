import random

import numpy as np
from itertools import product
import networkx as nx
import matplotlib.pyplot as plt
import json
import math
import random

from TechSieciowe.lab2.utils import get_random_except


def create_random_topology(vector_amount=20, edge_amount_begin=29):
    done = False
    while not done:
        edge_amount = edge_amount_begin
        adjacency_matrix = np.zeros((vector_amount, vector_amount))
        for row in range(vector_amount):
            if 1 in adjacency_matrix[row]:
                continue
            col = get_random_except(0, vector_amount, row)
            if adjacency_matrix[row][col] == 0:
                adjacency_matrix[row][col] = 1
                adjacency_matrix[col][row] = 1
                edge_amount -= 1
        while edge_amount != 0:
            row = np.random.randint(0, vector_amount)
            col = np.random.randint(0, vector_amount)
            if row == col:
                continue
            if adjacency_matrix[row][col] == 0:
                adjacency_matrix[row][col] = 1
                adjacency_matrix[col][row] = 1
                edge_amount -= 1
        wrong = False
        for i in range(vector_amount):
            i_exists = False
            for j in range(vector_amount):
                if adjacency_matrix[i][j] == 1:
                    i_exists = True
            if not i_exists:
                wrong = True
                break
        if wrong:
            continue
        rows, cols = np.where(adjacency_matrix == 1)
        edges = zip(rows.tolist(), cols.tolist())
        gr = nx.Graph()
        gr.add_edges_from(edges)
        if not fine(gr, check_overload=False):
            continue
        return gr


def create_good_topology(vector_amount=20, edge_amount_begin=29):
    edge_amount = edge_amount_begin
    adjacency_matrix = np.zeros((vector_amount, vector_amount))
    for times in range(1, 4):
        for row in range(vector_amount):
            if times - sum(adjacency_matrix[row]) > 0 and edge_amount >= 0:
                sample = random.sample(range(0, 20), 4)
                np.random.shuffle(sample)
                to_add_connection = 0
                for possible in sample:
                    if possible != row and adjacency_matrix[row][possible] != 1:
                        to_add_connection = possible
                        break
                edge_amount -= 1
                adjacency_matrix[row][to_add_connection] = 1
                adjacency_matrix[to_add_connection][row] = 1
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    if not fine(gr, check_overload=False):
        print("Generated not fine")
    return gr


def create_line_topology(vector_amount=20):
    gr = nx.Graph()
    gr.add_nodes_from(list(range(vector_amount)))
    for i in range(19):
        gr.add_edge(i, i + 1)
    return gr


def create_circular_topology(vector_amount=20):
    gr = nx.Graph()
    gr.add_nodes_from(list(range(vector_amount)))
    for i in range(vector_amount):
        gr.add_edge(i, (i + 1) % vector_amount)
    return gr


def create_upgraded_circular_topology(vector_amount=20, edge_amount=29):
    gr = nx.Graph()
    gr.add_nodes_from(list(range(vector_amount)))
    for i in range(vector_amount):
        gr.add_edge(i, (i + 1) % vector_amount)
        edge_amount -= 1
    nodes = list(gr.nodes())
    np.random.shuffle(nodes)
    for node in nodes:
        if (node, (node + vector_amount // 2) % vector_amount) not in gr.edges() and edge_amount > 0:
            gr.add_edge(node, (node + vector_amount // 2) % vector_amount)
            edge_amount -= 1
    return gr

def create_double_circular_topology_for_20_29():
    VECTOR_AMOUNT=20
    gr = nx.Graph()
    gr.add_nodes_from(list(range(VECTOR_AMOUNT)))
    for i in range(9):
        gr.add_edge(i, i+1)
    gr.add_edge(9, 0)
    for i in range(10, 19):
        gr.add_edge(i, i+1)
    gr.add_edge(19, 10)
    for i in range(9):
        gr.add_edge(i, i+10)
    return gr

def create_random_intensity(vector_amount=20, low=1, high=20):
    N = np.random.randint(low, high, size=(vector_amount, vector_amount))
    for i in range(vector_amount):
        N[i][i] = 0
    return N


def draw(gr: nx.Graph, check_overload=True, circular=False):
    node_color = []
    subgraphs = [gr.subgraph(c) for c in nx.connected_components(gr)]
    for node in gr.nodes():
        if check_overload:
            added = False
            for adjacent in gr.adj[node]:
                if gr[node][adjacent]['a'] > gr[node][adjacent]['c']:
                    node_color.append('purple')
                    added = True
                    break
            if added:
                continue
        if node in subgraphs[0]:
            node_color.append('blue')
        else:
            node_color.append('red')
    if circular:
        pos = nx.circular_layout(gr)
    else:
        pos = nx.nx_pydot.graphviz_layout(gr, prog='neato')
    nx.draw(gr, pos=pos, node_size=500, with_labels=True, node_color=node_color)
    plt.show()



def draw_with_flow(gr: nx.Graph):
    labels = nx.get_edge_attributes(gr, 'a')
    pos = nx.nx_pydot.graphviz_layout(gr, prog='neato')
    nx.draw(gr, pos, with_labels=True, node_size=500)
    nx.draw_networkx_edge_labels(gr, pos=pos, edge_labels=labels)
    plt.show()


def get_color(num: float):
    black = "#000000"
    blue = "#0000FF"
    colors = ["#006401", "#69B34C", "#ACB334", "#FAB733", "#FF8E15", "#FF4E11", "#FF0D0D"]
    biases = [0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
    if num > 1:
        return black
    elif num < 0:
        return blue
    for i in range(len(biases)):
        if num < biases[i]:
            return colors[i]
    return colors[-1]


def draw_with_flow_capacity(gr: nx.Graph):
    labels = nx.get_edge_attributes(gr, 'a')
    pos = nx.nx_pydot.graphviz_layout(gr, prog='neato')
    edges = gr.edges()
    colors = []
    widths = []
    max_capacity = 0
    for edge in edges:
        filled = gr[edge[0]][edge[1]]['a'] / gr[edge[0]][edge[1]]['c']
        colors.append(get_color(filled))
    for edge in edges:
        if gr[edge[0]][edge[1]]['c'] > max_capacity:
            max_capacity = gr[edge[0]][edge[1]]['c']
    for edge in edges:
        width = gr[edge[0]][edge[1]]['c'] / max_capacity * 5
        widths.append(width)
    nx.draw(gr, pos, with_labels=True, edge_color=colors, node_size=500, width=widths)
    nx.draw_networkx_edge_labels(gr, pos=pos, edge_labels=labels)
    plt.show()


def save(filename, graph):
    with open(f"graphs/{filename}", 'w+') as file:
        file.write(json.dumps(nx.readwrite.node_link_data(graph)))


def load(filename):
    with open(f"graphs/{filename}", 'r') as file:
        data = nx.readwrite.node_link_graph(json.loads(file.read()))
        return data

def load_from_saved(filename):
    with open(f"saved_graphs/{filename}", 'r') as file:
        data = nx.readwrite.node_link_graph(json.loads(file.read()))
        return data

def bfs(graph: nx.Graph, node1, node2) -> list:
    visited = [node1]
    parents = {node1: None}
    queue = [node1]
    while len(queue) != 0:
        node = queue.pop(0)
        adjacents = list(graph.adj[node].keys())
        for adjacent in adjacents:
            if adjacent not in visited:
                queue.append(adjacent)
                visited.append(adjacent)
                parents[adjacent] = node
    path = []
    node = node2
    plt.show()
    while node != node1:
        path.append((parents[node], node))
        node = parents[node]
    return path


def calculateA(graph: nx.Graph, intensity_matrix, path_algorithm=bfs):
    for row, col in graph.edges:
        graph[row][col]['a'] = 0
    rows, cols = np.where(intensity_matrix != 0)
    goals = zip(rows, cols)
    for node1, node2 in goals:
        path = path_algorithm(graph, node1, node2)
        for edge in path:
            graph[edge[0]][edge[1]]['a'] += intensity_matrix[node1][node2]


def setC(graph: nx.Graph):
    for row, col in graph.edges:
        a = graph[row][col]['a']
        graph[row][col]['c'] = a * 2 + 100


def degrade(graph: nx.Graph, k=0.95):
    to_delete = []
    for edge in graph.edges:
        delete = np.random.random() > k
        if delete: to_delete.append(edge)
    for edge in to_delete:
        graph.remove_edge(edge[0], edge[1])


def fine(graph: nx.Graph, vector_amount=20, check_overload=True):
    nodes = graph.nodes()
    for node in range(vector_amount):
        if node not in nodes:
            return False
    if not nx.is_connected(graph):
        return False
    if check_overload:
        for edge in graph.edges():
            if graph[edge[0]][edge[1]]['a'] > graph[edge[0]][edge[1]]['c']:
                return False
    return True


def main():
    VECTOR_AMOUNT = 20
    EDGE_AMOUNT = 29
    graph = create_circular_topology(vector_amount=VECTOR_AMOUNT)
    draw(graph, check_overload=False)
    save("circular.json", graph)
    graph = create_line_topology(VECTOR_AMOUNT)
    draw(graph, check_overload=False)
    save("line.json", graph)
    graph = create_upgraded_circular_topology(VECTOR_AMOUNT, EDGE_AMOUNT)
    draw(graph, check_overload=False, circular=True)
    save("upgraded_circular_topology.json", graph)
    graph = create_double_circular_topology_for_20_29()
    draw(graph, check_overload=False)
    save("double_circular.json", graph)

if __name__ == "__main__":
    main()
