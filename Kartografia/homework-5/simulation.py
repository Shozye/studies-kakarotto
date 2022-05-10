import random
import time
from rsa_functions import RSA, RSA_CRT
import os
from matplotlib import pyplot as plt
from tqdm import tqdm
import sys
import json
import visualise

"""Zadanie 4"""

e = 65537


def get_rsa_parameters(p, q):
    phi_n = (p - 1) * (q - 1)
    d = pow(e, -1, phi_n)
    return [p * q,  # N
            d,  # d
            d % (p - 1),  # dp
            d % (q - 1),  # dq
            pow(q, -1, p)]  # qi


def measure_time_of_two_primes(p: int, q: int):
    N, d, dp, dq, qi = get_rsa_parameters(p, q)
    random_number = random.randint(2, N - 1)

    rsa_start = time.time()
    RSA(random_number, N, d)
    rsa_time = (time.time() - rsa_start)

    rsa_crt_start = time.time()
    RSA_CRT(random_number, p, q, dp, dq, qi)
    rsa_crt_time = (time.time() - rsa_crt_start)

    return [rsa_time, rsa_crt_time]


def measure_time_of_primes(prime_pairs: list):
    rsa_time = 0
    rsa_crt_time = 0
    for p, q in prime_pairs:
        rsa_time_temp, rsa_crt_time_temp = measure_time_of_two_primes(p, q)
        rsa_time += rsa_time_temp
        rsa_crt_time_temp += rsa_crt_time
    rsa_time /= len(prime_pairs)
    rsa_crt_time /= len(prime_pairs)
    return [rsa_time, rsa_crt_time]


def gather_data_from_file(filepath: str):
    with open(filepath, 'r') as file:
        primes = list(map(int, file.read().split('\n')[:-1]))
    pairs = []
    while len(pairs) != 1000:
        pair = tuple(random.sample(primes, 2))
        if pair not in pairs:
            pairs.append(pair)

    time_data = [measure_time_of_two_primes(*pair) for pair in pairs]
    rsa_time = sum([x[0] for x in time_data])
    rsa_crt_time = sum([x[1] for x in time_data])

    return rsa_time, rsa_crt_time


def gather_data_from_directory(directory_path: str):
    Xs = list()
    rsa_time_values = dict()
    rsa_crt_time_values = dict()
    _tqdm = tqdm(os.listdir(directory_path), "Processing files")  # That's for progress bar displaying purposes
    for filename in _tqdm:
        _tqdm.set_description(f"Processing {filename}")
        amount_of_bits = int(filename.split("_")[1].split(".")[0])  # Filenames are p_{amount_of_bits}.txt
        file_path = os.path.join(directory_path, filename)
        rsa_time, rsa_crt_time = gather_data_from_file(file_path)
        Xs.append(amount_of_bits)
        rsa_time_values[amount_of_bits] = rsa_time
        rsa_crt_time_values[amount_of_bits] = rsa_crt_time
    _tqdm.close()

    Xs.sort()
    with open("plot_data.json", 'w+') as file:
        file.write(json.dumps({
            "Xs": Xs,
            "rsa_time_values": [rsa_time_values[x] for x in Xs],
            "rsa_crt_time_values": [rsa_crt_time_values[x] for x in Xs]}))
    visualise.visualise("plot_data.json")


if __name__ == "__main__":
    gather_data_from_directory(os.path.join(os.getcwd(), "primes_data"))

