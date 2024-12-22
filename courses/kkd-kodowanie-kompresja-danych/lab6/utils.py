import numpy as np
from itertools import product


def get_average_pixel(_pixels: np.array):
    return sum(_pixels) / len(_pixels)

def split_vector(vector):
    epsilon = 0.0001
    vector1 = vector * np.random.uniform(1, 1+epsilon, len(vector))
    vector2 = vector * np.random.uniform(1-epsilon, 1, len(vector))
    return vector1, vector2

def mse(_pixels: np.array, _new_pixels: np.array):
    ret = 0
    for pixel, new_pixel in zip(_pixels, _new_pixels):
        for i in range(3):
            ret += (pixel[i]-new_pixel[i])**2
    return ret

def snr(pixels, mserr):
    sum = 0
    for pixel, i in zip(pixels, range(3)):
        sum += pixel[i]**2
    return sum / (mserr * len(pixels) * 3)

