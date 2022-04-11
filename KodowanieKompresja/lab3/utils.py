import os
import math
import numpy as np

def sublistExists(list, sublist):
    for i in range(len(list)-len(sublist)+1):
        if np.equal(sublist, list[i:i+len(sublist)]).all():
            return i
    return -1


def get_file_data(filename):
    with open(filename, 'rb') as file:
        frequencies = dict()
        size = 0
        while True:
            byte = file.read(1)
            if not byte:
                break
            size += 1
            if frequencies.get(byte) is None:
                frequencies[byte] = 1
            else:
                frequencies[byte] += 1
    return {"size": size, "frequencies": frequencies}


def entropy_from_data(data: dict):
    information_sum = sum([x * math.log2(x) for x in data['frequencies'].values()])
    return math.log2(data['size']) - information_sum / data['size']


def entropy(filename: str):
    return entropy_from_data(get_file_data(filename))


def get_file_length(filename: str):
    return os.stat(filename).st_size


def compression(filename: str, filename_compressed: str) -> str:
    compressed_len = get_file_length(filename_compressed)
    normal_len = get_file_length(filename)
    return str(round(compressed_len / normal_len * 100, 2)) + "%"


def end_information(filename_start: str, filename_compressed: str):
    print(f"""
    Długość kodowanego pliku to {get_file_length(filename_start)}
    Dlugosc kodu to {get_file_length(filename_compressed)}
    Stopien kompresji: {compression(filename_start, filename_compressed)}
    Entropia kodowanego tekstu: {entropy(filename_start)}
    Entropia uzyskanego: {entropy(filename_compressed)}""")
