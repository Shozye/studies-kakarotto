import numpy as np
from itertools import product


def mse(_pixels: np.array, _new_pixels: np.array):
    ret = 0
    for pixel, new_pixel in zip(_pixels, _new_pixels):
        for i in range(3):
            ret += (pixel[i] - new_pixel[i]) ** 2
    return ret


def snr(pixels, mserr):
    sum = 0
    for pixel, i in zip(pixels, range(3)):
        sum += pixel[i] ** 2
    return sum / (mserr * len(pixels) * 3)
