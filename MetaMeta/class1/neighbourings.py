import numpy as np

def invert(solution: np.array) -> np.array:
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = np.concatenate((solution[:i], solution[i:j + 1][::-1], solution[j + 1:]))
            yield neighbour


def swap(solution: np.array) -> np.array:
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            new_solution = solution.copy()
            temp = new_solution[i]
            new_solution[i] = new_solution[j]
            new_solution[j] = temp
            yield new_solution


def main():
    for i in invert([1, 2, 3, 4, 5]):
        print(i)
    for i in swap([1, 2, 3, 4, 5]):
        print(i)


if __name__ == "__main__":
    main()
