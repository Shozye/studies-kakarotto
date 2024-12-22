from sly import Parser

from .gebalang_lexer import GebalangLexer
from .labels import Labels
from ..common.tac_models import (
    AssignTAC,
    IfGotoTAC, GotoTAC,
    WriteTAC, ReadTAC, CallTAC, ReturnTAC, LocalTAC, ParamTAC, Quadruple, LabelTAC, SCallTAC, TAC
)
from .parser_returntypes import P
from .parser_utils import BinaryArithmeticOperation, BinaryLogicOperation


class GebalangParser(Parser):
    tokens = GebalangLexer.tokens
    tac: dict[str, list[Quadruple]]

    def __init__(self):
        self.tac = {}
        self.labels = Labels()
        self.function_names = {
            "*": "!mul",
            "/": "!div",
            "%": "!mod"
        }

    @_('procedures main')
    def program_all(self, p: P):
        self.tac = p.procedures
        self.tac.update(p.main)
        for proc_name in self.tac:
            self.tac[proc_name] = list(filter(lambda x: x is not None, self.tac[proc_name]))

    @_('main')
    def program_all(self, p: P):
        """This is program without any procedures"""
        self.tac = p.main

    @_('procedures procedure')
    def procedures(self, p: P) -> dict[str, list[Quadruple]]:
        _tac = p.procedures
        _tac.update(p.procedure)
        return _tac

    @_('procedure')
    def procedures(self, p: P) -> dict[str, list[Quadruple]]:
        return p.procedure

    @_('PROCEDURE proc_head IS local_variables BEGIN commands END')
    def procedure(self, p: P) -> dict[str, list[Quadruple]]:
        """This procedure should somehow connect proc_head with declarations and commands together"""
        name, declarations = p.proc_head
        _tac = [ParamTAC("$ret")]
        _tac.extend((ParamTAC(declaration) for declaration in declarations))
        _tac.extend((LocalTAC(var) for var in p.local_variables))
        _tac.extend(p.commands)
        _tac.append(ReturnTAC())
        return {name: _tac}

    @_('PROGRAM IS local_variables BEGIN commands END')
    def main(self, p: P) -> dict[str, list[Quadruple]]:
        _tac = []
        _tac.extend((LocalTAC(var) for var in p.local_variables))
        _tac.extend(p.commands)
        _tac.append(ReturnTAC())
        return {"MAIN": _tac}

    @_('VAR declarations')
    def local_variables(self, p: P) -> list[str]:
        return p.declarations

    @_('')
    def local_variables(self, p) -> list[str]:
        return []

    @_('commands command')
    def commands(self, p: P) -> list[Quadruple]:
        _tac = p.commands
        _tac.extend(p.command)
        return _tac

    @_('command')
    def commands(self, p: P) -> list[Quadruple]:
        """Shouldn't it be the same as command"""
        return p.command

    @_('IF condition THEN commands ELSE commands ENDIF')
    def command(self, p: P) -> list[Quadruple]:
        _, ifgoto_false, _, if_false_etiquette = p.condition
        ifclosed_etiquette = self.labels.get()
        return [
            *ifgoto_false,
            *p.commands0,  # start if body
            GotoTAC(ifclosed_etiquette),  # end if body
            LabelTAC(if_false_etiquette),  # start else body
            *p.commands1,  # else body
            LabelTAC(ifclosed_etiquette)  # end if else
        ]

    @_('IF condition THEN commands ENDIF')
    def command(self, p: P) -> list[Quadruple]:
        _, ifgoto_false, _, if_false_etiquette = p.condition
        return [
            *ifgoto_false,  # go to after if, if condition is false
            *p.commands,  # if body
            LabelTAC(if_false_etiquette)  # after if
        ]

    @_('WHILE condition DO commands ENDWHILE')
    def command(self, p: P) -> list[Quadruple]:
        ifgoto_true, ifgoto_false, if_true_etiquette, if_false_etiquette = p.condition
        return [
            *ifgoto_false,  # go to after while if condition false
            LabelTAC(if_true_etiquette),  # while body start
            *p.commands,  # while body
            *ifgoto_true,  # goto body start if condition true
            LabelTAC(if_false_etiquette)  # endwhile
        ]

    @_('REPEAT commands UNTIL condition SEMICOLON')
    def command(self, p: P) -> list[Quadruple]:
        _, ifgoto_false, _, if_false_etiquette = p.condition
        return [
            LabelTAC(if_false_etiquette),  # repeat-until body start
            *p.commands,  # repeat-until body
            *ifgoto_false  # if condition is false then go to beginning of loop
        ]

    @_('proc_head SEMICOLON')
    def command(self, p: P) -> list[Quadruple]:
        return_etiquette = self.labels.get()
        name, args = p.proc_head
        return [
            CallTAC(name, [return_etiquette] + args),
            LabelTAC(return_etiquette)
        ]

    @_('ID ASSIGN expression SEMICOLON')
    def command(self, p: P) -> list[Quadruple]:
        if p.expression[0].isdecimal() and p.expression[2].isdecimal():
            return_etiquette = self.labels.get()
            return [
                SCallTAC(self.function_names[p.expression[1]],
                         [return_etiquette, p.expression[0], p.expression[2], p.ID]),
                LabelTAC(return_etiquette)
            ]

        if any([p.expression[1] in ["+", "-", ""],
                p.expression[1] in ["*", "/", "%"] and p.expression[2] == "2"]):
            return [AssignTAC(p.ID, *p.expression)]

        return_etiquette = self.labels.get()
        return [
            SCallTAC(self.function_names[p.expression[1]], [return_etiquette, p.expression[0], p.expression[2], p.ID]),
            LabelTAC(return_etiquette)
        ]

    @_('READ ID SEMICOLON')
    def command(self, p: P) -> list[Quadruple]:
        return [ReadTAC(p.ID)]

    @_('WRITE value SEMICOLON')
    def command(self, p: P) -> list[Quadruple]:
        return [WriteTAC(p.value)]

    @_('ID LPAR declarations RPAR')
    def proc_head(self, p: P) -> tuple[str, list[str]]:
        return p.ID, p.declarations

    @_('declarations COMMA ID')
    def declarations(self, p: P) -> list[str]:
        decs = p.declarations
        return decs + [p.ID]

    @_('ID')
    def declarations(self, p: P) -> list[str]:
        return [p.ID]

    @_('value')
    def expression(self, p: P) -> tuple[str, str, str]:
        return p.value, "", ""

    @_('value ARIT_OP value')
    def expression(self, p: P) -> tuple[str, str, str]:
        bin_op = BinaryArithmeticOperation(p.value0, p.ARIT_OP, p.value1)
        # Only variable cases cannot be optimised during arithmetic operations
        return bin_op.get_tuple()

    @_('value COND_OP value')
    def condition(self, p: P) -> tuple[list[Quadruple], list[Quadruple], str, str]:
        bin_op = BinaryLogicOperation(p.value0, p.COND_OP, p.value1)

        if_true_etiquette = self.labels.get()
        if_false_etiquette = self.labels.get()

        if bin_op.op in ["=", "!="]:
            les_bin_op = BinaryLogicOperation(bin_op.val0, "<", bin_op.val1)
            leq_bin_op = BinaryLogicOperation(bin_op.val0, "<=", bin_op.val1)
            gre_bin_op = BinaryLogicOperation(bin_op.val0, ">", bin_op.val1)
            jump_over_etiquette = self.labels.get()
            if bin_op.op == "=":
                ifgoto_true = [IfGotoTAC(jump_over_etiquette, *les_bin_op.get_tuple()),
                               IfGotoTAC(if_true_etiquette, *leq_bin_op.get_tuple()),
                               LabelTAC(jump_over_etiquette)]
                ifgoto_false = [IfGotoTAC(if_false_etiquette, *les_bin_op.get_tuple()),
                                IfGotoTAC(if_false_etiquette, *gre_bin_op.get_tuple())]
            else:  # !=
                ifgoto_false = [IfGotoTAC(jump_over_etiquette, *les_bin_op.get_tuple()),
                                IfGotoTAC(if_false_etiquette, *leq_bin_op.get_tuple()),
                                LabelTAC(jump_over_etiquette)]
                ifgoto_true = [IfGotoTAC(if_true_etiquette, *les_bin_op.get_tuple()),
                               IfGotoTAC(if_true_etiquette, *gre_bin_op.get_tuple())]
        else:
            ifgoto_true = [IfGotoTAC(if_true_etiquette, *bin_op.get_tuple())]

            bin_op.negate()
            bin_op.optimise()
            ifgoto_false = [IfGotoTAC(if_false_etiquette, *bin_op.get_tuple())]

        real_ifgoto_true = []
        real_ifgoto_false = []
        for tac in ifgoto_true:
            if tac.type == TAC.LABEL:
                real_ifgoto_true.append(tac)
            elif tac.arg1 == "1":
                real_ifgoto_true.append(GotoTAC(tac.res))
            elif tac.arg1 == "0":
                pass
            else:
                real_ifgoto_true.append(tac)

        for tac in ifgoto_false:
            if tac.type == TAC.LABEL:
                real_ifgoto_false.append(tac)
            elif tac.arg1 == "1":
                real_ifgoto_false.append(GotoTAC(tac.res))
            elif tac.arg1 == "0":
                pass
            else:
                real_ifgoto_false.append(tac)
        return real_ifgoto_true, real_ifgoto_false, if_true_etiquette, if_false_etiquette

    @_('NUM')
    def value(self, p: P) -> str:
        return p.NUM

    @_('ID')
    def value(self, p: P) -> str:
        return p.ID
