import numpy as np
import utils
from collections import defaultdict
import math
from tqdm import tqdm


def create_codebook(pixels, amount_of_colors: int):
    centroids = list([utils.get_average_pixel(pixels)])
    pbar = tqdm(range(amount_of_colors), "Splitting...")
    for _ in pbar:
        pbar.set_description(f"Splitting... Code book size {len(centroids)} / {2**amount_of_colors}")
        new_centroids = list()
        for centroid in centroids:
            centroid1, centroid2 = utils.split_vector(centroid)
            new_centroids.extend([centroid1, centroid2])

        pixel_groups = defaultdict(list)
        for pixel in pixels:
            closest_centroid = None
            closest_dist = np.inf
            for centroid in new_centroids:
                dist = euclid(pixel, centroid)
                if dist < closest_dist:
                    closest_dist = dist
                    closest_centroid = centroid
            pixel_groups[tuple(closest_centroid)].append(pixel)
        centroids = [utils.get_average_pixel(pixel_group) for pixel_group in pixel_groups.values()]
        pbar.set_description(f"Splitting... Code book size {len(centroids)} / {2**amount_of_colors}")

    pixel_groups = defaultdict(list)
    for pixel in pixels:
        closest_centroid = None
        closest_dist = np.inf
        for centroid in centroids:
            dist = taxi(pixel, centroid)
            if dist < closest_dist:
                closest_dist = dist
                closest_centroid = centroid
        pixel_groups[tuple(closest_centroid)].append(pixel)

    color_map = dict()
    for centroid, pixel_group in pixel_groups.items():
        for pixel in pixel_group:
            color_map[tuple(pixel)] = np.array(centroid)
    return color_map


def taxi(vec1, vec2):
    return sum([abs(vec1[i] - vec2[i]) for i in range(len(vec1))])


def euclid(vec1, vec2):
    ret = 0
    for i in range(len(vec1)):
        ret += (vec1[i] - vec2[i]) ** 2
    return math.sqrt(ret)
