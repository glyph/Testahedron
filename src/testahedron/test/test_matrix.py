from itertools import product
from unittest import TestCase

from ..matrix import Axis, Coordinate, Matrix


class MatrixTests(TestCase):
    def test_coordinate(self) -> None:
        """
        Coordinates that are the same compare the same.
        """
        letters = Axis("letters", ["a", "b"])
        numbers = Axis("numbers", [1, 2])
        self.assertEqual(
            Coordinate([(letters, "a"), Coordinate([(numbers, 1)])]),
            Coordinate([(letters, "a"), Coordinate([(numbers, 1)])]),
        )

    def test_iterate(self) -> None:
        letters = Axis("letters", ["a", "b"])
        numbers = Axis("numbers", [1, 2])
        words = Axis("words", ["dog", "cat", "bird"])
        m = Matrix(
            [
                letters,
                numbers,
                words,
            ]
        )
        self.assertEqual(
            list(m),
            [
                Coordinate([(letters, "a"), (numbers, 1), (words, "dog")]),
                Coordinate([(letters, "b"), (numbers, 1), (words, "dog")]),
                Coordinate([(letters, "a"), (numbers, 2), (words, "dog")]),
                Coordinate([(letters, "b"), (numbers, 2), (words, "dog")]),
                Coordinate([(letters, "a"), (numbers, 1), (words, "cat")]),
                Coordinate([(letters, "b"), (numbers, 1), (words, "cat")]),
                Coordinate([(letters, "a"), (numbers, 2), (words, "cat")]),
                Coordinate([(letters, "b"), (numbers, 2), (words, "cat")]),
                Coordinate([(letters, "a"), (numbers, 1), (words, "bird")]),
                Coordinate([(letters, "b"), (numbers, 1), (words, "bird")]),
                Coordinate([(letters, "a"), (numbers, 2), (words, "bird")]),
                Coordinate([(letters, "b"), (numbers, 2), (words, "bird")]),
            ],
        )

        axisvalues = [
            [(axis, each) for each in axis.values]
            for axis in [letters, numbers, words][::-1]
        ]
        from pprint import pprint
        print("\n\n---axisvalues")
        pprint(axisvalues)
        print("\n\n---expanded")
        expanded = list(product(*axisvalues))
        coordinates = [Coordinate(list(each[::-1])) for each in expanded]
        mcoordinates = list(m)
        pprint(coordinates)
        pprint(mcoordinates)
        self.maxDiff = 9999
        # self.assertEqual(len(mcoordinates), len(coordinates))
        # self.assertEqual(mcoordinates[0].scalars, coordinates[0].scalars)
        self.assertEqual(mcoordinates, coordinates)
