from unittest import TestCase

from solutions.day_2 import Day2Solution


example = ["7 6 4 2 1", "1 2 7 8 9", "9 7 6 2 1", "1 3 2 4 5", "8 6 4 4 1", "1 3 6 7 9"]


class Day2SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Day2Solution
        self.data = self.solution.format_data(example)

    def test_format_data(self) -> None:
        self.assertEqual(
            self.data,
            [
                [7, 6, 4, 2, 1],
                [1, 2, 7, 8, 9],
                [9, 7, 6, 2, 1],
                [1, 3, 2, 4, 5],
                [8, 6, 4, 4, 1],
                [1, 3, 6, 7, 9],
            ],
        )

    def test_solve_part_1(self) -> None:
        self.assertEqual(2, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(4, self.solution.solve_part_2(self.data))


class Day2HelpersTestCase(TestCase):
    def test_helper(self) -> None:
        pass
