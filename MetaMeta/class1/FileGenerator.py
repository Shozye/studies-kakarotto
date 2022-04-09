import sys
import os
import shutil
import tsplib95.models
import numpy as np
import math
from utils import dist


class FileGenerator:
    """
    Klasa do generowania losowych plikow. Obecnie do dyspozycji są:
    Macierzowe symetryczne i asymetryczne
    Euklidesowe + Macierzowe Symetryczne
    Tylko Euklidesowe dostają "moc" rysowania
    """
    DATASET_DIR_NAME = "datasets"

    def __init__(self):
        self.last_path = None

    def create_symmetric_matrix_dataset(self, name: str, dimension: int, max_num=1000):
        matrix = np.random.randint(0, max_num + 1, (dimension, dimension))
        for i in range(dimension):
            matrix[i][i] = 0
        for row in range(dimension):
            for col in range(row + 1, dimension):
                matrix[col][row] = matrix[row][col]
        self.__create_matrix_dataset(name, list(matrix))

    def create_asymmetric_matrix_dataset(self, name: str, dimension: int, max_num=1000):
        matrix = np.random.randint(0, max_num + 1, (dimension, dimension))
        for i in range(dimension):
            matrix[i][i] = 0
        self.__create_matrix_dataset(name, list(matrix), file_suffix=".atsp")

    def __create_matrix_dataset(self, name, full_matrix: list, file_suffix=".tsp"):
        self.create_dataset_directory()
        dimension = len(full_matrix)
        fullname = f"{name}{dimension}"
        if fullname in os.listdir(os.path.join(os.getcwd(), self.DATASET_DIR_NAME)):
            print(f"{fullname} file already in datasets. Choose different name")
            sys.exit(1)
        os.mkdir(os.path.join(os.getcwd(), self.DATASET_DIR_NAME, fullname))

        problem = tsplib95.models.StandardProblem.parse("")
        problem.dimension = dimension
        problem.name = fullname
        problem.type = "TSP"
        problem.comment = f"{dimension} nodes randomly generated by FileGenerator.py ~ Mateusz Pelechaty 2022"
        problem.edge_weight_type = "EXPLICIT"
        problem.edge_weight_format = "FULL_MATRIX"
        problem.display_data_type = "TWOD_DISPLAY"
        problem.edge_weights = full_matrix
        self.last_path = os.path.join(os.getcwd(), self.DATASET_DIR_NAME, fullname, f"{fullname}{file_suffix}")
        problem.save(self.last_path)
        with open(self.last_path, 'a+') as file:
            file.write("\n")

    def create_dataset_directory(self):
        if self.DATASET_DIR_NAME not in os.listdir(os.getcwd()):
            os.mkdir(self.DATASET_DIR_NAME)

    def rm_dataset_directory(self):
        if self.DATASET_DIR_NAME in os.listdir(os.getcwd()):
            shutil.rmtree(self.DATASET_DIR_NAME)

    def create_symmetric_EUC2D_dataset(self, name: str, dimension: int):
        points = []
        for node_id in range(dimension):
            not_added = True
            while not_added:
                p1 = np.random.random(2) * 100
                fit = True
                for p2 in points:
                    if dist(*p1, *p2) < 2:  # THIS PART MAY NEED REFACTOR.
                        fit = False
                if fit:
                    points.append(p1)
                    not_added = False
        node_coords = dict(zip(range(dimension), points))
        matrix = np.zeros((dimension, dimension))
        for row in range(dimension):
            for col in range(dimension):
                distance = dist(*node_coords[row], *node_coords[col])
                matrix[row][col] = distance
                matrix[col][row] = distance
        self.__create_EUC2D_dataset(name, node_coords, matrix)

    def __create_EUC2D_dataset(self, name, node_coords: dict, edge_weights: np.array):
        self.create_dataset_directory()
        dimension = len(node_coords.keys())
        fullname = f"{name}{dimension}"
        if fullname in os.listdir(os.path.join(os.getcwd(), self.DATASET_DIR_NAME)):
            print(f"{fullname} file already in datasets. Choose different name")
            sys.exit(1)
        os.mkdir(os.path.join(os.getcwd(), self.DATASET_DIR_NAME, fullname))

        problem = tsplib95.models.StandardProblem.parse("")
        problem.dimension = dimension
        problem.name = fullname
        problem.type = "TSP"
        problem.edge_weight_type = "EUC_2D"
        problem.comment = f"{dimension} nodes randomly generated by FileGenerator.py ~ Mateusz Pelechaty 2022"
        problem.node_coords = node_coords
        problem.edge_weights = edge_weights
        self.last_path = os.path.join(os.getcwd(), self.DATASET_DIR_NAME, fullname, f"{fullname}.tsp")
        problem.save(self.last_path)
        with open(self.last_path, 'a+') as file:
            file.write("\n")


if __name__ == "__main__":
    generator = FileGenerator()
    generator.rm_dataset_directory()
    generator.create_symmetric_EUC2D_dataset("GANGI", 20)
