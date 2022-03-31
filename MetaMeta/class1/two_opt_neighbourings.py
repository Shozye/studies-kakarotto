from numba import jit
import numpy as np


def invert(solution: np.array):
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution[:i] + solution[i:j + 1][::-1] + solution[j + 1:]
            yield neighbour


def swap(solution: np.array):
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            new_solution = solution.copy()
            temp = new_solution[i]
            new_solution[i] = new_solution[j]
            new_solution[j] = temp
            yield new_solution


if __name__ == "__main__":
    print(invert([1, 2, 3, 4, 5]))
    for i in swap([1, 2, 3, 4, 5]):
        print(i)
