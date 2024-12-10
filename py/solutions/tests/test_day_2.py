from unittest import TestCase

from solutions.day_2 import Day2Solution


example = []


class Day2SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Day2Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(None, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(None, self.solution.solve_part_2(self.data))


class Day2HelpersTestCase(TestCase):
    def test_helper(self) -> None:
        pass
