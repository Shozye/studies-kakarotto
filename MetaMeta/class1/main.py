from GoalFunctionCalculator import GoalFunctionCalculator
import numpy as np


def get_random_permutation(max_incl: int) -> list:
    return list(map(lambda x: x + 1, list(np.random.permutation(max_incl))))


def main():
    filename = "bays29/bays29.tsp"
    solution = GoalFunctionCalculator(filename)
    print(solution.calculate_goal_function([1, 2, 3]))
    random_permutation = get_random_permutation(29)
    print(solution.calculate_goal_function(random_permutation))

    probably_optimal = [1, 28, 6, 12, 9, 5, 26, 29, 3, 2, 20, 10, 4, 15, 18, 17, 14, 22, 11, 19, 25, 7, 23, 27, 8, 24, 16, 13, 21]
    print(solution.calculate_goal_function(probably_optimal))


if __name__ == "__main__":
    main()
