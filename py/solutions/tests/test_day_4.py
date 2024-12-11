from unittest import TestCase

from solutions.day_4 import Day4Solution, WordSearchGrid


example = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]


class WordSearchGridTestCase(TestCase):
    def setUp(self) -> None:
        self.grid = WordSearchGrid(example)

    def test_get(self) -> None:
        data = "MMMSXXMASM"

        for i in range(len(data)):
            assert self.grid.get(0, i) == data[i]

    def test_check_xmas(self) -> None:
        assert self.grid.check_xmas(0, 5, (1, 0))
        assert self.grid.check_xmas(9, 9, (0, -1))
        assert self.grid.check_xmas(9, 1, (1, -1))
        assert not self.grid.check_xmas(0, 5, (0, 1))

    def test_check_x_mas(self) -> None:
        assert self.grid.check_x_mas(1, 2)


class Day4SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Day4Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(18, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(9, self.solution.solve_part_2(self.data))


class Day4HelpersTestCase(TestCase):
    def test_helper(self) -> None:
        pass
