from ..common.commands import gen_load, gen_add, SET
from ..common.cfg_models import BasicBlock
from ..control_flow_graph.cfg import ICFG


class RedundantSetAddOptimiser:
    def __init__(self, icfg: ICFG):
        self.icfg = icfg

    def optimise(self):
        for proc_name, cfg in self.icfg.cfgs.items():
            if proc_name.startswith("!"):
                continue
            for bb in cfg.nodes.values():
                self._swap_in_bb(bb)

    def _swap_in_bb(self, bb: BasicBlock):
        new_commands = []
        i = 1
        while i < len(bb.commands):
            prev_command = bb.commands[i - 1]
            command = bb.commands[i]
            if prev_command.directive == "SET" and prev_command.arg == "0" and command.is_add:
                new_commands.append(gen_load(command.is_i)(command.arg, prev_command.label))
                i += 2
            elif prev_command.directive == "SET" and prev_command.arg.isdecimal() and command.is_add and command.arg.startswith(
                "*const_"):
                const_num = int(command.arg.split("const_")[1][:-1])
                new_commands.append(SET(str(int(prev_command.arg) + const_num), prev_command.label))
                i += 2
            else:
                new_commands.append(prev_command)
                i += 1
        if i == len(bb.commands):
            new_commands.append(bb.commands[-1])
        bb.set_commands(new_commands)
