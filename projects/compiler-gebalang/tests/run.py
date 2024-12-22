from tools.input_parser import Parser
from tools.config import Config
from tools.utils import listdir, run_tests
from tools.stats import Statistics

import os

def main():
    args = Parser().parse_args()
    Config.COMPILER_PATH = args.compiler_path
    Config.COMPILER_PREFIX = args.exec_prefix
    Config.VERBOSITY = args.verbose
    stats = Statistics()
    for test_directory in listdir(Config.TEST_DIR, Config.TEST_SUBDIR_REGEX):
        path_to_test_directory = os.path.join(Config.TEST_DIR, test_directory)
        
        print(test_directory, end="")
        run_tests(path_to_test_directory, stats)
        print()

if __name__ == "__main__":
    main()