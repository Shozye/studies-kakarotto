from .merger import Merger
from .symbol_filler import SymbolFiller
from ..common.commands import Command
from ..control_flow_graph.cfg import ICFG


def merge(icfg: ICFG) -> list[Command]:
    filler = SymbolFiller(icfg)
    filler.allocate_symbols()
    filler.fill_symbols()

    merger = Merger(icfg)
    merger.merge()
    return merger.merged_commands
