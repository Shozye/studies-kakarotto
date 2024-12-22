from ..common.cfg_models import BasicBlock
from ..common.commands import *
from ..control_flow_graph.cfg import ICFG
from ..translator.Flags import Flag


class Merger:
    merged_commands: list[Command]
    procedure_starts: dict[str, int]

    def __init__(self, icfg: ICFG):
        self.icfg = icfg
        self.merged_commands = []
        self.procedure_starts = {}

    def _get_all_flags(self) -> set[Flag]:
        flags = set()
        for cfg in self.icfg.cfgs.values():
            flags.update(cfg.flags)
        return flags

    def handle_flags(self):
        flags = self._get_all_flags()
        if Flag.one in flags:
            self.merged_commands.extend([
                SET("1"),
                STORE("5")
            ])

    def fill_commands(self, bb: BasicBlock):
        self.merged_commands.extend(bb.commands)

    def _translate_labels(self):
        labels = dict()
        for i, cmd in enumerate(self.merged_commands):
            if cmd.label != "":
                labels[cmd.label] = str(i)

        for cmd in self.merged_commands:
            if cmd.arg.startswith("E_"):
                cmd.arg = str(labels[cmd.arg])

    def merge(self):
        self.handle_flags()
        for bb in self.icfg.cfgs["MAIN"].nodes.values():
            self.fill_commands(bb)
        for proc_name, cfg in self.icfg.cfgs.items():
            if proc_name == "MAIN":
                continue
            self.procedure_starts[f"#{proc_name}#"] = len(self.merged_commands)
            for bb in cfg.nodes.values():
                self.fill_commands(bb)

        for command in self.merged_commands:
            if command.arg.startswith("#"):
                command.arg = str(self.procedure_starts[command.arg])

        self._translate_labels()



