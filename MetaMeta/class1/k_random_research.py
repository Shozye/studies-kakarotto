from TSPAlgorithms import TSPAlgorithms
import tsplib95
from utils import get_best_solution

def create_k_to_quality_dataset_k_random(problem: tsplib95.models.StandardProblem, max_range: int, step: int):
    algos = TSPAlgorithms(problem)
    quality = get_best_solution(problem)
    for k in range(1, max_range, step):
        sample_test = [k, algos.k_random(k)[1]/quality - 1]

