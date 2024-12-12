from unittest import TestCase

from solutions.day_5 import Day5Solution


example = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
    "",
    "75, 47, 61, 53, 29",
    "97, 61, 53, 29, 13",
    "75, 29, 13",
    "75, 97, 47, 61, 53",
    "61, 13, 29",
    "97, 13, 75, 29, 47",
]


class Day5SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Day5Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(143, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(123, self.solution.solve_part_2(self.data))


class Day5HelpersTestCase(TestCase):
    def test_helper(self) -> None:
        pass
