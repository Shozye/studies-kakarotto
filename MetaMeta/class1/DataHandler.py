import tsplib95


class DataHandler:
    def __init__(self, filename: str):
        self.__problem = tsplib95.read(open(filename))

    def getWeight(self, node1: int, node2: int) -> int:
        """
        :param node1: integer
        :param node2: integer
        :return: weight of edge from node1 to node2
        """
        print((node1, node2))
        return self.__problem.get_weight(*(node1, node2))

    def getListWeight(self, nodes: list) -> int:
        """Function to calculate sum of weights in list between all list members in order
        :param nodes: list of integers
        :return: sum of weights
        """
        return sum([self.getWeight(nodes[index], nodes[index + 1]) for index in range(len(nodes)-1)])

    def goal(self, nodes: list):
        """Function that calculates goal function of certain list. It calculates list weight adding first element to end
        :param nodes: list of nodes
        :return: goal function
        """
        return self.getListWeight(nodes) + self.getWeight(nodes[-1], nodes[0])

    def dimension(self):
        """:return: Amount of Nodes in problem """
        return self.__problem.dimension

    def get_closest_neighbour_of_all(self, node):
        """ Function to get the closest neighbour of all other nodes
        :param node: node of which we want closest neigbour
        :return: closest neighbour
        """
        all_nodes = list(range(self.dimension()))
        all_nodes.remove(node)
        return self.get_closest_neighbour(node, all_nodes)

    def get_closest_neighbour(self, node, neighbours):
        """ Function to get the closest neighbour from list of neighbours
        :param node: node of which we want closest neighbour
        :param neighbours: List of neighbours to take under consideration
        :return: list of node id and weight
        """
        lengths = list(map(lambda x: [x, self.getWeight(node, x)], neighbours))
        return min(lengths, key=lambda x: x[1])

