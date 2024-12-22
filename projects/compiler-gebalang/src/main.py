import os

from .cfg_optimiser.runner import optimise_icfg
from .assembler_optimiser.runner import optimise_assembler
from .merger.runner import merge
from .common.commands import write_commands_to_file
from .control_flow_graph.runner import get_icfg
from .translator.runner import translate
from .common.tac_models import write_tac_to_file
from .control_flow_graph.utils import write_icfg_to_file, plot_icfg
from .gebalang.runner import get_tac
from .tac_validator.runner import validate


def compile_gebalang(text: str, filename: str, output_path: str, output_dir: str, verbose: bool):
    " --- THREE ADDRESS CODE PART --- "
    tac = get_tac(text)
    if verbose:
        write_tac_to_file(tac, os.path.join(output_dir, f"{filename}.tac"))
    validate(tac)
    " --- CONTROL Flow GRAPH PART --- "
    icfg = get_icfg(tac)
    " --- ICFG OPTIMISATION PART "
    optimise_icfg(icfg)

    if verbose:
        write_icfg_to_file(icfg, f"{output_dir}/{filename}.bb.tac")
        plot_icfg(icfg, f"{output_dir}/{filename}_cfg.png")

    " --- TRANSLATION PART "

    translate(icfg)
    if verbose:
        write_icfg_to_file(icfg, f"{output_dir}/{filename}-no-optimisation.bb.asm", False)
    " --- ASSEMBLER OPTIMISATION PART --- "
    optimise_assembler(icfg)
    if verbose:
        write_icfg_to_file(icfg, f"{output_dir}/{filename}.bb.asm", False)

    # " --- END PART "
    commands = merge(icfg)
    write_commands_to_file(os.path.join(output_dir, output_path), commands)

