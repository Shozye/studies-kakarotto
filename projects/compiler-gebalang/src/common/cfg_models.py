from dataclasses import dataclass

from ..common.commands import Command
from ..common.tac_models import Quadruple

@dataclass
class VariableInfo:
    is_param: bool
    id: int = 0

class BasicBlock:
    """Class represents block of code that always follows from first to last line without any jumps and branching"""
    index: int
    tacs: list[Quadruple]
    commands: list[Command]

    def __init__(self, index: int, tacs: list[Quadruple]):
        self.index = index
        self.tacs = tacs
        self.commands = []

    def __repr__(self):
        return f"BasicBlock(id={self.index}, len(tacs)={len(self.tacs)})"

    def set_commands(self, commands: list[Command]):
        self.commands = commands


class OutEdge:
    def __init__(self, if_true: int, if_false: int = -1, op: str = "", arg1: str = "", arg2: str = ""):
        self.if_true = if_true
        self.if_false = if_false
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2

    def outs(self) -> list[int]:
        return list(filter(lambda x: x != -1, [self.if_true, self.if_false]))

    def __repr__(self):
        if self.if_false != -1:
            return f"OutEdge({self.if_true}, {self.if_false})"
        return f"OutEdge({self.if_true})"


class ProceduralEdge:
    def __init__(self, proc1: str, node1: int, proc2: str):
        self.proc1 = proc1
        self.node1 = node1
        self.proc2 = proc2

    def __repr__(self):
        return f"ProceduralEdge( {self.proc1}, {self.node1} -> {self.proc2}) )"
