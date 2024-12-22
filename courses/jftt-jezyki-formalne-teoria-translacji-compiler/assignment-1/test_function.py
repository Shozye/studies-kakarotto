import sys
import json
from FA import fa
from KMP import kmp

def parse_tests(filename) -> dict:
    with open(filename, encoding='utf-8') as file:
        lines = file.read().split("\n")[:-1]
    tests = dict()
    for line in lines:
        _, test, answers = line.split("'")
        tests[test] = json.loads(answers)
    return tests    
    
def main():
    if(len(sys.argv) < 3):
        print("Needed 3 arguments")
        sys.exit(1)
    text_file = sys.argv[1]
    tests_file = sys.argv[2]
    
    with open(text_file, encoding='utf-8') as file:
        text = file.read()
    tests = parse_tests(tests_file)
    
    
    for test, answer in tests.items():
        print("###############")
        print(f"Making test: {test}")
        fa_match = fa(text, test) == answer
        kmp_match = kmp(text, test) == answer
        if(fa_match and kmp_match):
            print("KMP and FA matched with answer")
        else:
            print("KMP OR FA didn't match with answer")
            print(f"Expected answer", answer)
            print(f"fa(text, {test}) == answer ? ", fa_match)
            print("FA: ", fa(text, test))
            print(f"kmp(text, {test}) == answer ? ", kmp_match)
            print("KMP: ", kmp(text, test))
    


if __name__ == "__main__":
    main()