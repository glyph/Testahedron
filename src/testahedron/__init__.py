from dataclasses import dataclass, field
from typing import Generic, Iterable, Iterator, TypeVar

T = TypeVar("T")

"""
Define your axes; an axis might be something like "platforms", each platform
could then be a Platform object with a name, or whatever other attributes are
interesting.

Each axis is mutually exclusive.

For Twisted, the axes might be:

    - dependency versions

        - mindeps: a constraint file having minimum dependency versions

        - maxdeps: a constraint file having current dependency versions

    - dependency availability

        - alldeps: install all extras

        - nodeps: install only twisted itself, no extras

    - operating system

        - macos

        - windows

        - linux

    - "has gtk"

        - gtk

        - no gtk

    - python version

        - 3.9

        - 3.10

        - 3.11

        - 3.12

        - 3.13

        - 3.14

there are then several different expansion strategies that might be invoked at
any given time

    - expand the matrix for the current platform, based on the availability of
      GTK+ libraries, for the most coverage you can get for local testing

    - expand the matrix as expansively as possible to reflect every possible
      environment into tox.ini, even if many of them are not runnable

    - expand the matrix for a supported subset of environments in github
      actions, making sure to cover at least part of every axis, explicitly
      making note of what is being excluded.
"""



@dataclass
class Axis(Generic[T]):
    name: str
    values: list[T] = field(compare=False)


@dataclass(repr=False)
class Coordinate:
    scalars: list[tuple[Axis[object], object]]

    def __repr__(self) -> str:
        return f'<{", ".join([f"{axis.name}={value}"for axis,value in self.scalars])}>'


@dataclass
class Cursor:
    axes: list[Axis[object]]
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


@dataclass
class Matrix:
    axes: list[Axis[object]]

    def __iter__(self) -> Iterator[Coordinate]:
        return iter(Cursor(self.axes))


if __name__ == "__main__":
    m = Matrix(
        [
            Axis("letters", ["a", "b", "c", "d"]),
            Axis("numbers", [1, 2, 3, 4]),
            Axis("words", ["dog", "cat", "bird", "fish", "circle", "square"]),
        ]
    )
    from pprint import pprint

    pprint(list(m))
