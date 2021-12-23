import numpy as np
import time

class Simulation:
    def __init__(self, n):
        self.n = n
        self.answers = []


    def run(self, k=100):
        iterator = 0
        while iterator < k:
            permutation = np.random.permutation(list(range(self.n)))
            self.insert_sort(permutation)
            iterator += 1


    def insert_sort(self,_data):
        compare_amount = 0
        swap_amount = 0
        time_needed = time.time()
        n = len(_data)
        for j in range(1, n):
            inside = False
            key = _data[j]
            # // Wstaw _data[j] w posortowany podciag _data[0..j-2]
            i = j - 1
            while True:
                compare_amount += 1
                if not i >= 0:
                    break
                compare_amount += 1
                if not _data[i] > key:
                    break
                _data[i + 1] = _data[i]
                swap_amount += 1
                i -= 1
            _data[i + 1] = key
            swap_amount += 1
        time_needed = time.time() - time_needed
        self.answers.append({"n": n, "cmp": compare_amount, "swp": swap_amount, "time":time_needed})