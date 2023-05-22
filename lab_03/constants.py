from enum import StrEnum, auto


class TYPE(StrEnum):
    TUPLE = auto()
    SET = auto()
    FROZENSET = auto()
    FUNCTION = auto()
    CODE = auto()
    CELL = auto()
    MODULE = auto()
    BYTES = auto()


UNSERIALIZABLE_CODE_TYPES = (
    "co_positions",
    "co_lines",
    "co_exceptiontable",
    "co_lnotab",
)
