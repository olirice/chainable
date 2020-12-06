"""
Experimental module re-implementing builtins for compilation with mypc
"""
from typing import Any, Generator, Iterable, Optional, Tuple, TypeVar

from typing_extensions import Protocol

T = TypeVar("T")


class SupportsLessThan(Protocol):
    def __lt__(self, __other: Any) -> bool:
        ...


SupportsLessThanT = TypeVar("SupportsLessThanT", bound="SupportsLessThan")


def range(x: int) -> Generator[int, None, None]:
    if x <= 0:
        raise ValueError("x must be > 0")

    i = 0

    while i < x:
        yield i
        i += 1


def enumerate(iterable: Iterable[T], start: int = 0) -> Generator[Tuple[int, T], None, None]:
    i = start
    for entry in iterable:
        yield (i, entry)
        i += 1


def max(
    iterable: Iterable[SupportsLessThanT],
    default_obj: Optional[SupportsLessThanT] = None,
) -> SupportsLessThanT:

    best = default_obj

    for entry in iterable:
        if best is None or entry > best:
            best = entry

    if best is None:
        raise ValueError("bad!")

    return best
