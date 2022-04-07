import sys
from time import time
from arithmetic_coding import compress
from arithmetic_coding import decompress


def printUsage():
    print("""Usage:
    main.py [type] [filename] [path_to_dir] [output_dir]
    where type is compress or decompress
    path to dir is directory where filename is located
    output_dir is where output_file should be located. 
    Note that output filename has got the same name as filename""")
    sys.exit(1)


def main():
    print(sys.argv)
    if len(sys.argv) != 5:
        printUsage()
    if sys.argv[1] == "compress":
        compress(sys.argv[2], path_to_dir=sys.argv[3], output_dir=sys.argv[4])
    elif sys.argv[1] == "decompress":
        decompress(sys.argv[2], path_to_dir=sys.argv[3], output_dir=sys.argv[4])
    else:
        printUsage()


def tests():
    files = ['pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt',
             'test1.bin',
             'test2.bin',
             'test3.bin']
    files = ['my_test1.txt']
    for filename in files:
        compress(filename, path_to_dir="files/", output_dir="compressed/")
        decompress(filename, path_to_dir="compressed/", output_dir="decompressed/")


if __name__ == "__main__":
    #tests()
    main()