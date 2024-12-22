from ..standard_library.standard_library_cfgs import get_standard_library
from ..common.cfg_models import VariableInfo
from ..common.tac_models import Quadruple, TAC
from .cfg import ICFG


def fill_symbols(icfg: ICFG):
    for proc_name, cfg in icfg.cfgs.items():
        if proc_name.startswith("!"):
            continue
        for tac in cfg.nodes[0].tacs:
            if tac.type not in [TAC.PARAM, TAC.LOCAL]:
                break
            cfg.symbols[tac.arg1] = VariableInfo(tac.type == TAC.PARAM)


def get_icfg(tacs: dict[str, list[Quadruple]]) -> ICFG:
    icfg = ICFG(tacs, get_standard_library())
    fill_symbols(icfg)
    return icfg
