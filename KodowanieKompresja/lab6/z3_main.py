import sys
from Tga import Tga
import os
from utils import mse, snr

import numpy as np


def quantize_value(value: np.float64, amount_of_bits: int):
    if value < 0:
        bits = bin(int(value))[3:]
    else:
        bits = bin(int(value))[2:]
    bits = '0' * (8 - len(bits)) + bits
    bits = bits[:amount_of_bits]
    bits += '1'
    bits += '0' * (8 - len(bits))
    bits = '0b' + bits
    if value < 0:
        return (-1) * int(bits, 2)
    return int(bits, 2)


def quantized_one(pixel: np.array, amount_of_bits: int):
    new_pixel = np.copy(pixel)
    for index, color in enumerate(new_pixel):
        new_pixel[index] = quantize_value(color, amount_of_bits)
    return new_pixel


def encode(pixels: np.array, amount_of_bits: int):
    d = np.zeros(len(pixels) * 3).reshape((len(pixels), 3))
    d[0] = quantized_one(pixels[0], amount_of_bits)
    X_n__minus__1_reversed = d[0]
    for i in range(1, len(pixels)):
        d[i] = quantized_one(pixels[i] - X_n__minus__1_reversed, amount_of_bits)
        X_n__minus__1_reversed = X_n__minus__1_reversed + d[i]
    return d


def decode_differentiated_and_quantized(pixels: np.array):
    new_pixels = np.zeros(len(pixels) * 3).reshape((len(pixels), 3))
    new_pixels[0] = pixels[0]
    for index, d_index in enumerate(pixels):
        if index == 0: continue
        new_pixels[index] = d_index + new_pixels[index - 1]
    return new_pixels


def main(input_path, output_path, amount_of_bits):
    tga = Tga(input_path)
    old_pixels = np.copy(tga.pixels)
    pixels = np.copy(tga.pixels)
    pixels = encode(pixels, amount_of_bits)
    pixels = decode_differentiated_and_quantized(pixels)
    tga.update(pixels)
    tga.write(output_path)

    mserr = mse(old_pixels, pixels)
    print("Błąd średniokwadratowy: ", mserr)
    print("Stosunek sygnału do szumu: ", snr(pixels, mserr))
    tga.write(output_path)


if __name__ == "__main__":
    INPUT_FILE = sys.argv[1]
    INPUT_PATH = os.path.join("pictures", INPUT_FILE)
    OUTPUT_FILE = sys.argv[2]
    OUTPUT_PATH = os.path.join("pictures", OUTPUT_FILE)
    AMOUNT_OF_BITS = int(sys.argv[3])
    main(INPUT_PATH, OUTPUT_PATH, AMOUNT_OF_BITS)
