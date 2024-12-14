from unittest import TestCase

from solutions.day_9 import Day9Solution, compress_file, expand_file

example: list[str] = ["2333133121414131402"]


class Day9SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Day9Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(1928, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(0, self.solution.solve_part_2(self.data))


class Day9HelpersTestCase(TestCase):
    def test_expand_file(self) -> None:
        assert expand_file("12345") == [
            "0",
            ".",
            ".",
            "1",
            "1",
            "1",
            ".",
            ".",
            ".",
            ".",
            "2",
            "2",
            "2",
            "2",
            "2",
        ]
        assert expand_file(example[0]) == [
            "0",
            "0",
            ".",
            ".",
            ".",
            "1",
            "1",
            "1",
            ".",
            ".",
            ".",
            "2",
            ".",
            ".",
            ".",
            "3",
            "3",
            "3",
            ".",
            "4",
            "4",
            ".",
            "5",
            "5",
            "5",
            "5",
            ".",
            "6",
            "6",
            "6",
            "6",
            ".",
            "7",
            "7",
            "7",
            ".",
            "8",
            "8",
            "8",
            "8",
            "9",
            "9",
        ]

    def test_compress_file(self) -> None:
        assert (
            compress_file(
                [
                    "0",
                    ".",
                    ".",
                    "1",
                    "1",
                    "1",
                    ".",
                    ".",
                    ".",
                    ".",
                    "2",
                    "2",
                    "2",
                    "2",
                    "2",
                ]
            )
            == "022111222"
        )
        assert (
            compress_file(
                [
                    "0",
                    "0",
                    ".",
                    ".",
                    ".",
                    "1",
                    "1",
                    "1",
                    ".",
                    ".",
                    ".",
                    "2",
                    ".",
                    ".",
                    ".",
                    "3",
                    "3",
                    "3",
                    ".",
                    "4",
                    "4",
                    ".",
                    "5",
                    "5",
                    "5",
                    "5",
                    ".",
                    "6",
                    "6",
                    "6",
                    "6",
                    ".",
                    "7",
                    "7",
                    "7",
                    ".",
                    "8",
                    "8",
                    "8",
                    "8",
                    "9",
                    "9",
                ]
            )
            == "0099811188827773336446555566"
        )
