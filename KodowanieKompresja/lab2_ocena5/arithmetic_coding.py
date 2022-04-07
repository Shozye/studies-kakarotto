import fractions

import numpy as np
from fractions import Fraction
from tqdm import tqdm

BYTE_RANGE = 256


def get_probability_table(text: bytes) -> list:
    frequency_table = [0] * BYTE_RANGE
    fraction_table = []
    size = len(text)
    for letter in text:
        frequency_table[letter] += 1
    for byte in range(BYTE_RANGE):
        freq = frequency_table[byte]
        fraction_table.append(Fraction(freq, size))
    return fraction_table


def get_range_tables(text: bytes) -> tuple:
    probability_table = get_probability_table(text)
    range_table_start = [Fraction(0, 1) for _ in range(BYTE_RANGE)]
    range_table_end = [Fraction(0, 1) for _ in range(BYTE_RANGE)]
    pointer = Fraction(0, 1)
    for byte in range(BYTE_RANGE):
        range_table_start[byte] = pointer
        pointer += probability_table[byte]
        range_table_end[byte] = pointer
    return range_table_start, range_table_end


def get_binary_code(low: fractions.Fraction, high: fractions.Fraction) -> list:
    exponent = 1
    bits = [1]
    code = Fraction(1, 2)
    while not low < code < high:
        if code >= high:
            code -= Fraction(1, 2 ** exponent)
            bits[-1] = 0
            exponent += 1
            code += Fraction(1, 2 ** exponent)
            bits.append(1)
        elif code <= high:
            exponent += 1
            bits.append(1)
            code += Fraction(1, 2 ** exponent)
    while len(bits) % 8 != 0:
        bits.append(0)
    return [int("".join(map(str, bits[i:i + 8])), 2) for i in range(0, len(bits), 8)]


def compress(filename, path_to_dir, output_dir):
    with open(path_to_dir + filename, 'rb') as file:
        text = file.read()
    range_table_start, range_table_end = get_range_tables(text)
    low = Fraction(0, 1)
    high = Fraction(1, 1)
    _range = Fraction(1, 1)
    amount = 0
    packet_amount = 0

    packets = []
    for c in tqdm(text, "Encoding..."):
        high = low + _range * range_table_end[c]
        low = low + _range * range_table_start[c]
        _range = high - low
        amount += 1
        if amount == 128:
            packets.append((low, high))
            low = Fraction(0, 1)
            high = Fraction(1, 1)
            _range = Fraction(1, 1)
            amount = 0
            packet_amount += 1

    with open(output_dir + filename, 'wb+') as file:
        for byte in range(BYTE_RANGE):
            file.write(byte.to_bytes())
            file.write(range_table_start[byte])

        for packet in tqdm(packets, "Writing to file..."):
            low, high = packet
            code = get_binary_code(low, high)


def decompress(filename, path_to_dir, output_dir):
    return None


if __name__ == "__main__":
    print(get_binary_code(Fraction(5001, 10000), Fraction(5002, 10000)))
