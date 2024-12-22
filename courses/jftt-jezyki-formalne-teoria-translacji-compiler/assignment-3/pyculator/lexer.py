from sly import Lexer

class CalcLexer(Lexer):
    tokens = {NUM, LBR, RBR, ADD, SUB, MUL, DIV, POW, ERR, NEWLINE}
    ignore = ' \t'
    ignore_comment = r'^\#(.|\\\n)*\n'
    ignore_backslashed_newline = r'\\\n'
    literals = { '+', '-', '*', '/', '^', '(', ')' }

    NEWLINE = r'\n'
    NUM = r'\d+'
    LBR = r'\('
    RBR = r'\)'
    ADD = r'\+'
    SUB = r'-'
    MUL = r'\*'
    DIV = r'/'
    POW = r'\^'
    ERR = '.+'

    def NUM(self, t):
        t.value = int(t.value)
        return t

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

def main():
    lexer = CalcLexer()
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
            for token in lexer.tokenize(result_text):
                print(token)


if __name__ == '__main__':
    main()