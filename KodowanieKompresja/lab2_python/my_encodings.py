import utils
import json
import time

def encode(filename: str, output_filename: str, code: dict, header: bytes):
    with open(output_filename, 'wb+') as write_file, open(filename, 'rb') as read_file:
        encoded = ""
        while True:
            read_byte = read_file.read(1)
            if not read_byte:
                break
            encoded += code[read_byte]
        # print(encoded)
        split_to_bytes = [encoded[x:x + 8] for x in range(0, len(encoded), 8)]
        last_byte_len = str(len(split_to_bytes[-1])).encode("utf-8")
        compressed = list(map(lambda x: int(x, 2).to_bytes(1, 'little'), split_to_bytes))
        # print("OK",bin(int.from_bytes(compressed[-1],'little')))
        write_file.write(last_byte_len + header)
        # print(compressed)
        # print(b''.join(compressed))
        write_file.write(b''.join(compressed))


def dump(codes: dict):
    dumped = b''
    for key, value in codes.items():
        dumped += b' ' + key + b' ' + value.encode('utf-8')
    return dumped


def load(dumped: bytes):
    code = dict()
    # print(len(dumped), dumped)
    pointer = 1
    dumped += b' '
    while pointer != len(dumped):
        argument = dumped[pointer]
        pointer += 2
        new_pointer = pointer
        while dumped[new_pointer] != 32:
            new_pointer += 1
        value = dumped[pointer:new_pointer]
        code[argument.to_bytes(1, 'little')] = value.decode('utf-8')
        pointer = new_pointer + 1
    return code


def make_code_header(codes: dict):
    header_codes = dump(codes)
    header_len = len(header_codes)
    header = str(header_len).encode("utf-8") + header_codes
    return header


def huffman(filename: str, output_filename: str):
    code = utils.get_huffman_code(utils.get_file_data(filename))
    header = make_code_header(code)
    encode(filename, output_filename, code, header)
    return {"entropy": utils.entropy(output_filename),
            "average_encoding": sum([len(x) for x in code.values()]) / len(code.values()),
            "compression": utils.compression(filename, output_filename)
            }


def pad_zeroes(word: str, pad_num: int):
    return (pad_num - len(word)) * "0" + word


def create_decoding_dict(reverse_codes: dict):
    bin_codes = reverse_codes.keys()
    decoding_dict = dict()



def huffman_decode(filename: str, output_filename: str):
    with open(filename, 'rb') as read_file:
        header_size = b''
        header_size_found = False
        last_byte_size = read_file.read(1)
        while not header_size_found:
            read_byte = read_file.read(1)
            if read_byte == b' ':
                header_size_found = True
                header_size = int(header_size)
            else:
                header_size += read_byte
        huffman_dict = load((b' ' + read_file.read(header_size - 1)))
        rest = read_file.read()

        output = ""
        for byte in rest[:-1]:
            output += pad_zeroes(bin(byte)[2:], 8)
        output += pad_zeroes(bin(rest[-1])[2:], int(last_byte_size))

        codes_revert = dict()
        for key, value in huffman_dict.items():
            codes_revert[value] = key
        bin_codes = codes_revert.keys()
        pointer = 0
        real_output = b""


        searching_now = ""
        start = time.time()
        while pointer != len(output):
            searching_now += output[pointer]
            pointer += 1

            if searching_now in bin_codes:
                real_output += codes_revert[searching_now]
                searching_now = ""
        end = time.time()
        try:
            real_output = real_output.decode('utf-8')
            with open(output_filename, 'w+') as write_file:
                write_file.write(real_output)
        except:
            with open(output_filename, 'wb+') as write_file:
                write_file.write(real_output)
