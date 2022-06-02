import sys
from Tga import Tga
import os
from utils import mse, snr
from quantize import quantize
from codebook import create_codebook
import numpy as np

def main():
    tga = Tga(INPUT_FILE)
    color_map = create_codebook(tga.pixels, AMOUNT_OF_COLOURS)
    old_pixels = np.copy(tga.pixels)
    new_pixels = quantize(tga.pixels, color_map)
    mserr = mse(old_pixels, new_pixels)
    print("Błąd średniokwadratowy: ", mserr)
    print("Stosunek sygnału do szumu: ", snr(new_pixels, mserr))
    tga.write(OUTPUT_FILE)


if __name__ == "__main__":
    INPUT_FILE = sys.argv[1]
    INPUT_PATH = os.path.join("pictures", INPUT_FILE)
    OUTPUT_FILE = sys.argv[2]
    OUTPUT_PATH = os.path.join("pictures", OUTPUT_FILE)
    AMOUNT_OF_COLOURS = int(sys.argv[3])
    main()