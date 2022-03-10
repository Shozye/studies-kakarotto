import tsplib95


class GoalFunctionCalculator:
    def __init__(self, filename: str):
        self.__file = tsplib95.read(open(filename))

    def getLength(self, node1: int, node2: int) -> int:
        return self.__file.edge_weights[node1 - 1][node2 - 1]

    def getListLength(self, nodes: list) -> int:
        result = 0
        for index in range(len(nodes) - 1):
            result += self.getLength(nodes[index], nodes[index + 1])
        return result

    def calculate_goal_function(self, nodes: list):
        copied_list = nodes.copy()
        copied_list.append(copied_list[0])
        return self.getListLength(copied_list)
