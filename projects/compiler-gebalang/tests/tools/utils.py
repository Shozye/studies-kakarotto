import json
from .config import Config
from .stats import Statistics
import re
import os

class Testcase:
    def __init__(self, data: dict):
        self.filename = data['filename']
        
        self.translated = data.get('translated', Config.DEFAULT_TRANSLATED)
        self.compilation = data.get("compilation", Config.DEFAULT_COMPILATION)
        self.runtime = data.get("runtime", Config.DEFAULT_RUNTIME)
        self.stdin = data.get("stdin", Config.DEFAULT_STDIN)
        self.stdout = data.get("stdout", Config.DEFAULT_STDOUT)
        self.description = data.get("description", Config.DEFAULT_DESCRIPTION)
        
        if self.compilation == "ERROR":
            self.runtime = "ERROR"
    

def read_test_config(dir_path: str) -> list[Testcase]:
    config_path = os.path.join(dir_path, Config.TEST_CONFIG)
    with open(config_path, encoding='utf-8') as file:
        test_config = json.loads(file.read())
    
    testcases = []
    for test_data in test_config:
        testcases.append(Testcase(test_data))
    
    return test_config

def listdir(path: str, regex: str):
    p = re.compile(regex)
    return [ name for name in os.listdir(path) if p.match(name) ]

def run_test(testcase_path: str, stdin: str, stdout: str, stats: Statistics) -> dict[str, int]:
    """Here we run testcase with subprocess by using compiler and running virtual machine"""

def run_tests(dir_path: str, stats: Statistics):
    test_config = read_test_config(dir_path)
    for test in test_config:
        run_test(os.path.join(dir_path, test.filename), test.stdin, test.stdout, stats)
    
    


    
    