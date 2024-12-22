from dataclasses import dataclass

@dataclass
class Statistics:
    """Class for keeping track of time and lines used by compiler"""
    mem  : int = 0
    io   : int = 0
    jump : int = 0
    ari  : int = 0
    line : int = 0
