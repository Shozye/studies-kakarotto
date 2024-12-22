from sly import Parser

from ..common.commands import *
from .commands_lexer import AssemblerLexer


class AssemblerParser(Parser):
    tokens = AssemblerLexer.tokens
    commands: list[Command]

    def __init__(self):
        self.commands = []

    @_("lines")
    def program_all(self, p):
        self.commands = p.lines

    @_("lines line")
    def lines(self, p):
        p.lines.append(p.line)
        return p.lines

    @_("")
    def lines(self, p):
        return []

    @_("label command NEWLINE")
    def line(self, p):
        p.command.label = p.label
        return p.command

    @_("LABEL SEMICOLON")
    def label(self, p):
        return p.LABEL

    @_("")
    def label(self, p):
        return ""

    @_("GET ID")
    def command(self, p):
        return GET(p.ID)

    @_("PUT ID")
    def command(self, p):
        return PUT(p.ID)

    @_("LOAD ID")
    def command(self, p):
        return LOAD(p.ID)

    @_("STORE ID")
    def command(self, p):
        return STORE(p.ID)

    @_("LOADI ID")
    def command(self, p):
        return LOADI(p.ID)

    @_("STOREI ID")
    def command(self, p):
        return STOREI(p.ID)

    @_("ADD ID")
    def command(self, p):
        return ADD(p.ID)

    @_("SUB ID")
    def command(self, p):
        return SUB(p.ID)

    @_("ADDI ID")
    def command(self, p):
        return ADDI(p.ID)

    @_("SUBI ID")
    def command(self, p):
        return SUBI(p.ID)

    @_("SET ID")
    def command(self, p):
        return SET(p.ID)

    @_("HALF")
    def command(self, p):
        return HALF()

    @_("JUMP LABEL")
    def command(self, p):
        return JUMP(p.LABEL)

    @_("JPOS LABEL")
    def command(self, p):
        return JPOS(p.LABEL)

    @_("JZERO LABEL")
    def command(self, p):
        return JZERO(p.LABEL)

    @_("JUMPI ID")
    def command(self, p):
        return JUMPI(p.ID)

    @_("HALT")
    def command(self, p):
        return HALT()
