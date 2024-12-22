from typing import Callable

from ..common.cfg_models import BasicBlock
from ..control_flow_graph.cfg import CFG
from .Flags import Flag
from ..common.commands import *
from ..common.tac_models import Quadruple, TAC


class ProcedureTranslator:
    commands: list[Command]

    def __init__(self, proc: str, cfg: CFG):
        self.name = proc
        self.cfg = cfg
        self.commands = []

    def run(self):
        for bb in self.cfg.nodes.values():
            self._translate_bb(bb)

    def _translate_bb(self, bb: BasicBlock):
        func_mapping: dict[TAC, Callable] = {
            TAC.PARAM: self._pass_, TAC.LOCAL: self._pass_,
            TAC.READ: self._read, TAC.WRITE: self._write,
            TAC.SCALL: self._scall, TAC.CALL: self._call,
            TAC.RETURN: self._return_,
            TAC.IFGOTO: self._ifgoto, TAC.GOTO: self._goto,
            TAC.ASSIGN: self._assign
        }

        self.commands = []
        for tac in bb.tacs:
            func_mapping[tac.type](tac)
        bb.set_commands(self.commands)

    def _pass_(self, tac: Quadruple):
        pass

    def _read(self, tac: Quadruple):
        if self._is_param(tac.arg1):
            self.commands.extend([GET("*storage_0*", tac.label), STOREI(tac.arg1)])
        else:
            self.commands.extend([GET(tac.arg1, tac.label)])

    def _write(self, tac: Quadruple):
        if tac.arg1.isdecimal():
            self.commands.extend([SET(tac.arg1, tac.label), PUT("*storage_0*")])
        elif self._is_param(tac.arg1):
            self.commands.extend([LOADI(tac.arg1, tac.label), PUT("*storage_0*")])
        else:
            self.commands.extend([PUT(tac.arg1, tac.label)])

    def _call(self, tac: Quadruple):
        self.commands.extend([SET(tac.arg2[0], tac.label),
                              STORE(f"#{tac.arg1}#{0}#")])
        for i, arg in enumerate(tac.arg2[1:], start=1):
            self.commands.extend([LOAD(arg) if self._is_param(arg) else SET(arg),
                                  STORE(f"#{tac.arg1}#{i}#")])
        self.commands.extend([JUMP(f"#{tac.arg1}#")])

    def _scall(self, tac: Quadruple):
        ret, a, b, p = tac.arg2
        self.commands.extend([SET(ret, tac.label),
                              STORE(f"#{tac.arg1}#{0}#")])
        for i, arg in enumerate([a, b], start=1):
            self.commands.extend(
                [
                    SET(arg) if arg.isdecimal() else self._GEN_LOAD(arg),
                    STORE(f"#{tac.arg1}#{i}#")
                ]
            )

        self.commands.extend([LOAD(p) if self._is_param(p) else SET(p),
                              STORE(f"#{tac.arg1}#{3}#")])
        self.commands.extend([JUMP(f"#{tac.arg1}#")])

    def _assign(self, tac: Quadruple):
        {"+": self._add, "-": self._sub, "*": self._mul,
         "/": self._div, "%": self._mod, "": self._nothing}[tac.op](tac)

    def _nothing(self, tac: Quadruple):
        self.commands.extend([
            SET(tac.arg1, tac.label) if tac.arg1.isdecimal() else self._GEN_LOAD(tac.arg1, tac.label),
            self._GEN_STORE(tac.res)
        ])

    def _add(self, tac: Quadruple):
        self.commands.extend([
            SET(tac.arg2, tac.label) if tac.arg2.isdecimal() else self._GEN_LOAD(tac.arg2, tac.label),
            self._GEN_ADD(tac.arg1),
            self._GEN_STORE(tac.res)
        ])

    def _sub(self, tac: Quadruple):
        if tac.arg2.isdecimal() and tac.arg2 == "1":
            self.cfg.flags.add(Flag.one)
            self.commands.extend([self._GEN_LOAD(tac.arg1, tac.label),
                                  self._GEN_SUB("*const_1*")])
        elif tac.arg2.isdecimal():
            self.commands.extend([SET(tac.arg2, tac.label),
                                  STORE("*storage_1*"),
                                  self._GEN_LOAD(tac.arg1),
                                  self._GEN_SUB("*storage_1*")])
        else:
            self.commands.extend([self._GEN_LOAD(tac.arg1, tac.label),
                                  self._GEN_SUB(tac.arg2)])
        self.commands.extend([self._GEN_STORE(tac.res)])

    def _mul(self, tac: Quadruple):
        if tac.arg2 == "2":
            self.commands.extend([self._GEN_LOAD(tac.arg1, tac.label),
                                  ADD("*storage_0*"),
                                  self._GEN_STORE(tac.res)])
        else:
            print("fucked up")

    def _div(self, tac: Quadruple):
        if tac.arg2 == "2":
            self.commands.extend([self._GEN_LOAD(tac.arg1, tac.label),
                                  HALF(),
                                  self._GEN_STORE(tac.res)])
        else:
            print("fucked up")

    def _mod(self, tac: Quadruple):
        if tac.arg2 == "2":
            self.commands.extend([self._GEN_LOAD(tac.arg1, tac.label),
                                  HALF(),
                                  ADD("*storage_0*"),
                                  STORE("*storage_1*"),
                                  self._GEN_LOAD(tac.arg1),
                                  SUB("*storage_1*"),
                                  self._GEN_STORE(tac.res)])
        else:
            print("fucked up")

    def _ifgoto(self, tac: Quadruple):
        {">": self._grt, "<": self._les, ">=": self._geq, "<=": self._leq, "=": self._eq}[tac.op](tac)

    def _goto(self, tac: Quadruple):
        self.commands.extend([JUMP(tac.res, tac.label)])

    def _return_(self, tac: Quadruple):
        self.commands.extend([HALT(tac.label) if self.name == "MAIN" else JUMPI("$ret", tac.label)])

    def _is_param(self, arg: str) -> bool:
        if arg.startswith("*"):
            return False
        return self.cfg.symbols[arg].is_param

    def _GEN(self, commandi, command, arg: str, label: str) -> Command:
        return commandi(arg, label) if self._is_param(arg) else command(arg, label)

    def _GEN_SUB(self, arg: str, label: str = "") -> Command:
        return self._GEN(SUBI, SUB, arg, label)

    def _GEN_ADD(self, arg: str, label: str = "") -> Command:
        return self._GEN(ADDI, ADD, arg, label)

    def _GEN_LOAD(self, arg: str, label: str = "") -> Command:
        return self._GEN(LOADI, LOAD, arg, label)

    def _GEN_STORE(self, arg: str, label: str = "") -> Command:
        return self._GEN(STOREI, STORE, arg, label)

    def _ADD_ONE(self) -> Command:
        self.cfg.flags.add(Flag.one)
        return ADD("*const_1*")

    def _eq(self, tac: Quadruple):
        if tac.arg2 != "0":
            print('its fucked up')
        self.commands.extend([
            self._GEN_LOAD(tac.arg1, tac.label),
            JZERO(tac.res)
        ])

    def _les(self, tac: Quadruple):
        self.commands.extend([
            SET(tac.arg2, tac.label) if tac.arg2.isdecimal() else self._GEN_LOAD(tac.arg2, tac.label),
            self._GEN_SUB(tac.arg1),
            JPOS(tac.res)])

    def _geq(self, tac: Quadruple):
        self.commands.extend([
            SET(tac.arg2, tac.label) if tac.arg2.isdecimal() else self._GEN_LOAD(tac.arg2, tac.label),
            self._GEN_SUB(tac.arg1),
            JZERO(tac.res)])

    def _grt(self, tac: Quadruple, add_label: bool = True):
        label = tac.label if add_label else ""
        if tac.arg2.isdecimal():
            self.commands.extend([SET(tac.arg2, label),
                                  self._ADD_ONE(),
                                  self._GEN_SUB(tac.arg1),
                                  JZERO(tac.res)])
        else:
            self.commands.extend([self._GEN_LOAD(tac.arg1, label),
                                  self._GEN_SUB(tac.arg2),
                                  JPOS(tac.res)])

    def _leq(self, tac: Quadruple):
        if tac.arg2.isdecimal():
            self.commands.extend([SET(tac.arg2, tac.label),
                                  self._ADD_ONE(),
                                  self._GEN_SUB(tac.arg1),
                                  JPOS(tac.res)])
        else:
            self.commands.extend([self._GEN_LOAD(tac.arg1, tac.label),
                                  self._GEN_SUB(tac.arg2),
                                  JZERO(tac.res)])
