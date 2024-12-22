import networkx as nx
import tsplib95
import numpy as np
import json
import sys
import math


class DataHandler:
    """
    Klasa zajmujaca sie otwieraniem pliku i portowaniem informacji dla innych algorytmow
    To stad uzywamy funkcje cost i dimension i ogolnie zbieramy dane z problemu.
    Jak cos jest potrzebne z problemu czy z pliku to powinno byc w tej klasie.
    """
    __problem: tsplib95.models.StandardProblem

    def __init__(self, filename: str):
        self.__problem = tsplib95.read(open(filename))
        self.edge_weights = None
        self.node_coords = None
        self.name = self.__problem.name
        self.dimension = self.__problem.dimension
        self.__setup()

    def isEuc2D(self):
        return self.node_coords is not None

    def __setup(self):
        if self.__problem.edge_weight_type == "FULL_MATRIX" or (self.__problem.edge_weight_type == "EXPLICIT" and self.__problem.edge_weight_format == "FULL_MATRIX"):
            # Full matrix has got edge weights. So i am porting it to my class
            self.edge_weights = self.__problem.edge_weights
        elif self.__problem.edge_weight_type in ["EUC_2D", "GEO", "ATT"]:
            # EUC 2D may have got node_coords starting by 1. I am negating it to start by 0
            if self.__problem.node_coords.get(0) is None:
                self.node_coords = dict()
                for key, value in self.__problem.node_coords.items():
                    self.node_coords[key - 1] = value
            else:
                self.node_coords = self.__problem.node_coords
            # EUC 2D may or may not have edge_weights. I am assuring it has, because my weight functions functions on it.
            # Have in mind that edge_weights of 100x100 is 10 000 elements. But we are unable to store files with more than 1 000 000 elems.
            if len(self.__problem.edge_weights) != 0:
                self.edge_weights = self.__problem.edge_weights
            else:
                matrix = np.zeros((self.dimension, self.dimension))
                for row in range(self.dimension):
                    for col in range(self.dimension):
                        p1 = self.node_coords[row]
                        p2 = self.node_coords[col]
                        distance = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
                        matrix[row][col] = distance
                        matrix[col][row] = distance
                self.edge_weights = matrix
        else:
            print(f"UNIDENTIFIED EDGE WEIGHT TYPE {self.__problem.edge_weight_type}")
            sys.exit(1)

    def getCost(self, node1: int, node2: int) -> int:
        return self.edge_weights[node1][node2]

    def cost(self, nodes: np.array) -> int:
        return sum([self.getCost(nodes[index], nodes[index + 1]) for index in range(len(nodes) - 1)]) + self.getCost(
            nodes[-1], nodes[0])

    def getGraph(self) -> nx.Graph:
        graph = nx.Graph()
        for node_id in self.node_coords.keys():
            graph.add_node(node_id)
        return graph

    def getPos(self) -> dict:
        return self.node_coords

    def is_symmetric(self) -> bool:
        return "[symmetric]" in self.__problem.comment or self.__problem.is_symmetric()
