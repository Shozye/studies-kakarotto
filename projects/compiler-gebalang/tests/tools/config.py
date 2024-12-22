import os

class Config:
    TEST_DIR = "test_data"
    TEST_SUBDIR_REGEX = r"test_.*"
    TEST_CONFIG = "config.json"
    VM_PATH = os.path.join("..", "vm-stats", )
    
    DEFAULT_TRANSLATED = ""
    DEFAULT_COMPILATION = "ERROR"
    DEFAULT_RUNTIME = "ERROR"
    DEFAULT_STDIN = ""
    DEFAULT_STDOUT = ""
    DEFAULT_DESCRIPTION = ""
    
    COMPILER_PATH = None
    COMPILER_PREFIX = None
    VERBOSITY = None