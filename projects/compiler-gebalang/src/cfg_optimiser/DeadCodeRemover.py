from ..control_flow_graph.cfg import ICFG


class DeadCodeRemover:
    def __init__(self, icfg: ICFG):
        self.icfg = icfg

    def optimise(self):
        visited = set()

        queue = [("MAIN", 0)]
        while queue:
            elem = queue.pop()
            if elem in visited:
                continue
            visited.add(elem)
            prog_name, bb_index = elem
            if self.icfg.cfgs[prog_name].edges.get(bb_index) is not None:
                bb_outs = self.icfg.cfgs[prog_name].edges[bb_index].outs()
                for bb_end_index in bb_outs:
                    queue.append((prog_name, bb_end_index))

            if self.icfg.cfgs[prog_name].outer_procedural_edges.get(bb_index) is not None:
                goal_prog = self.icfg.cfgs[prog_name].outer_procedural_edges[bb_index]
                queue.append((goal_prog, 0))

        for proc_name, cfg in self.icfg.cfgs.items():
            nodes_to_remove = []
            for node in cfg.nodes:
                if (proc_name, node) not in visited:
                    nodes_to_remove.append(node)

            for node in nodes_to_remove:
                del cfg.nodes[node]

        cfgs_to_remove = set()
        for name, cfg in self.icfg.cfgs.items():
            if len(cfg.nodes) == 0:
                cfgs_to_remove.add(name)
        for cfg in cfgs_to_remove:
            del self.icfg.cfgs[cfg]



