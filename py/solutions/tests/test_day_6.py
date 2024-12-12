from unittest import TestCase

from solutions.day_6 import Day6Solution


example = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
]


class Day6SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Day6Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(41, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(6, self.solution.solve_part_2(self.data))


class Day6HelpersTestCase(TestCase):
    def test_helper(self) -> None:
        pass
