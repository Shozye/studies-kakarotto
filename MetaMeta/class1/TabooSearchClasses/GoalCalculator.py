import time

from MetaMeta.class1.DataHandler import DataHandler
import numpy as np

import sys

from MetaMeta.class1.neighbourings import *


class GoalCalculator:
    """Class responsible for calculating goal function.
    It's main goal is to add acceleration feature
    """

    def __init__(self, dataHandler: DataHandler):
        self.dataHandler = dataHandler

        self.__main_solution: np.array
        self.__cumulative_goal_function: np.array

        self.__main_solution = None
        self.__cumulative_goal_function = None
        self.__neighboring_function = None  # invert / swap / ?

    def __call__(self, solution, i: int, j: int) -> float:
        return self.goal(solution, i, j)

    def set_main_solution(self, solution: np.array):
        """Sets solution used for acceleration purposes"""
        self.__main_solution = solution
        self.calculate_cumulative_goal_function()

    def set_neighboring_function(self, neighboring_function: str):
        """Sets neighboring function for acceleration purposes"""
        self.__neighboring_function = neighboring_function

    def calculate_cumulative_goal_function(self):
        """Calculates cumulative goal function for acceleration purposes"""
        if self.__main_solution is None:
            raise Exception("main solution is not specified. "
                            "Use GoalCalculator.set_main_solution first")
        goal = 0
        cumulative_goal_function = [0]
        for i in range(1, len(self.__main_solution)):
            node1 = self.__main_solution[i - 1]
            node2 = self.__main_solution[i]
            goal += self.dataHandler.getCost(node1, node2)
            cumulative_goal_function.append(goal)
        self.__cumulative_goal_function = cumulative_goal_function

    def basic_goal(self, solution: np.array) -> float:
        """Function that has got normal goal functionality"""
        return sum([self.dataHandler.getCost(solution[index], solution[index + 1]) for index in
                    range(len(solution) - 1)]) + self.dataHandler.getCost(solution[-1], solution[0])

    def goal(self, solution: np.array, i: int, j: int) -> float:
        """Function that will try to use acceleration if possible else basic_goal"""
        if not self.__should_use_acceleration():
            return self.basic_goal(solution)
        if self.__neighboring_function == "invert":
            return self.__invert_accelerate_goal(solution, i, j)
        if self.__neighboring_function == "swap":
            return self.__swap_accelerate_goal(solution, i, j)
        return self.basic_goal(solution)

    def __invert_accelerate_goal(self, solution: np.array, i: int, j: int) -> float:
        """Function to calculate acceleration for invert"""
        length = len(solution)
        res = 0
        if i != 0:
            res += self.__cumulative_goal_function[i - 1]  # left side
            res += self.dataHandler.getCost(solution[i - 1], solution[i])  # change left
        if j != length - 1:
            res += self.dataHandler.getCost(solution[j], solution[j + 1])  # change right
            res += self.__cumulative_goal_function[length - 1] - self.__cumulative_goal_function[j + 1]  # right side
        res += self.dataHandler.getCost(solution[length - 1], solution[0])  # end to first
        if self.dataHandler.is_symmetric():
            res += self.__cumulative_goal_function[j] - self.__cumulative_goal_function[i]  # middle
        else:
            for index in range(i, j): # middle
                res += self.dataHandler.getCost(solution[index], solution[index + 1])
        return res

    def __swap_accelerate_goal(self, solution: np.array, i: int, j: int) -> float:
        """Function to calculate acceleration for swap"""
        length = len(solution)
        res = 0
        if i != 0:
            res += self.__cumulative_goal_function[i - 1]  # left side
            res += self.dataHandler.getCost(solution[i - 1], solution[i])  # change left
        if j != length - 1:
            res += self.dataHandler.getCost(solution[j], solution[j + 1])  # change right
            res += self.__cumulative_goal_function[length - 1] - self.__cumulative_goal_function[j + 1]  # right side
        if j - i == 1:
            res += self.dataHandler.getCost(solution[i], solution[j]) # middle
        else:
            res += self.dataHandler.getCost(solution[i], solution[i+1]) # middle left
            res += self.dataHandler.getCost(solution[j-1], solution[j]) # middle right
            res += self.__cumulative_goal_function[j-1] - self.__cumulative_goal_function[i+1] # middle proper
        res += self.dataHandler.getCost(solution[length - 1], solution[0])  # end to first
        return res

    def __should_use_acceleration(self) -> bool:
        return self.__main_solution is not None \
               and self.__cumulative_goal_function is not None \
               and self.__neighboring_function in ["invert", "swap"]
