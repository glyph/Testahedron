# -*- test-case-name: testahedron.test.test_matrix -*-
"""
Fully abstract matrix representation.
"""

from dataclasses import dataclass, field
from typing import Any, Generic, Iterator, Sequence, TypeVar, TypeVarTuple

T = TypeVar("T")

@dataclass(frozen=True)
class Axis(Generic[T]):
    """
    An axis is a collection of values for one dimension of a matrix.
    """
    name: str
    values: list[T] = field(compare=False)


@dataclass(repr=False, frozen=True)
class Coordinate:
    """
    A coordinate is a specific location within the matrix, with one value for each aaxis.
    """
    scalars: list[tuple[Axis[object], object]]

    def __repr__(self) -> str:
        return f'<{", ".join([f"{axis.name}={value}"for axis,value in self.scalars])}>'


@dataclass
class Cursor:
    """
    A L{Cursor} is an iterable that can produce a set of L{Coordinate}s for a
    particular matrix in order.
    """
    axes: Sequence[Axis[Any]]
    indexes: list[int] = field(init=False)

    def __post_init__(self) -> None:
        self.indexes = [0] * len(self.axes)

    def __iter__(self) -> Iterator[Coordinate]:
        while True:
            yield Coordinate(
                [
                    (self.axes[m], self.axes[m].values[index])
                    for m, index in enumerate(self.indexes)
                ]
            )
            for n, i in enumerate(self.indexes):
                if i < (len(self.axes[n].values) - 1):
                    self.indexes[n] = i + 1
                    self.indexes[:n] = [0] * n
                    break
            else:
                return

Axes = TypeVarTuple("Axes")
@dataclass
class Matrix(Generic[*Axes]):
    """
    A L{Matrix} is an iterable which uses a collection of L{axes <Axis>} to
    produce a L{Cursor} to iterate its full cartesian product of L{Coordinate}s
    """
    axes: tuple[*Axes]

    def __iter__(self) -> Iterator[Coordinate]:
        return iter(Cursor(self.axes))

