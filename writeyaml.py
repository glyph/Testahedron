from sys import stdout
from yaml import dump

dump(
    {
        "name": "CI",
        "on": {
            "push": {
                "branches": ["trunk", "release-*"],
                "tags": [
                    "twisted-*",
                ],
            },
            "pull_request": {"branches": ["trunk"]},
        },
        "permissions": "read",
        "concurrency": {
            "group": "${{ github.ref }}",
            "cancel-in-progress": "${{ github.ref != 'refs/heads/trunk' }}",
        },
        "jobs": {
            "testing": {
                "strategy": {
                    "matrix": {
                        # matrix-key: [matrix-value*s*]
                        # looks like maybe we cannot have empty arrays for
                        # matrix keys; Twisted's config is careful to suppply
                        # job-level defaults for everything
                        # SPECIAL KEYS! you can't have an 'include' value.
                        "include": [
                            {
                                # matrix-key: matrix:value
                            },
                        ],
                        "exclude": [
                            {
                                # probably don't need this one
                            },
                        ],
                    },
                },
            },
        },
    },
    stdout,
)
