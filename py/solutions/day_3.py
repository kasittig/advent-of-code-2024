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
            data_matches: list[tuple[str, str]] = re.findall("mul\((\d+),(\d+)\)", data)
            for a, b in data_matches:
                total += int(a) * int(b)

        return total

    @classmethod
    def solve_part_2(cls, input_data: list[str]) -> int:
        """
        Strategy:
        - Find indexes for the (stop, start) operator pairs
        - Remove the data at these entries
        - Add together the resulting strings
        """
        total = 0

        for data in input_data:
            while data:
                stop_idx = find_stop(data)
                start_idx = find_start(data)

                if stop_idx:
                    total += cls.solve_part_1(data[:stop_idx])
                    data = data[start_idx:] if start_idx else None
                else:
                    total += cls.solve_part_1([data])

                total += cls.solve_part_1([data[:stop_idx]])
                data = data[start_idx:] if start_idx else None
        return total
