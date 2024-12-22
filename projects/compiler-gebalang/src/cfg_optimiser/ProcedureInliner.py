from collections import defaultdict

from ..control_flow_graph.cfg import ICFG


class ProcedureInliner:
    def __init__(self, icfg: ICFG):
        self.icfg = icfg

    def inline(self):
        to_inline = self._get_procedures_to_inline()
        #print(to_inline)

    def _get_procedures_to_inline(self) -> list[str]:
        frequencies = defaultdict(int)
        for pedge in self.icfg.procedural_edges:
            frequencies[pedge.proc2] += 1
        return [proc for proc in frequencies if frequencies[proc] == 1]

