def invert(solution: list):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbours.append(solution[:i] + solution[i:j + 1][::-1] + solution[j + 1:])
    return neighbours


def swap(solution: list):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            new_solution = solution.copy()
            temp = new_solution[i]
            new_solution[i] = new_solution[j]
            new_solution[j] = temp
            neighbours.append(new_solution)
    return neighbours


if __name__ == "__main__":
    print(invert([1, 2, 3, 4, 5]))
    print(swap([1, 2, 3, 4, 5]))
