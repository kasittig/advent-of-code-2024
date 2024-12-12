from unittest import TestCase

from solutions.day_7 import Day7Solution
from solutions.helpers.day_7 import get_possible_totals


example = [
    "190: 10 19",
    "3267: 81 40 27",
    "83: 17 5",
    "156: 15 6",
    "7290: 6 8 6 15",
    "161011: 16 10 13",
    "192: 17 8 14",
    "21037: 9 7 18 13",
    "292: 11 6 16 20",
]


class Day7SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Day7Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(3749, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(11387, self.solution.solve_part_2(self.data))


class Day7HelpersTestCase(TestCase):
    def test_get_possible_totals(self) -> None:
        assert 156 in get_possible_totals([15, 6], 156, concatenate=True)
        assert 7290 in get_possible_totals([6, 8, 6, 15], 7290, concatenate=True)
        assert 192 in get_possible_totals([17, 8, 14], 192, concatenate=True)
