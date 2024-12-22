import argparse

class Parser(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(
            description="Program to run several tests on compiler and provide statistics to user",
        )
        self.add_argument("-e", "--exec-prefix", 
                          help="Defines prefix to use when running compiler",
                          type=str,
                          default="")
        self.add_argument("-v", "--verbose",
                          help="Additional information during testing",
                          action="count",
                          default=0)
        self.add_argument("compiler_path", 
                          type=str, 
                          help="Path to executable file of compiler")