from ..common.cfg_models import VariableInfo
from ..control_flow_graph.cfg import ICFG


class SymbolFiller:
    global_symbols: dict[str, VariableInfo]

    def __init__(self, icfg: ICFG):
        self.icfg = icfg
        self.free_memory_index = 20
        self.global_symbols = {
            "*storage_0*": VariableInfo(False, 0),
            "*storage_1*": VariableInfo(False, 1),
            "*const_1*": VariableInfo(False, 5)
        }

    def get_free_memory(self) -> int:
        self.free_memory_index += 1
        return self.free_memory_index - 1

    def allocate_symbols(self):
        for cfg in self.icfg.cfgs.values():
            for symbol_name, info in cfg.symbols.items():
                if info.id != 0:
                    continue
                info.id = self.get_free_memory()

    def fill_symbols(self):
        for cfg in self.icfg.cfgs.values():
            for node in cfg.nodes.values():
                for command in node.commands:
                    if any([
                        (command.arg.startswith("#") and command.directive == "JUMP"),
                        command.arg == "",
                        command.arg.isdecimal(),
                        command.arg.startswith("E_")
                    ]):
                        continue
                    if command.arg.startswith("*"):
                        command.arg = str(self.global_symbols[command.arg].id)
                    elif command.arg.startswith("#"):
                        _, proc_name, index, _ = command.arg.split("#")
                        index = int(index)
                        memory_indexes = []
                        for var_info in list(self.icfg.cfgs[proc_name].symbols.values()):
                            memory_indexes.append(var_info.id)
                        min_memory = min(memory_indexes)
                        command.arg = str(min_memory + index)
                    else:
                        command.arg = str(cfg.symbols[command.arg].id)

