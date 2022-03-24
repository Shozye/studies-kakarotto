import numpy as np


def get_random_solution(max_incl: int) -> list:
    return list(np.random.permutation(max_incl))
