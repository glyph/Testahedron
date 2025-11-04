"""
An axis of operating systems that your project might support.
"""

from enum import Enum, auto

from ..matrix import Axis


class SystemType(Enum):
    macOS = auto()
    windows = auto()
    linux = auto()
    freebsd = auto()

os = Axis(
    "Operating System",
    list(SystemType),
)
