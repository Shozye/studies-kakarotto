import numpy as np


def get_random_permutation(max_incl: int) -> list:
    return list(map(lambda x: x + 1, list(np.random.permutation(max_incl))))