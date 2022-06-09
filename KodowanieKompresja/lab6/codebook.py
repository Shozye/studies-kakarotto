import numpy as np
from collections import defaultdict
import math
from tqdm import tqdm


def euclid_1d(val1: int, val2: int):
    return abs(val1 - val2)


def get_average_color(pixels):
    return sum(pixels) // len(pixels)


def split_1d(value):
    epsilon = 0.01
    value1 = value * np.random.uniform(1, 1 + epsilon)
    value2 = value * np.random.uniform(1 - epsilon, 1)
    return value1, value2

def create_codebook_for_color(pixels, amount_of_colors: int, color_index):
    groups = [[pixel[color_index] for pixel in pixels]]
    pbar = tqdm(range(amount_of_colors+1))
    for _ in pbar:
        pbar.set_description(f"Splitting... Code book size {len(groups)} / {2 ** amount_of_colors}")
        new_centroids = list()
        for group in groups:
            centroid = get_average_color(group)
            new_centroids.extend(split_1d(centroid))

        groups_for_centroids = defaultdict(list)
        for pixel in pixels:
            color = pixel[color_index]
            closest_centroid = None
            closest_distance = np.inf
            for centroid in new_centroids:
                dist = euclid_1d(color, centroid)
                if dist < closest_distance:
                    closest_centroid = centroid
                    closest_distance = dist
            groups_for_centroids[closest_centroid].append(color)
        groups = list(groups_for_centroids.values())

    centroids = list()
    for group in groups:
        centroids.append(get_average_color(group))

    return centroids


def create_codebook(pixels, amount_of_colors: int):
    codebook = [None, None, None]
    for i in range(3):
        codebook[i] = create_codebook_for_color(pixels, amount_of_colors, i)
    return codebook


def taxi(vec1, vec2):
    return sum([abs(vec1[i] - vec2[i]) for i in range(len(vec1))])


def euclid(vec1, vec2):
    ret = 0
    for i in range(len(vec1)):
        ret += (vec1[i] - vec2[i]) ** 2
    return math.sqrt(ret)
