import sys
from collections import defaultdict
    
    

def compute_prefix_function(pattern):
    i = 1
    j = 0
    res = [0] * len(pattern)
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            res[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            # here we have to backtrack to previous
            j = res[j-1]
        else:
            #here suffix start and prefix start do not match so
            # lps[i] = 0 and we move suffix start further
            res[i] = 0
            i += 1
    return res

class DFA:
    def __init__(self, pattern):
        self.state = -1
        self.end_state = len(pattern)-1
        self.delta = self.calculate_delta(pattern)
        
    def calculate_delta(self, pattern: str):
        alphabet = list(set(pattern))
        LPS = compute_prefix_function(pattern)
        delta = dict()
        for state in range(-1, self.end_state):
            for letter in list(set(pattern)):
                if pattern[state + 1] == letter:
                    delta[state, letter] = state+1
                elif state + 1 == 0:
                    delta[state, letter] = -1
                else:
                    delta[state, letter] = delta[LPS[state]-1, letter]
                        
        # now i have to calculate for state == end_state
        for letter in alphabet:
            delta[self.end_state, letter] = delta[LPS[self.end_state]-1, letter]
        return delta
    
    def is_in_accepting_state(self) -> bool:
        return self.state == self.end_state
    
    def parse_letter(self, letter: str):
        self.state = self.delta.get((self.state, letter), -1)
        
def fa(text, pattern):
    answers = []
    dfa = DFA(pattern)
    for i, c in enumerate(text):
        dfa.parse_letter(c)
        if(dfa.is_in_accepting_state()):
            answers.append(i-len(pattern) + 1)
    return answers
            
def main():
    if len(sys.argv) < 3:
        print("Expected 3 arguments")
        sys.exit(1)
    pattern = sys.argv[1]
    filename = sys.argv[2]
    with open(filename, encoding='utf-8') as file:
        text = file.read()
    print(fa(text, pattern))
    
    
if __name__ == "__main__":
    main()
