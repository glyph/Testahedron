
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




__version__ = '0.0.1'
