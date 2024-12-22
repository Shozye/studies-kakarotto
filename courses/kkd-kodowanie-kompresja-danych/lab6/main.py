import sys
from Tga import Tga
import os
from utils import mse, snr
from itertools import product
from codebook import create_codebook
from codebook import euclid_1d
import numpy as np

"""
def quantize_value(value: np.float64, codebook: list, index: int):
    codes = codebook[index]
    closest_distance = np.inf
    closest_code = None
    for code in codes:
        dist = euclid_1d(value, code)
        if dist < closest_distance:
            closest_code = code
            closest_distance = dist
    return closest_code
"""


def quantize_value(value: np.float64, amount_of_bits: int):
    negative = value < 0
    val = abs(int(value))
    bits = bin(val)[2:]
    bits = (8 - len(bits)) * '0' + bits
    bits = bits[:amount_of_bits]
    bits += '1'
    bits += (8 - len(bits)) * '0'
    bits = '0b' + bits
    val = int(bits, 2)
    if negative:
        val *= (-1)
    return val


def get_low_mask():
    return np.array([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 1]])


def get_high_mask():
    return np.array([[-1, -1, -1],
                     [-1, 9, -1],
                     [-1, -1, -1]])


def get_index(row, col, width):
    return row * width + col


def encode_filter(pixels, mask, width, height):
    new_pixels = np.zeros(len(pixels) * 3).reshape((len(pixels), 3))
    for row in range(height):
        for col in range(width):
            for i, j in product(range(3), range(3)):
                pixel = np.array([0, 0, 0])
                if 0 <= row + i - 1 < height and 0 <= col + j - 1 < width:
                    pixel = pixels[get_index(row + i - 1, col + j - 1, width)]
                new_pixels[get_index(row, col, width)] += pixel * mask[i][j]
            new_pixels[get_index(row, col, width)] //= sum(sum(mask))
    return new_pixels


def quantized_one(pixel: np.array, amount_of_bits: int):
    new_pixel = np.copy(pixel)
    for index, color in enumerate(new_pixel):
        new_pixel[index] = quantize_value(color, amount_of_bits)
    return new_pixel


def encode(pixels: np.array, amount_of_bits):
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
    for index, d_index in enumerate(pixels[1:], start=1):
        new_pixels[index] = d_index + new_pixels[index - 1]
    return new_pixels


def quantize(pixels: np.array, amount_of_bits):
    new_pixels = np.zeros(len(pixels) * 3).reshape((len(pixels), 3))
    for i in range(len(new_pixels)):
        new_pixels[i] = quantized_one(pixels[i], amount_of_bits)
    return new_pixels


def decode_both_filters(pixels_low: np.array, pixels_high: np.array):
    new_pixels = np.zeros(len(pixels_low) * 3).reshape((len(pixels_low), 3))
    for i in range(len(new_pixels)):
        new_pixels[i] = (pixels_low[i] * 9 + pixels_high[i]) // 10
    return new_pixels


def main(input_path, output_path, amount_of_bits):
    tga = Tga(input_path)
    old_pixels = np.copy(tga.pixels)
    pixels = np.copy(tga.pixels)
    print(pixels)
    pixels_low = encode_filter(pixels, get_low_mask(), tga.width, tga.height)
    print(pixels_low)
    pixels_low = encode(pixels_low, amount_of_bits)
    print(pixels_low)
    pixels_high = quantize(encode_filter(pixels, get_high_mask(), tga.width, tga.height), amount_of_bits)
    pixels_low = decode_differentiated_and_quantized(pixels_low)
    tga.update(pixels_low)
    tga.write(output_path + "low")
    tga.update(pixels_high)
    tga.write(output_path + "high")
    pixels = decode_both_filters(pixels_low, pixels_high)
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
