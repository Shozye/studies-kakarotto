import os
import json
import time

from Simulation import Simulation
from Logger import Logger


def main():
    logger = Logger()
    for n in range(1000, 100001, 1000):
        start_n_time = time.time()
        if n % 10000 == 0:
            print(f"{n / 1000}% done")
        n_data = []
        for k in range(50):
            start_time = time.time()
            simulation = Simulation(n)
            simulation.run()
            n_data.append({"index": k, "answers": simulation.answers, "time": time.time() - start_time})
        logger.log(n, json.dumps(n_data))
        print(f"n={n} took {int(time.time() - start_n_time)} seconds")


if __name__ == "__main__":
    main()
