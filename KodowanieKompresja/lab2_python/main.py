import sys
import my_encodings
from time import time

def test_huffman_encoding(filepath: str, output_filepath: str):
    print(filepath, my_encodings.huffman(filepath, output_filepath))


def test_huffman_decoding(encoded_filepath, decoded_filepath):
    my_encodings.huffman_decode(encoded_filepath, decoded_filepath)


def main():
    filename = "my_test1.txt" if len(sys.argv) == 1 else sys.argv[1]
    filepath = f"files/{filename}"
    name, extension = filename.split(".")
    encoded_filepath = f"encoded/{name + '_commpressed_' + extension}"
    decoded_filepath = f"decoded/{filename}"
    start_time = time()
    test_huffman_encoding(filepath, encoded_filepath)
    middle_time = time()
    test_huffman_decoding(encoded_filepath, decoded_filepath)
    end_time = time()
    print(f"It took {round(middle_time - start_time)} seconds to encode and {round(end_time - middle_time)} to decode")


def tests():

    files = ['pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt',
             'test1.bin',
             'test2.bin',
             'test3.bin']
    #files = ['test2.bin']
    for filename in files:
        filepath = f"files/{filename}"
        name, extension = filename.split(".")
        encoded_filepath = f"encoded/{name + '_commpressed_' + extension}"
        decoded_filepath = f"decoded/{filename}"
        start_time = time()
        test_huffman_encoding(filepath, encoded_filepath)
        middle_time = time()
        test_huffman_decoding(encoded_filepath, decoded_filepath)
        end_time = time()
        print(f"It took {round(middle_time - start_time)} seconds to encode and {round(end_time-middle_time)} to decode")


if __name__ == "__main__":
    main()
    #tests()
