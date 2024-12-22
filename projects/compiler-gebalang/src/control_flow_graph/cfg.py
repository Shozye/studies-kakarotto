from typing import Optional

from ..common.cfg_models import VariableInfo
from ..common.cfg_models import BasicBlock, OutEdge, ProceduralEdge
from ..common.tac_models import Quadruple, TAC
from collections import defaultdict


def _get_leaders(tacs: list[Quadruple]) -> list[int]:
    """Leaders are the starting points of basic blocks. TAC is a leader iff it is one of the following:
    1. The first statement of program or procedure.
    2. Statement that is target of a conditional or unconditional GOTO statement # every target has label
    3. Statement that immediately follows a conditional or unconditional GOTO statement
    4. Statement that immediately follows a method invocation statement # all of them have return label
    credits. page 423"""
    leaders = set()
    leaders_label = []
    labels = dict()
    for i, tac in enumerate(tacs):
        if not leaders:
            leaders.add(i)  # 1.
        if tac.type in [TAC.CALL, TAC.SCALL]:
            leaders.add(i + 1)  # 4.
        if tac.type in [TAC.GOTO, TAC.IFGOTO]:
            leaders.add(i + 1)  # 3
            leaders_label.append(tac.res)  # 2a.

        if tac.label:
            labels[tac.label] = i  # helper to 2
    for label in leaders_label:
        leaders.add(labels[label])  # 2b.

    return sorted(list(leaders))


class CFG:
    """Class represents Procedure Control Flow Graph of one process
    credits: https://www.researchgate.net/publication/273445077_Designing_and_Implementing_Control_Flow_Graph_for_Magic_4th_Generation_Language"""
    nodes: dict[int, BasicBlock]  # basic blocks with their indexes
    edges: dict[int, OutEdge]  # edge is between two basic blocks id's
    outer_procedural_edges: dict[int, str]  # edge is between block_id and procedure_name
    symbols: dict[str, VariableInfo]
    backtrack_edges: dict[int, list[int]]
    name: str

    def __init__(self, name: str, tacs: list[Quadruple], initialize=True):
        """ We make CFG by finding leaders of TAC, and then we create basic blocks by
        starting with leader and extending up to the next leader.
        @param tacs: list of tacs that start with proc_start and end with ReturnTAC
        """
        self.name = name
        self.nodes = {}
        self.edges = {}
        self.outer_procedural_edges = dict()
        self.symbols = dict()
        self.flags = set()
        self.backtrack_edges = defaultdict(list)
        if initialize:
            self._make_nodes(tacs)
            self._fill_edges()
            self._fill_backtrack_edges()

    def _fill_backtrack_edges(self):
        for start, out_edge in self.edges.items():
            for endpoint in out_edge.outs():
                self.backtrack_edges[endpoint].append(start)

    def _fill_edges(self):
        start_label_to_basic_block = {}
        for i, node in self.nodes.items():
            label = node.tacs[0].label
            if label:
                start_label_to_basic_block[label] = i

        for i, node in self.nodes.items():
            last = node.tacs[-1]
            if last.type == TAC.RETURN:
                pass
            elif last.type == TAC.IFGOTO:
                self.edges[i] = OutEdge(start_label_to_basic_block[last.res], i + 1, last.op, last.arg1, last.arg2)
            elif last.type == TAC.GOTO:
                self.edges[i] = OutEdge(start_label_to_basic_block[last.res])
            elif last.type in [TAC.CALL, TAC.SCALL]:
                self.edges[i] = OutEdge(i + 1)
                self.outer_procedural_edges[i] = last.arg1
            else:
                self.edges[i] = OutEdge(i + 1)  # case when there was some loop

    def _make_nodes(self, tacs: list[Quadruple]):
        leaders = _get_leaders(tacs)
        for i, leader_index in enumerate(leaders):
            last_index = leaders[i + 1] if i + 1 < len(leaders) else len(tacs)
            self.nodes[i] = BasicBlock(i, tacs[leader_index:last_index])


class ICFG:
    """Class represents InterProcedural Control Flow Graph
    credits: https://www.researchgate.net/publication/273445077_Designing_and_Implementing_Control_Flow_Graph_for_Magic_4th_Generation_Language"""
    cfgs: dict[str, CFG]  # key: procedure name
    procedural_edges: list[ProceduralEdge]

    def __init__(self, tacs: dict[str, list[Quadruple]], cfgs: Optional[dict[str, CFG]] = None):
        if cfgs is None:
            cfgs = {}
        self.cfgs = cfgs
        for proc_name, tac in tacs.items():
            self.cfgs[proc_name] = CFG(proc_name, tac)
        self.procedural_edges = self._make_procedural_edges()

    def _make_procedural_edges(self) -> list[ProceduralEdge]:
        proc_edges = []
        for proc_name, cfg in self.cfgs.items():
            for bb_index, other_proc_name in cfg.outer_procedural_edges.items():
                proc_edges.append(ProceduralEdge(proc_name, bb_index, other_proc_name))
        return proc_edges
