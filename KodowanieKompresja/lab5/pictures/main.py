#!/usr/bin/python
""" jpeg-ls coding """

from sys import argv
from math import log, inf
from collections import defaultdict


class Pixel:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __add__(self, other):
        return Pixel(
            self.red + other.red, self.green + other.green, self.blue + other.blue
        )

    def __sub__(self, other):
        return Pixel(
            self.red - other.red, self.green - other.green, self.blue - other.blue
        )

    def __floordiv__(self, number):
        return Pixel(self.red // number, self.green // number, self.blue // number)

    def __mod__(self, number):
        return Pixel(self.red % number, self.green % number, self.blue % number)


def new_scheme(n, w, nw):
    n = [n.red, n.green, n.blue]
    w = [w.red, w.green, w.blue]
    nw = [nw.red, nw.green, nw.blue]
    rgb = []
    for color in range(3):
        if nw[color] >= max(w[color], n[color]):
            rgb.append(max(w[color], n[color]))
        elif nw[color] <= min(w[color], n[color]):
            rgb.append(min(w[color], n[color]))
        else:
            rgb.append(w[color] + n[color] - nw[color])
    return Pixel(rgb[0], rgb[1], rgb[2])


schemes = [
    lambda n, w, nw: w,
    lambda n, w, nw: n,
    lambda n, w, nw: nw,
    lambda n, w, nw: n + w - nw,
    lambda n, w, nw: n + (w - nw) // 2,
    lambda n, w, nw: w + (n - nw) // 2,
    lambda n, w, nw: (n + w) // 2,
    new_scheme,
]


def jpeg_ls(bitmap, scheme):
    result = []
    for i, row in enumerate(bitmap):
        encoded_row = []
        for j, pixel in enumerate(row):
            if i == 0:
                n = Pixel(0, 0, 0)
            else:
                n = bitmap[i - 1][j]

            if j == 0:
                w = Pixel(0, 0, 0)
            else:
                w = bitmap[i][j - 1]

            if i == 0 or j == 0:
                nw = Pixel(0, 0, 0)
            else:
                nw = bitmap[i - 1][j - 1]

            encoded_row.append((pixel - scheme(n, w, nw)) % 256)
        result.append(encoded_row)
    return result


def parse_bitmap(bitmap, width, height):
    result = []
    row = []
    for i in range(width * height):
        row.append(
            Pixel(blue=bitmap[i * 3], green=bitmap[i * 3 + 1], red=bitmap[i * 3 + 2])
        )

        if width == len(row):
            result.insert(0, row)
            row = []
    return result


def entropy(freq, count):
    H = 0
    for i in freq:
        H += freq[i] / count * -log(freq[i] / count, 2)
    return H


def calculate_entropy(bitmap, color):
    freq = defaultdict(int)
    count = 0

    for row in bitmap:
        for pixel in row:
            if color == "red":
                freq[pixel.red] += 1
                count += 1
            elif color == "green":
                freq[pixel.green] += 1
                count += 1
            elif color == "blue":
                freq[pixel.blue] += 1
                count += 1
            else:
                freq[pixel.red] += 1
                freq[pixel.green] += 1
                freq[pixel.blue] += 1
                count += 3

    return entropy(freq, count)


def print_entropy(entropies):
    print("Entropy: ", entropies[""])
    print("Red: ", entropies["red"])
    print("Green: ", entropies["green"])
    print("Blue: ", entropies["blue"])
    print("############################")


if __name__ == "__main__":
    if len(argv) == 2:
        with open(argv[1], "rb") as f:
            tga = f.read()
            width = tga[13] * 256 + tga[12]
            height = tga[15] * 256 + tga[14]
            bitmap = parse_bitmap(tga[18 : len(tga) - 26], width, height)

            print("Input entropy")
            entropies = {
                "": calculate_entropy(bitmap, ""),
                "red": calculate_entropy(bitmap, "red"),
                "green": calculate_entropy(bitmap, "green"),
                "blue": calculate_entropy(bitmap, "blue"),
            }
            print_entropy(entropies)

            best = inf
            best_red = inf
            best_green = inf
            best_blue = inf
            best_id = 0
            best_red_id = 0
            best_green_id = 0
            best_blue_id = 0

            for idx, scheme in enumerate(schemes):
                encoded = jpeg_ls(bitmap, scheme)

                entropies = {
                    "": calculate_entropy(encoded, ""),
                    "red": calculate_entropy(encoded, "red"),
                    "green": calculate_entropy(encoded, "green"),
                    "blue": calculate_entropy(encoded, "blue"),
                }

                if entropies[""] < best:
                    best = entropies[""]
                    best_id = idx + 1
                if entropies["red"] < best_red:
                    best_red = entropies["red"]
                    best_red_id = idx + 1
                if entropies["green"] < best_green:
                    best_green = entropies["green"]
                    best_green_id = idx + 1
                if entropies["blue"] < best_blue:
                    best_blue = entropies["blue"]
                    best_blue_id = idx + 1

                print("Schemat ", idx + 1)
                print_entropy(entropies)

            print("Best entropy: ", best_id)
            print("Best red: ", best_red_id)
            print("Best green: ", best_green_id)
            print("Best blue: ", best_blue_id)