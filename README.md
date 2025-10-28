# Testahedron

## What are you testing and how are you testing it?

Many python projects support multiple target environments: multiple python
versions, multiple operating systems, multiple dependency library versions,
multiple operating system dependencies.  These axes of the support matrix are
represented in various ad-hoc ways:

- trove classifiers, such as `Programming Language :: Python :: 3.8`, `Programming Language :: Python :: 3.9`, `Programming Language :: Python :: 3.10`, `Environment :: GPU :: NVIDIA CUDA :: 13`
- a `requires-python=">=3.8"` declaration in `pyproject.toml`
- factors in `tox.ini` (but [not `tox.toml`](https://tox.wiki/en/4.32.0/config.html#:~:text=unless%20you%20need%20some%20of%20the%20more%20advanced%20features%20that%20TOML%20does%20not%20support)), including the implicit `pyXY` factors (`py311`, `py313`, etc) and explicit factors that you define
- matrix entries in github actions YAML, particularly a matrix axis defined on the `runs-on` key

## Not testing too much

However, these representations are almost always incomplete in strategic ways as well.  If we support all current Python versions (usually around 5) and two current versions of PyPy, as well as all three major OSes (linux, windows, macOS), 4 different kinds of GPU (Intel, AMD, NVidia, Apple) and 2 CPU architectures (x86_64, aarch64) then our fully expanded matrix is hypothetically 168 full runs of the tests.

This matrix is, however, only hypothetical.  Even before we get to cost concerns, parts of it are nonsensical. You can't have a */macOS/NVidia/aarch64 builder; that hardware doesn't exist.  These need to be excluded.

But other parts of the matrix also produce *theoretically* necessary test environments, but are in practice so duplicative that you don't need to run them all.  For example, if you have no python-version specific code, do you really need to run python3.11/macOS/Apple/aarch64 / python3.11/linux/Apple/aarch64 / python3.11/windows/Apple/aarch64 (presumably in a VM?) just to make sure python 3.11 works?  For most projects, a single 3.11 builder is fine, because you're *almost* never going to see a real-life test failure that only occurs in one specific environment.  (Of course, there are projects that do need to fully explode the whole matrix, but even then, they can usually afford to run the full integration suite once or twice a day rather than on every single commit.)

These exclusions, however, are often defined implicitly, by inclusion, in an ad-hoc way in a variety of not-necessarily-mutually-intelligible configuration files for different tools (tox, nox, github actions, circleCI, gitlab CI, etc).

Testagon provides a way to declare the matrix abstractly, enumerate all possible coordinates within that fully expanded matrix, then illustrate which parts are excluded and why.

The project's goal is to eventually be able to *create* config files for a variety of different tools which need to be derived from this information.
