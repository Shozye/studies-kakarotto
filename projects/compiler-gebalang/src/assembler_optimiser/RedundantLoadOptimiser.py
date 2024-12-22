from ..common.cfg_models import BasicBlock
from ..control_flow_graph.cfg import ICFG, CFG


class RedundantLoadOptimiser:
    def __init__(self, icfg: ICFG):
        self.icfg = icfg

    def optimise(self):
        for procname, cfg in self.icfg.cfgs.items():
            if procname.startswith("!"):
                continue
            self._optimise_cfg(cfg)

    def _optimise_cfg(self, cfg: CFG):
        for proc_name, bb in cfg.nodes.items():
            if bb.commands[0].is_load and bb.index != 0:
                self._optimise_interblock_load(cfg, bb)
            self._optimise_block(bb)

    def _optimise_interblock_load(self, cfg: CFG, bb: BasicBlock):
        """ Optimisation is removed, because it doesn't seem to bring any profit
        load_argument = bb.commands[0].arg
        can_remove = True
        prev_nodes = [x for x in cfg.backtrack_edges[bb.index]]
        visited = set()
        while prev_nodes:
            node = prev_nodes.pop()
            for command in cfg.nodes[node].commands[::-1]:
                if command.is_jump and not command.arg.startswith("#"):
                    continue
                if command.is_store and command.arg == load_argument:
                    break
                can_remove = False
                break
            else:
                visited.add(node)
                prev_nodes.extend([x for x in cfg.backtrack_edges[node] if x not in visited])

        print(cfg.name, bb.index,can_remove)
        """

    def _optimise_block(self, bb: BasicBlock):

        prev_command = bb.commands[0]
        to_remove = set()
        for i, command in enumerate(bb.commands):
            if command.is_load:
                if prev_command.arg == command.arg:
                    if prev_command.is_store:
                        to_remove.add(i)
                    pass
            prev_command = command
        if not to_remove:
            return
        new_commands = [bb.commands[i] for i in range(len(bb.commands)) if i not in to_remove]
        bb.set_commands(new_commands)
