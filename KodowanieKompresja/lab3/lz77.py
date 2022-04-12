import numpy as np
import utils
from tqdm import tqdm


def compress(filename: str, path_to_dir: str, output_dir: str):
    with open(path_to_dir + filename, 'rb') as plaintext_file, open(output_dir + filename, 'wb+') as compressed_file:
        plaintext = np.array(list(plaintext_file.read()), dtype=np.int8)
        print(plaintext)
        pbar = tqdm(total=len(plaintext), desc="Compression...")

        dict_buffer_ptr_start = 0
        dict_buffer_ptr_end = 0
        coding_buffer_ptr_start = 0
        coding_buffer_ptr_end = 256
        while dict_buffer_ptr_end != len(plaintext):
            pbar.update(dict_buffer_ptr_end - pbar.n)
            longest_prefix = []
            prefix_index = -1
            # ZNAJDOWANIE PREFIXU BUFORU KODOWANIA W SLOWNIKU
            for letter in plaintext[coding_buffer_ptr_start: coding_buffer_ptr_end]:
                temp_prefix = longest_prefix.copy()
                temp_prefix.append(letter)

                index = utils.sublistExists(plaintext[dict_buffer_ptr_start:dict_buffer_ptr_end], temp_prefix)
                if index == -1:
                    break
                prefix_index = index

                longest_prefix = temp_prefix
            # JEZELI ZADNEGO PREFIXU NIE MA
            if not longest_prefix:
                byte_to_write = plaintext[coding_buffer_ptr_start]
                compressed_file.write(b'\x00')
                compressed_file.write(byte_to_write)

                coding_buffer_ptr_start = min(coding_buffer_ptr_start + 1, len(plaintext))
                coding_buffer_ptr_end = min(coding_buffer_ptr_end + 1, len(plaintext))
                dict_buffer_ptr_end += 1
                dict_buffer_ptr_start = max(dict_buffer_ptr_end - 255, 0)
            else:
                #print(coding_buffer_ptr_start, dict_buffer_ptr_start, prefix_index)
                j = (coding_buffer_ptr_start - (dict_buffer_ptr_start + prefix_index)).to_bytes(1, 'little')
                l = (len(longest_prefix)).to_bytes(1, 'little')
                compressed_file.write(j)
                compressed_file.write(l)

                coding_buffer_ptr_start = min(coding_buffer_ptr_start + len(longest_prefix), len(plaintext))
                coding_buffer_ptr_end = min(coding_buffer_ptr_end + len(longest_prefix), len(plaintext))
                dict_buffer_ptr_end += len(longest_prefix)
                dict_buffer_ptr_start = max(dict_buffer_ptr_end - 255, 0)
        pbar.close()


def decompress(filename: str, path_to_dir: str, output_dir: str):
    with open(path_to_dir + filename, 'rb') as plaintext_file, open(output_dir + filename, 'wb+') as compressed_file:
        plaintext = []
        while True:
            j = plaintext_file.read(1)
            if not j:
                break
            l = plaintext_file.read(1)
            if j == b'\x00':
                plaintext.append(l[0])
            else:
                to_add = []
                for i in range(-j[0], -j[0]+l[0]):
                    to_add.append(plaintext[i])
                plaintext.extend(to_add)
        plaintext = np.array(plaintext, dtype=np.int8)
        compressed_file.write(plaintext.tobytes('C'))
