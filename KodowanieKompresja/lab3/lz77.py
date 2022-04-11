import numpy as np
import utils


def compress(filename: str, path_to_dir: str, output_dir: str):
    with open(path_to_dir + filename, 'rb') as plaintext_file, open(output_dir + filename, 'wb+') as compressed_file:
        plaintext = np.array(list(plaintext_file.read()), dtype=np.int8)
        dict_buffer_ptr_start = 0
        dict_buffer_ptr_end = 0
        coding_buffer_ptr_start = 0
        coding_buffer_ptr_end = 256
        while dict_buffer_ptr_end != len(plaintext):
            longest_prefix = []
            prefix_index = -1
            for letter in plaintext[coding_buffer_ptr_start: coding_buffer_ptr_end]:
                temp_prefix = longest_prefix.copy()
                temp_prefix.append(letter)

                index = utils.sublistExists(plaintext[dict_buffer_ptr_start:dict_buffer_ptr_end], temp_prefix)
                if index == -1:
                    break
                prefix_index = index

                longest_prefix = temp_prefix

            if not longest_prefix:
                byte_to_write = plaintext[coding_buffer_ptr_start]
                compressed_file.write(b'\x00')
                compressed_file.write(byte_to_write)

                coding_buffer_ptr_start = min(coding_buffer_ptr_start + 1, len(plaintext))
                coding_buffer_ptr_end = min(coding_buffer_ptr_end + 1, len(plaintext))
                dict_buffer_ptr_end += 1
                dict_buffer_ptr_start = max(dict_buffer_ptr_end - 255, 0)
            else:
                j = (coding_buffer_ptr_start - (dict_buffer_ptr_start + prefix_index)).to_bytes(1, 'little')
                l = (len(longest_prefix)).to_bytes(1, 'little')
                compressed_file.write(j)
                compressed_file.write(l)

                coding_buffer_ptr_start = min(coding_buffer_ptr_start + len(longest_prefix), len(plaintext))
                coding_buffer_ptr_end = min(coding_buffer_ptr_end + len(longest_prefix), len(plaintext))
                dict_buffer_ptr_end += len(longest_prefix)
                dict_buffer_ptr_start = max(dict_buffer_ptr_end - 255, 0)

def decompress(filename: str, path_to_dir: str, output_dir: str):
    with open(path_to_dir + filename, 'rb') as plaintext_file, open(output_dir + filename, 'wb+') as compressed_file:
        pass

