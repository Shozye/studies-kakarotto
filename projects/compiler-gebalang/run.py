import argparse
import os
import sys

from src.main import compile_gebalang
from src.tac_validator.exceptions import TACException


class Parser(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(
            description="""GebalangCompiler created by Mateusz Pelechaty""",
        )
        self.add_argument("input_path",
                          type=str,
                          help="Path to Gebalang file")
        self.add_argument("output_path",
                          type=str,
                          help="Path to compiled file")
        self.add_argument("-o", "--output-dir",
                          type=str,
                          dest="output_dir",
                          help="""Path to directory, from which relative path of `output_path` will start. 
                          Defaults to `.`""",
                          default=".")
        self.add_argument("-v", "--verbose",
                          action="store_true",
                          dest="verbose",
                          help="Specifies if compiler should save intermediate products of compiler. Defaults to False",
                          default=False)


def main():
    args = Parser().parse_args()

    with open(args.input_path, encoding='utf-8') as file:
        text = file.read()
    if not os.path.isdir(args.output_dir):
        os.mkdir(args.output_dir)

    try:
        compile_gebalang(
            text,
            os.path.basename(args.input_path).split(".")[0],
            args.output_path,
            args.output_dir,
            args.verbose
        )
    except TACException as e:
        print("ERROR:", e.__repr__())
        sys.exit(1)

if __name__ == "__main__":
    main()

