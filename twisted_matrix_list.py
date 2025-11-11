from __future__ import annotations
from dataclasses import dataclass

from testahedron.axes import platforms, pythons
from testahedron.matrix import Matrix

@dataclass
class Task:
    """
    A thing to do; the implicit axis of:

    - tests
    - api docs
    - narrative docs
    - release: build, publish
    """
    shellCommands: list[str]           # probably too simple (???)
    needs: list[Task]         # the tasks which much complete before this one


@dataclass
class DependencyConstraints:
    """
    List of dependency constraints, drawn from a lockfile of some kind,
    intended to provide a range of options for suppoprting older versions of
    other dependencies.  i.e. (no word for it yet)/mindeps axis
    """
    versions: list[str]

@dataclass
class DepGroups:
    """
    A set of dependency groups to install, i.e. alldeps/nodeps axis.
    """
    groups: list[str]


@dataclass
class HasCoverage:
    """
    Does this job have coverage?  Not just a bool because we're going to need
    methods on here to compute some extra shell commands at the beginning / end
    of the job.
    """
    hasCoverage: bool


@dataclass
class HasIPv6:
    """
    Does the job run in an environment that has IPv6 connectivity?  Needed to
    contribute some sysctl commands to the setup process.
    """
    hasIPv6: bool


@dataclass
class Job:
    system: platforms.SystemType
    python: pythons.PythonVersion
    task: Task
    dependencyConstraints: DependencyConstraints
    optionalDependencyGroupSets: DepGroups
    coverage: HasCoverage       # include coverage? withcov/nocov axis


matrix = Matrix([
    platforms.os
])
