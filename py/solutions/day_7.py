from typing import Any

from .base import BaseDailySolution
from .helpers.day_7 import get_possible_totals


class Day7Solution(BaseDailySolution):
    DAY = 7

    @classmethod
    def format_data(cls, input_data: list[str]) -> list[tuple[int, list[int]]]:
        """
        Example line: 190: 10 19

        :param input_data:
        :return:
        """
        values: list[tuple[int, list[int]]] = []

        for entry in input_data:
            entry = entry.strip()
            test_value, rest = entry.split(":")
            numbers: list[str] = rest.strip().split()

            values.append((int(test_value), [int(n) for n in numbers]))
        return values

    @classmethod
    def solve_part_1(cls, input_data: list[tuple[int, list[int]]]) -> int:
        """
        Insert * or + to make expressions correct

        Sum up total value of all correctable expressions

        :param input_data:
        :return:
        """
        result = 0

        for limit, entries in input_data:
            totals = get_possible_totals(entries, limit)
            if limit in totals:
                result += limit
        return result

    @classmethod
    def solve_part_2(cls, input_data: Any) -> int:
        """

        :param input_data:
        :return:
        """
        return 0
