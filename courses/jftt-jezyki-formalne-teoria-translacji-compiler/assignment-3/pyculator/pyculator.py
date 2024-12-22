from lexer import CalcLexer
from parser import CalcParser

def main():
    lexer = CalcLexer()
    parser = CalcParser()

    while True:
        try:
            result_text = ""
            text = input('')
            while len(text) > 0 and text[-1] == "\\":
                result_text += text[:-1]
                text = input('')
            result_text += text + "\n"
        except EOFError:
            break
        else:
            parser.parse(lexer.tokenize(result_text))

if __name__ == '__main__':
    main()