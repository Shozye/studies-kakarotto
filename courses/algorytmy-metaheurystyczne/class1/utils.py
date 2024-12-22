import math


def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def calculate_goal(path):
    goal = 0
    for i in range(len(path) - 1):
        goal += dist(*path[i][1], *path[i + 1][1])
    return goal
