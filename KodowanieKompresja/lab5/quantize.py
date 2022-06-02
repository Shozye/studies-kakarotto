import numpy as np


def quantize(_pixels: np.array, _color_map: np.array):
    for index in range(len(_pixels)):
        _pixels[index] = _color_map[tuple(_pixels[index])]
    return _pixels
