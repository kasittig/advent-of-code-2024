from unittest import TestCase

from solutions.day_10 import Day10Solution

example: list[str] = [
    "89010123",
    "78121874",
    "87430965",
    "96549874",
    "45678903",
    "32019012",
    "01329801",
    "10456732",
]


class Day10SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Day10Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(0, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(0, self.solution.solve_part_2(self.data))


class Day10HelpersTestCase(TestCase):
    def test_helper(self) -> None:
        pass
