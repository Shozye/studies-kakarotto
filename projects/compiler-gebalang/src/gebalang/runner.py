from ..common.tac_models import Quadruple, TAC
from .gebalang_lexer import GebalangLexer
from .gebalang_parser import GebalangParser


def _clear_labels(tacs: dict[str, list[Quadruple]]) -> dict[str, list[Quadruple]]:
    labels: dict[str, str] = dict()
    label_groups: list[set] = []

    for proc, proc_tacs in tacs.items():
        for i, tac in enumerate(proc_tacs):
            if not tac.label:
                continue

            found_group = None
            for label_group in label_groups:
                if tac.label in label_group:
                    found_group = label_group

            if found_group is None:
                found_group = {tac.label}
                label_groups.append(found_group)

            if tac.type == TAC.LABEL:
                next_tac = proc_tacs[i + 1]
                if not next_tac.label:
                    next_tac.label = tac.label
                else:
                    found_group.add(next_tac.label)

    for i, label_group in enumerate(label_groups):
        for label in label_group:
            labels[label] = f"E_{i}"

    for proc, proc_tacs in tacs.items():
        for i, tac in enumerate(proc_tacs):
            if tac.label:
                tac.label = labels[tac.label]

            if tac.type in [TAC.CALL, TAC.SCALL]:
                tac.arg2[0] = labels[tac.arg2[0]]

            if tac.type in [TAC.GOTO, TAC.IFGOTO]:
                tac.res = labels[tac.res]

    new_tacs = dict()
    for proc, proc_tacs in tacs.items():
        new_tacs[proc] = []
        for tac in proc_tacs:
            if tac.type != TAC.LABEL:
                new_tacs[proc].append(tac)
    return new_tacs


def get_tac(text: str) -> dict[str, list[Quadruple]]:
    lexer = GebalangLexer()
    parser = GebalangParser()
    parser.parse(lexer.tokenize(text))
    tacs = _clear_labels(parser.tac)
    return tacs
