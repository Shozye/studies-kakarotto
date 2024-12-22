class TACException(Exception):
    pass


class VariableNotDeclaredException(TACException):
    """Thrown when variable in procedure was not previously declared in param or locals"""


class NotInitialisedException(TACException):
    """Done during procedure execution, write, """
    pass


class NotEnoughParamsException(TACException):
    """Done"""


class ProcedureNotDeclaredException(TACException):
    """Done"""


class RecursiveCallException(TACException):
    """Done"""


class VariableAlreadyDeclaredException(TACException):
    """Done"""


class ProcedureAlreadyDeclaredException(TACException):
    """Done"""
