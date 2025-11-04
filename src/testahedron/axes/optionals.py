"""
Compute an axis for an optional dependency group.

Thoughts:

    1. this should handle pinning of dependencies (and serialization of pins)
       as well as enumerating extras

    2. this is part of a lifecycle somewhere, where someone will run it to
       freeze things, producing both floor and ceiling pins for CI, which the
       user may or may not want to explicitly include in their matrix (most
       projects should just stick with a ceiling environment, assuming users
       will upgrade the whole venv at once, but some libraries may need to
       maintain a compatibility window that keeps and tests with both sets of
       pins, c.f. twisted's 'mindeps')

    3. obviously `uv`, `pip-tools`, `poetry`, etc, already all deal with this
       in their own ways, so integrating somehow would be nice (?) but might
       not be possible because most of them serialize a *single* set of pins in
       a lock file, rather than multiple sets for version spans (the
       aforementioned floor / ceiling)
"""

from dataclasses import dataclass

from build.util import project_wheel_metadata

from ..matrix import Axis


@dataclass
class OptionalDependencyGroup:
    name: str
    deps: list[str]


def getExtras() -> Axis[OptionalDependencyGroup]:
    """
    get the extras from the current directory to represent as an axis
    """
    metadata = project_wheel_metadata(".")
    groups = []
    for name, value in metadata.items():
        if name == "Provides-Extra":
            groups.append(OptionalDependencyGroup(value, []))
        elif name == "Requires-Dist":
            if groups:
                groups[-1].deps.append(value)
    return Axis("Optional Dependencies", groups)

if __name__ == "__main__":
    extrasAxis = getExtras()
    print([each.name for each in extrasAxis.values])
