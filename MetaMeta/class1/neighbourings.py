import numpy as np


def possible_i_j(solution: np.array) -> list:
    result = list()
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            result.append((i, j))
    return result


def invert(solution: np.array, i: int, j: int) -> np.array:
    neighbour = np.concatenate((solution[:i], solution[i:j + 1][::-1], solution[j + 1:]))
    return neighbour


def swap(solution: np.array, i: int, j: int) -> np.array:
    new_solution = solution.copy()
    temp = new_solution[i]
    new_solution[i] = new_solution[j]
    new_solution[j] = temp
    return new_solution


def main():
    for i in invert([1, 2, 3, 4, 5]):
        print(i)
    for i in swap([1, 2, 3, 4, 5]):
        print(i)


if __name__ == "__main__":
    main()
