from ..common.tac_models import Quadruple


class C:
    lexed = str
    value = str
    expression = tuple[str]
    condition = tuple[list[Quadruple], list[Quadruple], str, str]
    declarations = list[str]
    local_variables = list[str]
    proc_head = tuple[str, list[str]]
    command = list[Quadruple]
    commands = list[Quadruple]
    procedure = dict[str, list[Quadruple]]
    procedures = dict[str, list[Quadruple]]
    main = dict[str, list[Quadruple]]


class P:
    NUM: C.lexed
    ID: C.lexed
    ARIT_OP: C.lexed
    COND_OP: C.lexed
    COMMA: C.lexed

    value: C.value
    value0: C.value
    value1: C.value

    expression: C.expression
    condition: C.condition
    declarations: C.declarations
    local_variables: C.local_variables
    proc_head: C.proc_head
    command: C.command
    commands: C.commands
    commands0: C.commands
    commands1: C.commands
    procedure: C.procedure
    procedures: C.procedures
    main: C.main
