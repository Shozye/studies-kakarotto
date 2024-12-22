from ..common.commands import LOAD, LOADI, ADDI, ADD, gen_load, gen_add
from ..common.cfg_models import BasicBlock
from ..control_flow_graph.cfg import ICFG


class EquivalenceLoadAddSwapper:
    """Swapping """
    def __init__(self, icfg: ICFG):
        self.icfg = icfg

    def swap(self):
        for proc_name, cfg in self.icfg.cfgs.items():
            if proc_name.startswith("!"):
                continue
            for bb in cfg.nodes.values():
                self._swap_in_bb(bb)

    def _swap_in_bb(self, bb: BasicBlock):
        possible_load_swaps = set()
        prev_command = bb.commands[0]
        for i, command in enumerate(bb.commands[1:], start=1):
            if prev_command.is_load and command.is_add and command.arg != "*storage_0*":
                possible_load_swaps.add(i-1)
            prev_command = command
        if not possible_load_swaps:
            return

        new_commands = []
        i = 0
        while i < len(bb.commands):
            if i in possible_load_swaps:
                load_command = bb.commands[i]
                add_command = bb.commands[i+1]
                new_load_command = gen_load(add_command.is_i)(add_command.arg, load_command.label)
                new_add_command = gen_add(load_command.is_i)(load_command.arg, add_command.label)
                new_commands.extend([new_load_command, new_add_command])
                i += 2
            else:
                new_commands.append(bb.commands[i])
                i += 1
        bb.set_commands(new_commands)



