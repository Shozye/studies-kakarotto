import os
import json
import time
import random

from Logger import Logger
from Simulation import Simulation


def main(k):
    logger = Logger()
    for n in range(100, 10001, 100):
        start_n_time = time.time()
        if n % 1000 == 0:
            print(f"{n / 100}% done")
        n_data = []
        simulation = Simulation(n)
        simulation.run(k)
        n_data.append({"n": n, "answers": simulation.answers, "timeit": time.time() - start_n_time})
        logger.log(n, json.dumps(n_data))
        print(f"n={n} took {int(time.time() - start_n_time)} seconds")


if __name__ == "__main__":
    main(1)
