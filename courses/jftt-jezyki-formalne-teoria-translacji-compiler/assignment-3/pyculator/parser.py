from lexer import CalcLexer
from sly import Parser
from utils import *

P = 1234577

class CalcParser(Parser):
    tokens = CalcLexer.tokens
    errstr = ""

    precedence = (
        ('left', ADD, SUB),
        ('left', MUL, DIV),
        ('right', UMINUS),
        ('nonassoc', POW)
        )

    def __init__(self):
        self.notation = ""

    @_('line statement')
    def statement(self, p):
        pass

    @_('')
    def statement(self, p):
        pass
    
    @_('expr NEWLINE')
    def line(self, p):
        if self.errstr == "":
            print(f"Notation: {self.notation}\nResult: {p.expr}")
        else:
            print("Error: " + self.errstr)
        self.errstr = ""
        self.notation=""
    
    @_('expr ERR NEWLINE')
    def line(self, p):
        print("Blad")
        self.errstr = ""
        self.notation=""
    
    @_('ERR NEWLINE')
    def line(self, p):
        print("Blad")
        self.errstr = ""
        self.notation=""

    @_('NEWLINE')
    def line(self, p):
        pass

    @_('number')
    def expr(self, p):
        self.notation += f"{p.number} "
        return p.number
    
    @_('LBR expr RBR')
    def expr(self, p):
        return p.expr

    @_('SUB LBR expr RBR %prec UMINUS')
    def expr(self, p):
        return neg(p.expr)

    @_('expr ADD expr')
    def expr(self, p):
        self.notation += "+ "
        return add(p.expr0, p.expr1)
    
    @_('expr SUB expr')
    def expr(self, p):
        self.notation += "- "
        return sub(p.expr0, p.expr1)
    
    @_('expr MUL expr')
    def expr(self, p):
        self.notation += "* "
        return mul(p.expr0, p.expr1)

    @_('expr DIV expr')
    def expr(self, p):
        self.notation += "/ "
        if p.expr1 == 0:
            self.errstr = "Division by zero"
            return 1
        result = div(p.expr0, p.expr1)
        if result == -1:
            self.errstr = f"{p.expr1} is not invertible modulo {P-1}"
            return 1
        return result
    
    @_('expr POW powexpr')
    def expr(self, p):
        self.notation += "^ "
        return pow(p.expr, p.powexpr)
    
    @_('pownumber')
    def powexpr(self, p):
        self.notation += f"{p.pownumber} "
        return p.pownumber
    
    @_('LBR powexpr RBR')
    def powexpr(self, p):
        return p.powexpr

    @_('SUB LBR powexpr RBR %prec UMINUS')
    def powexpr(self, p):
        return neg(p.powexpr, P-1)

    @_('powexpr ADD powexpr')
    def powexpr(self, p):
        self.notation += "+ "
        return add(p.powexpr0, p.powexpr1, P-1)
    
    @_('powexpr SUB powexpr')
    def powexpr(self, p):
        self.notation += "- "
        return sub(p.powexpr0, p.powexpr1, P-1)

    @_('powexpr MUL powexpr')
    def powexpr(self, p):
        self.notation += "* "
        return mul(p.powexpr0, p.powexpr1, P-1)
    
    @_('powexpr DIV powexpr')
    def powexpr(self, p):
        self.notation += "/ "
        if p.powexpr1 == 0:
            self.errstr = "Division by zero"
            return 1
        result = div(p.powexpr0, p.powexpr1, P-1)
        if result == -1:
            self.errstr = f"{p.powexpr1} is not invertible modulo {P-1}"
            return 1
        return result

    @_('NUM')
    def number(self, p):
        return p.NUM % P
    
    @_('SUB number %prec UMINUS')
    def number(self, p):
        return neg(-p.number)

    @_('NUM')
    def pownumber(self, p):
        return p.NUM % (P-1)

    @_('SUB pownumber %prec UMINUS')
    def pownumber(self, p):
        return neg(-p.pownumber, P-1)   

    


