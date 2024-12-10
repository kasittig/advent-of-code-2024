from unittest import TestCase

from solutions.day_1 import Day1Solution


example = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]


class Day1SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Day1Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(11, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(31, self.solution.solve_part_2(self.data))


class Day1HelpersTestCase(TestCase):
    def test_helper(self) -> None:
        pass
