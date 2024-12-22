import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

from ..common.cfg_models import BasicBlock
from .cfg import ICFG, CFG
from ..common.tac_models import get_tac_repr
import matplotlib.pyplot as plt


def write_icfg_to_file(
    icfg: ICFG,
    path: str,
    should_tacs: bool = True
):
    nodes = {key: icfg.cfgs[key].nodes.values() for key in icfg.cfgs}
    inner_edges = {key: icfg.cfgs[key].edges for key in icfg.cfgs}
    procedural_edges = {(pedge.proc1, pedge.node1): pedge for pedge in icfg.procedural_edges}

    if should_tacs:
        max_label = 0
        for proc in nodes:
            lbb = nodes[proc]
            for bb in lbb:
                for tac in bb.tacs:
                    max_label = max(max_label, len(tac.label))
    with open(path, 'w+') as file:
        for proc in nodes:
            lbb = nodes[proc]
            edges = inner_edges[proc]
            file.write(f"===== {proc} =====\n")
            for bb in lbb:
                bb: BasicBlock
                file.write(f"{bb}")
                file.write("" if edges.get(bb.index) is None else f" {edges[bb.index]}")
                file.write(f" {procedural_edges[(proc, bb.index)]}"
                           if procedural_edges.get((proc, bb.index)) is not None else "")
                file.write("\n")
                if should_tacs:
                    for tac in bb.tacs:
                        file.write(f"{get_tac_repr(tac, max_label)}\n")
                else:
                    for cmd in bb.commands:
                        file.write(f"{cmd.label} : {cmd}\n")


def fill_DiGraph_with_CFG(G: nx.DiGraph, proc: str, cfg: CFG):
    for bb in cfg.nodes.values():
        G.add_node((proc, bb.index))

    for index, out_edge in cfg.edges.items():
        G.add_edge((proc, index), (proc, out_edge.if_true))
        if out_edge.if_false != -1:
            G.add_edge((proc, index), (proc, out_edge.if_false))


def make_ICFG_DiGraph(icfg: ICFG) -> nx.DiGraph:
    G = nx.DiGraph()
    for proc, cfg in icfg.cfgs.items():
        fill_DiGraph_with_CFG(G, proc, cfg)
    # here will be also adding procedural edges
    return G


def plot_icfg(
    icfg: ICFG,
    path: str
):
    G = make_ICFG_DiGraph(icfg)
    pos = graphviz_layout(G, prog="dot")
    nx.draw_networkx(G, pos, node_size=500, arrows=True, node_shape='s', font_size=6)  # so^>v<dph8
    calledges = [((pedge.proc1, pedge.node1), (pedge.proc2, 0)) for pedge in icfg.procedural_edges]
    retedges = [((pedge.proc2, max(icfg.cfgs[pedge.proc2].nodes.keys())), (pedge.proc1, pedge.node1 + 1))
                for pedge in icfg.procedural_edges]
    nx.draw_networkx_edges(G, pos=pos, edgelist=calledges, node_shape='s', node_size=500, style="dashed", alpha=0.5,
                           edge_color="red")
    nx.draw_networkx_edges(G, pos=pos, edgelist=retedges, node_shape='s', node_size=500, style="dashed", alpha=0.5,
                           edge_color="green")
    plt.savefig(path)
