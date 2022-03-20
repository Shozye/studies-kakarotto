def invert(solution: list):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbours.append(solution[:i] + solution[i:j + 1][::-1] + solution[j + 1:])
    return neighbours


if __name__ == "__main__":
    print(invert([1, 2, 3, 4]))
