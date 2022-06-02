import numpy as np


class Tga:
    def __init__(self, path_to_file):
        self.footer = None
        self.pixels = None
        self.height = None
        self.width = None
        self.header = None
        self.parse_file(path_to_file)

    def parse_file(self, path_to_file):
        with open(path_to_file, 'rb+') as file:
            data = file.read()

        signature = data[-18:-2]
        self.header = data[:18]

        self.width = data[12] + data[13] * 256
        self.height = data[14] + data[15] * 256

        if signature == b'TRUEVISION-XFILE':
            colors = data[18:-26]
            self.footer = data[-26:]
        else:
            colors = data[18:]

        self.pixels = np.zeros(self.width * self.height * 3).reshape(self.height * self.width, 3)

        i = 0
        for index in range(self.height * self.width):
            self.pixels[index][0] = colors[i]
            self.pixels[index][1] = colors[i + 1]
            self.pixels[index][2] = colors[i + 2]
            i += 3

    def write(self, path_to_file):
        with open(path_to_file, 'wb+') as file:
            file.write(self.header)
            for index in range(self.height*self.width):
                for i in range(3):
                    file.write(int(self.pixels[index][i]).to_bytes(1, 'little'))

            if self.footer:
                file.write(self.footer)
