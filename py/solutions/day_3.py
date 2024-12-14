import re

from .base import BaseDailySolution


def find_start(data: str) -> int | None:
    match = re.search("do\(\)", data)
    return re.Match.start(match) if match else None


def find_stop(data: str) -> int | None:
    match = re.search("don't\(\)", data)
    return re.Match.start(match) if match else None


class Day3Solution(BaseDailySolution):
    DAY = 3

    @classmethod
    def solve_part_1(cls, input_data: list[str]) -> int:
        total = 0
        for data in input_data:
            data_matches: list[tuple[str, str]] = re.findall(
                "mul\((\d+),(\d+)\)", data
            )
            for a, b in data_matches:
                total += int(a) * int(b)

        return total

    @classmethod
    def solve_part_2(cls, input_data: list[str]) -> int:
        """
        There are two new instructions you'll need to handle:
        - The do() instruction enables future mul instructions.
        - The don't() instruction disables future mul instructions.

        Strategy:
        - Find indexes for the (stop, start) operator pairs
        - Remove the data at these entries
        - Add together the resulting strings

        IMPORTANT!!! Data is split over multiple lines but is one continuous entry
        """
        total = 0

        data = "".join(input_data)

        while data:
            stop_idx = find_stop(data)

            if stop_idx:
                entry, rest = data[:stop_idx], data[stop_idx:]
                total += cls.solve_part_1([entry])
                start_idx = find_start(rest)
                data = rest[start_idx:]
            else:
                total += cls.solve_part_1([data])
                data = None

        return total
