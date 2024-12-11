from unittest import TestCase

from solutions.day_3 import Day3Solution


example = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]


class Day3SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Day3Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(161, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(48, self.solution.solve_part_2(self.data))


class Day3HelpersTestCase(TestCase):
    def test_helper(self) -> None:
        pass
