from sly import Lexer


class GebalangLexer(Lexer):
    tokens = {PROCEDURE, PROGRAM, IS, VAR, BEGIN, END, LPAR, RPAR,
              IF, THEN, ELSE, ENDIF,
              WHILE, DO, ENDWHILE,
              REPEAT, UNTIL,
              READ, WRITE,
              ARIT_OP, COND_OP,
              NUM, ID, COMMA, SEMICOLON, ASSIGN}

    ignore = " \t"
    ignore_comment = r"\[(.|\n)*?\]"
    ignore_newline = r"\n"
    PROCEDURE = r"PROCEDURE"
    PROGRAM = r"PROGRAM"
    IS = r"IS"
    VAR = r"VAR"
    BEGIN = r"BEGIN"
    ENDWHILE = r"ENDWHILE"
    ENDIF = r"ENDIF"
    END = r"END"
    IF = r"IF"
    THEN = r"THEN"
    ELSE = r"ELSE"
    WHILE = r"WHILE"
    DO = r"DO"
    REPEAT = r"REPEAT"
    UNTIL = r"UNTIL"
    READ = r"READ"
    WRITE = r"WRITE"
    ASSIGN = r":="
    ARIT_OP = r"\+|-|\*|/|%"
    COND_OP = r">=|<=|>|<|!=|="
    ID = r"[_a-z]+"
    NUM = r"[0-9]+"
    COMMA = r","
    SEMICOLON = r";"
    LPAR = r"\("
    RPAR = r"\)"

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        raise Exception("Bad Character")
