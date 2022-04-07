import tsplib95
import numpy as np
import json

class DataHandler:
    def __init__(self, filename: str):
        self.__problem = tsplib95.read(open(filename))

    def dimension(self):
        """:return: Amount of Nodes in problem """
        return self.__problem.dimension

    def get_edge_weights(self):
        return self.__problem.edge_weights
