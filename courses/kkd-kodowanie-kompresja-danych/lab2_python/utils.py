import math
import os


def get_file_data(filename):
    with open(filename, 'rb') as file:
        frequencies = dict()
        size = 0
        while True:
            byte = file.read(1)
            if not byte:
                break
            size += 1
            if frequencies.get(byte) is None:
                frequencies[byte] = 1
            else:
                frequencies[byte] += 1
    return {"size": size, "frequencies": frequencies}


def entropy_from_data(data: dict):
    information_sum = sum([x * math.log2(x) for x in data['frequencies'].values()])
    return math.log2(data['size']) - information_sum / data['size']


def entropy(filename: str):
    return entropy_from_data(get_file_data(filename))


class Tree:
    def __init__(self, __bytes: list, frequency):
        self.bytes = __bytes
        self.frequency = frequency
        self.left = "null"
        self.right = "null"

    def is_leaf(self) -> bool:
        return self.left == "null" and self.right == "null"

    def __repr__(self):
        return f"""{{"bytes":{self.bytes}, "frequency":{self.frequency}, "left": {self.left}, "right": {self.right}}}"""


def get_root_of_2_subtrees(tree1: Tree, tree2: Tree) -> Tree:
    root_bytes = tree1.bytes.copy()
    root_bytes.extend(tree2.bytes)
    sum_frequency = tree1.frequency + tree2.frequency
    root = Tree(root_bytes, sum_frequency)
    root.left = tree1
    root.right = tree2
    return root


def write_tree(tree: Tree, filename="tree_test.json"):
    with open(f"tree_tests/{filename}, 'w+'") as file:
        file.write(str(tree))


def get_huffman_code(data: dict):
    frequencies = data['frequencies']
    tree_frequencies = list([Tree([x[0]], x[1]) for x in frequencies.items()])
    tree_frequencies.sort(key=lambda x: x.frequency)
    while len(tree_frequencies) != 1:
        min_1, min_2 = tree_frequencies.pop(0), tree_frequencies.pop(0)
        root = get_root_of_2_subtrees(min_1, min_2)
        tree_frequencies.append(root)
        tree_frequencies.sort(key=lambda x: x.frequency)
    codes = dict()
    to_parse = [(tree_frequencies[0], "0")]
    while len(to_parse) != 0:
        parsing = to_parse.pop(0)
        if parsing[0].is_leaf():
            codes[parsing[0].bytes[0]] = parsing[1]
        else:
            if parsing[0].left != "null":
                to_parse.append((parsing[0].left, parsing[1] + "0"))
            if parsing[0].right != "null":
                to_parse.append((parsing[0].right, parsing[1] + "1"))
    return codes


def test_entropy():
    print(entropy('../lab2_ocena5/files/pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt'))
    print(entropy('../lab2_ocena5/files/test1.bin'))
    print(entropy('../lab2_ocena5/files/test2.bin'))
    print(entropy('../lab2_ocena5/files/test3.bin'))


def test_get_huffman_code():
    print(get_huffman_code(get_file_data("../lab2_ocena5/files/my_test1.txt")))


def get_file_length(filename: str):
    return os.stat(filename).st_size


def compression(filename: str, filename_compressed: str) -> str:
    compressed_len = get_file_length(filename_compressed)
    normal_len = get_file_length(filename)
    return str(round(compressed_len / normal_len * 100, 2)) + "%"


if __name__ == "__main__":
    test_entropy()
    #test_get_huffman_code()
