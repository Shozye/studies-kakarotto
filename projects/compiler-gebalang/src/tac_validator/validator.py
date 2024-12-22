from dataclasses import dataclass, field
from typing import Callable

from .exceptions import *
from ..common.tac_models import TAC, Quadruple


@dataclass
class ParamInformation:
    need: bool = False


@dataclass
class ProcedureInformation:
    param: list[str] = field(default_factory=list)
    local: list[str] = field(default_factory=list)
    initialised: list[str] = field(default_factory=list)
    param_initialised: dict[str, ParamInformation] = field(default_factory=dict)


class Validator:
    """Simple validator checking for few things
    In case it finds any of the following things, it throws exception
    1. Call for not existing procedure
    2. Recursion call in procedure
    3. Not enough parameters to call procedure
    4. Existence of two variables with the same name in one procedure or program.
    5. Existence of two procedures with same identifier
    6. Usage of undeclared variables
    7. Usage of uninitialized variables, but this is up to some point:
    -   Analysis do not perform any Control Graph analysis so if there is any code
        Previously that may have initialized variables then it is initialized
        Even though it may not be in the same control branch.
    -   It is assumed that leaving from the procedure initializes variables
    @todo Full check for uninitialized variables
    """
    symbols: dict[str, ProcedureInformation]

    def __init__(self):
        self.symbols = {}
        self.curr_proc = None

    def curr(self):
        return self.symbols[self.curr_proc]

    def run(self, tacs: dict[str, list[Quadruple]]):
        func_mapping: dict[TAC, Callable] = {
            TAC.READ: self.read, TAC.WRITE: self.write,
            TAC.PARAM: self.param, TAC.LOCAL: self.local,
            TAC.SCALL: self.scall, TAC.CALL: self.call,
            TAC.RETURN: self.return_,
            TAC.IFGOTO: self.ifgoto, TAC.GOTO: self.goto,
            TAC.ASSIGN: self.assign
        }
        for proc in tacs:
            if proc in self.symbols:
                raise ProcedureAlreadyDeclaredException(proc)
            self.curr_proc = proc
            self.symbols[proc] = ProcedureInformation()
            for tac in tacs[proc]:
                func_mapping[tac.type](tac)

    def param(self, tac: Quadruple):
        if tac.arg1.startswith("$"):  # we do not want to take return values as params yet
            return
        if not self.is_not_declared(tac.arg1):
            raise VariableAlreadyDeclaredException(f"{self.curr_proc}:{tac.arg1}")
        self.curr().param.append(tac.arg1)
        self.curr().param_initialised[tac.arg1] = ParamInformation()

    def local(self, tac: Quadruple):
        if not self.is_not_declared(tac.arg1):
            raise VariableAlreadyDeclaredException(f"{self.curr_proc}:{tac.arg1}")
        self.curr().local.append(tac.arg1)

    def read(self, tac: Quadruple):
        self.raise_if_not_declared(tac.arg1)
        self.curr().initialised.append(tac.arg1)

    def write(self, tac: Quadruple):
        if not tac.arg1.isdecimal():
            self.raise_if_not_declared(tac.arg1)
            self.expect_initialised(tac.arg1)

    def call(self, tac: Quadruple):
        if tac.arg1 == self.curr_proc:
            raise RecursiveCallException(tac.arg1)

        if tac.arg1 not in self.symbols:
            raise ProcedureNotDeclaredException(tac.arg1)
        if len(tac.arg2) - 1 != len(self.symbols[tac.arg1].param):
            raise NotEnoughParamsException(f"{tac.arg1}. {len(tac.arg2) - 1} != {len(self.symbols[tac.arg1].param)}")

        for arg in tac.arg2:
            if not arg.startswith("E_") and not arg.isdecimal():  # Nothing to analyse in pushing return values
                self.raise_if_not_declared(arg)
        for var in tac.arg2:
            if var in self.curr().param and self.curr().param_initialised[var].need:
                self.expect_initialised(var, f"{self.curr_proc}: Procedure {tac.arg1} expects {var} initialised")
        for arg in tac.arg2:
            if not arg.startswith("E_"):
                self.curr().initialised.append(arg)  # we are assuming procedures initialise variables

    def scall(self, tac: Quadruple):
        _, a, b, p = tac.arg2
        self.raise_if_not_declared(p)
        for var in [a, b]:
            var: str
            if var.isdecimal():
                continue
            self.raise_if_not_declared(var)
            self.expect_initialised(var, f"{self.curr_proc}: Procedure {tac.arg1} expects {var} initialised")
        self.curr().initialised.append(p)


    def assign(self, tac: Quadruple):
        self.raise_if_not_declared(tac.res)
        self.curr().initialised.append(tac.res)

        for var in [tac.arg1, tac.arg2]:
            if var.isdecimal() or var == "":
                continue  # there is nothing wrong if it is decimal
            self.raise_if_not_declared(var)
            self.expect_initialised(var)

    def ifgoto(self, tac: Quadruple):
        for var in [tac.arg1, tac.arg2]:
            if var.isdecimal():
                continue  # there is nothing wrong if it is decimal
            self.raise_if_not_declared(var)
            self.expect_initialised(var)

    def goto(self, tac: Quadruple):
        """Literally nothing to do. Etiquette checking is done for free during creation"""

    def return_(self, tac: Quadruple):
        """Literally nothing to do lol. It may halt the program or sth"""

    def raise_if_not_declared(self, identifier: str):
        if self.is_not_declared(identifier):
            raise VariableNotDeclaredException(f"{self.curr_proc}:{identifier}")

    def is_not_declared(self, identifier):
        return identifier not in self.curr().local and identifier not in self.curr().param

    def expect_initialised(self, identifier: str, msg: str = ""):
        if msg == "":
            msg = f"{self.curr_proc}: Not initialised variable {identifier}"
        if identifier in self.curr().initialised:
            return
        if identifier in self.curr().local:
            raise NotInitialisedException(msg)
        self.curr().param_initialised[identifier].need = True
