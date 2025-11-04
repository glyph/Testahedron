from dataclasses import dataclass
from typing import Iterable

from ..matrix import Axis

@dataclass
class PythonVersion:
    # per verbiage on https://www.python.org/downloads/ , "python version"
    # refers to a minor version release series, "release version" refers to the
    # specific micro-version.
    major: int
    minor: int


def pythonVersions(
    *,
    majors: Iterable[int] = range(3, 4),
    minors: Iterable[int] = range(10, 15),
) -> Axis[PythonVersion]:
    """
    Compute a Python versions axis, defaulting to currently (as of this
    writing) supported versions, i.e. Python 3.10 to 3.14.
    """
    return Axis(
        "Python Version",
        [PythonVersion(major, minor) for major in majors for minor in minors],
    )
