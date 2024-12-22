import sys


def compute_prefix_function(pattern):
    i = 1
    j = 0
    res = [0] * len(pattern)
    # Zlozonosc to O(n), bo if + else wykona sie max len(pattern) razy
    # natomiast elif wykonuje sie gdy j > 0, a j zwiekszamy maksymalnie len(pattern) razy
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


def kmp(text: str, pattern: str) -> list:
    i,j = 0,0
    answers = []
    LPS = compute_prefix_function(pattern)
    while(i < len(text)):
        if(text[i] == pattern[j]):
            i+=1
            j+=1
            if j == len(pattern):
                answers.append(i-j)
                j = LPS[j-1]
        elif j > 0:
            j = LPS[j-1]
        else:
            i+=1
    return answers
    
    


def main():
    if len(sys.argv) < 3:
        print("Expected 3 arguments")
        sys.exit(1)
    pattern = sys.argv[1]
    filename = sys.argv[2]
    with open(filename, encoding='utf-8') as file:
        text = file.read()
    print(kmp(text, pattern))


if __name__ == "__main__":
    main()
