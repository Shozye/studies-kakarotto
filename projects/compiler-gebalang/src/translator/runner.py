from .procedure import ProcedureTranslator
from ..common.cfg_models import BasicBlock
from ..control_flow_graph.cfg import ICFG


def translate(icfg: ICFG):
    for proc_name, cfg in icfg.cfgs.items():
        if proc_name.startswith("!"):
            continue
        translator = ProcedureTranslator(proc_name, cfg)
        translator.run()

