import numpy as np
def get_random_except(low, high, without: int):
    if without == low:
        return np.random.randint(low+1, high)
    if without == high-1:
        return np.random.randint(low, high-1)
    amount = [np.random.randint(low, without),
              np.random.randint(without+1, high)]
    return amount[np.random.randint(0,2)]

if __name__ == "__main__":
    for _ in range(50):
        print(get_random_except(0, 3, 1))