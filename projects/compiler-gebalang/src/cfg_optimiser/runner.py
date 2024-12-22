from .DeadCodeRemover import DeadCodeRemover
from .ProcedureInliner import ProcedureInliner
from ..control_flow_graph.cfg import ICFG



def optimise_icfg(icfg: ICFG):
    DeadCodeRemover(icfg).optimise()
    ProcedureInliner(icfg).inline()
