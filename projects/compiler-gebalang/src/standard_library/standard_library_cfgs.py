from ..translator.Flags import Flag
from ..common.cfg_models import BasicBlock, VariableInfo
from ..common.tac_models import ReturnTAC, ParamTAC, LocalTAC
from ..common.commands import Command
from ..control_flow_graph.cfg import CFG
import os

from .commands_lexer import AssemblerLexer
from .commands_parser import AssemblerParser


def get_commands(path: str) -> list[Command]:
    with open(path, encoding='utf-8') as file:
        text = file.read()
    lexer = AssemblerLexer()
    parser = AssemblerParser()
    parser.parse(lexer.tokenize(text))
    return parser.commands


def get_mul(commands: list[Command]) -> CFG:
    cfg = CFG("!mul", [], False)
    bb = BasicBlock(0, [ParamTAC("$ret"), ParamTAC("a"), ParamTAC("b"), ParamTAC("p"),
                        ReturnTAC()])
    bb.set_commands(commands)
    cfg.nodes[0] = bb
    cfg.flags = {Flag.one}
    cfg.symbols = {
        "$ret": VariableInfo(True, 10),
        "a": VariableInfo(True, 11),
        "b": VariableInfo(True, 12),
        "p": VariableInfo(True, 13)
    }
    return cfg


def get_div(commands: list[Command]) -> CFG:
    cfg = CFG("!div", [], False)
    bb = BasicBlock(0, [ParamTAC("$ret"), ParamTAC("a"), ParamTAC("b"), ParamTAC("p"),
                        LocalTAC("temp"), LocalTAC("b_copy"), ReturnTAC()])
    bb.set_commands(commands)
    cfg.nodes[0] = bb
    cfg.symbols = {
        "$ret": VariableInfo(True, 10),
        "a": VariableInfo(True, 11),
        "b": VariableInfo(True, 12),
        "p": VariableInfo(True, 13),
        "temp": VariableInfo(False, 14),
        "b_copy": VariableInfo(False, 15)
    }
    return cfg


def get_mod(commands: list[Command]) -> CFG:
    cfg = CFG("!mod", [], False)
    bb = BasicBlock(0, [ParamTAC("$ret"), ParamTAC("a"), ParamTAC("b"), ParamTAC("p"),
                        LocalTAC("b_copy"), ReturnTAC()])
    bb.set_commands(commands)
    cfg.nodes[0] = bb
    cfg.symbols = {
        "$ret": VariableInfo(True, 10),
        "a": VariableInfo(True, 11),
        "b": VariableInfo(True, 12),
        "p": VariableInfo(True, 13),
        "b_copy": VariableInfo(False, 14)
    }
    return cfg


def get_standard_library() -> dict[str, CFG]:
    static_path = os.path.join(os.path.dirname(__file__), "static")
    return {
        "!mul": get_mul(get_commands(os.path.join(static_path, "mul.imp"))),
        "!div": get_div(get_commands(os.path.join(static_path, "new_div_3.imp"))),
        "!mod": get_mod(get_commands(os.path.join(static_path, "new_mod2.imp")))
    }
