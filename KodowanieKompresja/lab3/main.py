import sys
import time

from utils import end_information
from lz77 import compress
from lz77 import decompress

from tqdm import tqdm


def printUsage():
    print("""Usage:
    test.py [type] [filename] [path_to_dir] [output_dir]
    where type is compress or decompress
    path to dir is directory where filename is located
    output_dir is where output_file should be located. 
    Note that output filename has got the same name as filename""")
    sys.exit(1)


def main():
    print(sys.argv)
    start_time = time.time()
    if len(sys.argv) != 5:
        printUsage()
    if sys.argv[1] == "compress":
        compress(filename=sys.argv[2], path_to_dir=sys.argv[3], output_dir=sys.argv[4])
        end_information(sys.argv[3] + sys.argv[2], sys.argv[4] + sys.argv[2])
    elif sys.argv[1] == "decompress":
        decompress(filename=sys.argv[2], path_to_dir=sys.argv[3], output_dir=sys.argv[4])
    else:
        printUsage()
    print(f"{sys.argv[1]} took {time.time() - start_time} seconds.")


def tests():
    #files = ['pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt',
    #         'test1.bin',
    #         'test2.bin',
    #         'test3.bin']
    files = ['my_test5.txt']
    for filename in files:
        start_time = time.time()
        print(f"Start compressing {filename}")
        compress(filename, path_to_dir="files/", output_dir="compressed/")
        compress_time = time.time()
        end_information("files/" + filename, "compressed/" + filename)
        print(f"Compression of {filename} took {round(compress_time - start_time,2)} seconds")
        decompress(filename, path_to_dir="compressed/", output_dir="decompressed/")
        decompress_time = time.time()
        print(f"Decompression of {filename} took {round(decompress_time - compress_time, 2)} seconds")


if __name__ == "__main__":
    tests()
    #main()