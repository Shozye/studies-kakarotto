from sly import Lexer


class AssemblerLexer(Lexer):
    tokens = {GET, PUT,
              LOAD, STORE, LOADI, STOREI,
              ADD, SUB, ADDI, SUBI, SET, HALF,
              JUMP, JPOS, JZERO, JUMPI,
              HALT, NEWLINE, ID, SEMICOLON, LABEL}

    ignore = " \t"
    ignore_comment = r"\[(.|\n)*?\]"

    @_(r"\n")
    def NEWLINE(self, t):
        self.lineno += 1
        return t

    GET = r"GET"
    PUT = r"PUT"

    LOADI = r"LOADI"
    STOREI = r"STOREI"
    ADDI = r"ADDI"
    SUBI = r"SUBI"
    JUMPI = r"JUMPI"

    LOAD = r"LOAD"
    STORE = r"STORE"

    ADD = r"ADD"
    SUB = r"SUB"
    SET = r"SET"
    HALF = r"HALF"

    JUMP = r"JUMP"
    JPOS = r"JPOS"
    JZERO = r"JZERO"

    HALT = r"HALT"

    ID = r"[\*\$_a-z0-9]+"
    SEMICOLON = r":"
    LABEL = r"E_[_A-Za-z0-9]*"


