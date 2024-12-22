import enum
from dataclasses import dataclass
from typing import Union


class TAC(enum.Enum):
    # commands
    READ = "READ"
    WRITE = "WRITE"
    PARAM = "PARAM"
    LOCAL = "LOCAL"
    RETURN = "RETURN"
    CALL = "CALL"
    SCALL = "SCALL"
    # flow
    IFGOTO = "IFGOTO"
    GOTO = "GOTO"
    # others
    ASSIGN = "ASSIGN"
    LABEL = "LABEL"


@dataclass
class Quadruple:
    type: TAC
    op: str = ""
    arg1: str = ""
    arg2: Union[str, list[str]] = ""
    res: str = ""
    label: str = ""


class LabelTAC(Quadruple):
    def __init__(self, label: str):
        super().__init__(type=TAC.LABEL, label=label)


class ReadTAC(Quadruple):
    def __init__(self, arg: str, label: str = ""):
        super().__init__(type=TAC.READ, op=TAC.READ.name, arg1=arg, label=label)


class WriteTAC(Quadruple):
    def __init__(self, arg: str, label: str = ""):
        super().__init__(type=TAC.WRITE, op=TAC.WRITE.name, arg1=arg, label=label)


""" ======================= FUNCTIONS TAC ======================= """


class ParamTAC(Quadruple):
    def __init__(self, arg: str, label: str = ""):
        super().__init__(type=TAC.PARAM, op=TAC.PARAM.name, arg1=arg, label=label)


class LocalTAC(Quadruple):
    def __init__(self, arg: str, label: str = ""):
        super().__init__(type=TAC.LOCAL, op=TAC.LOCAL.name, arg1=arg, label=label)


class ReturnTAC(Quadruple):
    def __init__(self, label: str = ""):
        super().__init__(type=TAC.RETURN, op=TAC.RETURN.name, label=label)


class CallTAC(Quadruple):
    def __init__(self, arg: str, params: list[str], label: str = ""):
        super().__init__(type=TAC.CALL, op=TAC.CALL.name, arg1=arg, arg2=params, label=label)


class SCallTAC(Quadruple):
    def __init__(self, arg: str, params: list[str], label: str = ""):
        super().__init__(type=TAC.SCALL, op=TAC.SCALL.name, arg1=arg, arg2=params, label=label)


""" ==================== FUNCTIONS TAC END ====================== """


class GotoTAC(Quadruple):
    def __init__(self, res: str, label: str = ""):
        super().__init__(type=TAC.GOTO, res=res, label=label)


class AssignTAC(Quadruple):
    def __init__(self, res: str, arg1: str, op: str = "", arg2: str = "", label: str = ""):
        super().__init__(type=TAC.ASSIGN, res=res, arg1=arg1, op=op, arg2=arg2, label=label)


class IfGotoTAC(Quadruple):
    def __init__(self, res: str, arg1: str, op: str, arg2: str, label: str = ""):
        super().__init__(type=TAC.IFGOTO, res=res, arg1=arg1, op=op, arg2=arg2, label=label)


def get_tac_repr(tac: Quadruple, label_pad: int):
    label = tac.label.ljust(label_pad)
    if tac.type == TAC.SCALL:
        right_side = f"SCALL {tac.arg1}({', '.join(tac.arg2)})"
    if tac.type == TAC.CALL:
        right_side = f"CALL {tac.arg1}({', '.join(tac.arg2)})"
    elif tac.type == TAC.IFGOTO:
        right_side = f"IF {tac.arg1} {tac.op} {tac.arg2} GOTO {tac.res}"
    elif tac.type == TAC.GOTO:
        right_side = f"GOTO {tac.res}"
    elif tac.type == TAC.ASSIGN:
        right_side = f"{tac.res} := {tac.arg1} {tac.op} {tac.arg2}"
    else:
        right_side = f"{tac.op} {tac.arg1} {tac.arg2}"
    return f"{label} | {right_side}"


def write_tac_to_file(tacs: dict[str, list[Quadruple]], path: str):
    max_label = 0
    for proc in tacs:
        proc_tacs = tacs[proc]
        for tac in proc_tacs:
            max_label = max(max_label, len(tac.label))

    text = ""
    for proc in tacs:
        proc_tacs = tacs[proc]
        text += f"{'=' * (max_label + 2)} {proc} {'=' * (max_label + 2)}\n"
        for tac in proc_tacs:
            text += f"{get_tac_repr(tac, max_label)}\n"

    with open(path, 'w+') as file:
        file.write(text)
