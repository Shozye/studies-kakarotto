def gen_load(with_i: bool):
    return LOADI if with_i else LOAD

def gen_add(with_i: bool):
    return ADDI if with_i else ADD


class Command:
    directive: str
    arg: str
    label: str
    is_load: bool
    is_store: bool
    is_jump: bool
    is_add: bool
    is_i: bool

    def __init__(self, label: str, directive: str, arg: str = ""):
        self.directive = directive
        self.arg = arg
        self.label = label
        self.is_add = directive.startswith("ADD")
        self.is_load = directive.startswith("LOAD")
        self.is_store = directive.startswith("STORE")
        self.is_jump = False
        self.is_i = directive.endswith("I")

    def __repr__(self):
        return f"{self.directive} {self.arg}" if self.arg else f"{self.directive}"


def write_commands_to_file(path: str, commands: list[Command]):
    text = ""
    for command in commands:
        text += f"{command}\n"
    with open(path, 'w+', encoding='utf-8') as file:
        file.write(text)


""" ======== INPUT / OUTPUT ======== """


class GET(Command):
    def __init__(self, i: str, label: str = ""):
        super().__init__(label, "GET", i)


class PUT(Command):
    def __init__(self, i: str, label: str = ""):
        super().__init__(label, "PUT", i)


""" ======== MEMORY ======== """


class LOAD(Command):
    def __init__(self, i: str, label: str = ""):
        super().__init__(label, "LOAD", i)


class STORE(Command):
    def __init__(self, i: str, label: str = ""):
        super().__init__(label, "STORE", i)


class LOADI(Command):
    def __init__(self, i: str, label: str = ""):
        super().__init__(label, "LOADI", i)


class STOREI(Command):
    def __init__(self, i: str, label: str = ""):
        super().__init__(label, "STOREI", i)


""" ======== ARITHMETIC ======== """


class ADD(Command):
    def __init__(self, i: str, label: str = ""):
        super().__init__(label, "ADD", i)


class SUB(Command):
    def __init__(self, i: str, label: str = ""):
        super().__init__(label, "SUB", i)


class ADDI(Command):
    def __init__(self, i: str, label: str = ""):
        super().__init__(label, "ADDI", i)


class SUBI(Command):
    def __init__(self, i: str, label: str = ""):
        super().__init__(label, "SUBI", i)


class SET(Command):
    def __init__(self, x: str, label: str = ""):
        super().__init__(label, "SET", x)


class HALF(Command):
    def __init__(self, label: str = ""):
        super().__init__(label, "HALF")


""" ======== CONDITIONAL ======== """


class JUMP(Command):
    def __init__(self, i: str, label: str = ""):
        super().__init__(label, "JUMP", i)
        self.is_jump = True


class JPOS(Command):
    def __init__(self, i: str, label: str = ""):
        super().__init__(label, "JPOS", i)
        self.is_jump = True


class JZERO(Command):
    def __init__(self, i: str, label: str = ""):
        super().__init__(label, "JZERO", i)
        self.is_jump = True


class JUMPI(Command):
    def __init__(self, i: str, label: str = ""):
        super().__init__(label, "JUMPI", i)
        self.is_jump = True


""" ======== OUTPUT ======== """


class HALT(Command):
    def __init__(self, label: str = ""):
        super().__init__(label, "HALT")
