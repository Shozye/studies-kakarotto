def get_function_name(operator: str):
    names = {
        "*": "!mul",
        "/": "!div",
        "%": "!mod"
    }
    return names[operator]


def _get_reversable() -> dict[str, str]:
    d = {}
    for a, b in [(">", "<="), ("<", ">="), ("=", "!="), ("+", "+"), ("*", "*")]:
        d[a] = b
        d[b] = a
    return d


class BinOp:
    reversable: dict[str, str]
    val0: str
    val1: str
    op: str

    def __init__(self, val0: str, op: str, val1: str):
        self.val0 = val0
        self.op = op
        self.val1 = val1
        self.reversable = _get_reversable()
        self.optimise()

    def optimise(self):
        if self._is_numeric():
            self._optimise_numeric_case()
        elif self._is_mixed():
            self._optimise_mixed_case()
        else:
            self._optimise_variable_case()

    def _is_numeric(self) -> bool:
        return self.val0.isdecimal() and self.val1.isdecimal()

    def _is_mixed(self) -> bool:
        return self.val0.isdecimal() or self.val1.isdecimal()

    def is_operator_reversible(self) -> bool:
        return self.op in ["+", "*", "=", "!=", "<", ">", "<=", ">="]

    def is_operator_commutative(self) -> bool:
        return self.op in ["+", "*", "="]

    def swap_sides(self):
        self.op = self.reversable[self.op]
        self.val1, self.val0 = self.val0, self.val1

    def eval(self):
        if self.op == "=":
            self.op = "=="
        return eval(f"{self.val0} {self.op} {self.val1}")

    def set_solo_val0(self, val0: str):
        self.val0 = val0
        self.op = ""
        self.val1 = ""

    def get_tuple(self) -> tuple[str, str, str]:
        return self.val0, self.op, self.val1

    def _optimise_numeric_case(self):
        pass

    def _optimise_mixed_case(self):
        pass

    def _optimise_variable_case(self):
        pass


class BinaryArithmeticOperation(BinOp):
    def __init__(self, val0: str, op: str, val1: str):
        super().__init__(val0, op, val1)

    def _optimise_numeric_case(self):
        self._optimise_zeroing_cases()
        if self.op == "/":
            self.op = "//"
        if self.op == "*":
            value = self.eval()
            if value > 2**63 - 1:
                return
        self.set_solo_val0(str(max(0, self.eval())))

    def _optimise_mixed_case(self):
        if self.is_operator_reversible() and self.val0.isdecimal():
            self.swap_sides()
        self._optimise_neutral_case()
        self._optimise_zeroing_cases()

    def _optimise_neutral_case(self):
        if any([self.op in ["+", "-"] and "0" in self.val1,
                self.op in ["*", "/"] and "1" in self.val1]):
            self.set_solo_val0(self.val0)

    def _optimise_zeroing_cases(self):
        if any([self.op in ("/", "%", "*") and "0" in (self.val0, self.val1),
                self.op == "-" and "0" in self.val0]):
            self.set_solo_val0("0")


class BinaryLogicOperation(BinOp):
    def __init__(self, val0: str, op: str, val1: str):
        super().__init__(val0, op, val1)

    def _optimise_numeric_case(self):
        self.set_solo_val0(str(int(self.eval())))

    def _optimise_mixed_case(self):
        if self.val0.isdecimal():
            self.swap_sides()
        self._optimise_tautology()
        self._optimise_contradiction()
        self._optimise_equivalences()

    def _optimise_variable_case(self):
        self._optimise_tautology()
        self._optimise_contradiction()

    def negate(self):
        if self.op == "":
            self.set_solo_val0(str((int(self.val0) + 1) % 2))
        else:
            self.op = self.reversable[self.op]

    def _optimise_tautology(self):
        if any([self.op == ">=" and "0" in self.val1,
                self.op in ["=", ">=", "<="] and self.val0 == self.val1]):
            self.set_solo_val0("1")

    def _optimise_contradiction(self):
        if any([self.op == "<" and "0" in self.val1,
                self.op in ["<", ">", "!="] and self.val0 == self.val1]):
            self.set_solo_val0("0")

    def _optimise_equivalences(self):
        if self.op == "<" and self.val1 == "1":
            self.op, self.val1 = "=", "0"
        if self.op == ">=" and self.val1 == "1":
            self.op, self.val1 = ">", "0"
        if self.op == "<=" and self.val1 == "0":
            self.op = "="
