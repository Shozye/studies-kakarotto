import numpy as np
import tsplib95
from TSPAlgorithms import TSPAlgorithms
import time
from two_opt_neighbourings import *


def get_best_solution(problem: tsplib95.models.StandardProblem) -> int:
    algos = TSPAlgorithms(problem)
    min_value = algos.repetitive_closest_neighbour()[1]
    tested_algos = [algos.two_opt, algos.two_opt, algos.k_random]
    tested_algos_arguments = [invert, swap, 10000]
    algos_time = [5, 5, 2]
    for algo, arg, algo_time in zip(tested_algos, tested_algos_arguments, algos_time):
        time_now = time.time()
        time_passed = False
        while not time_passed:
            found_value_of_solution = algo(arg)[1]
            min_value = min(min_value, found_value_of_solution)
            if time.time() - time_now > algo_time:
                time_passed = True
    return min_value
