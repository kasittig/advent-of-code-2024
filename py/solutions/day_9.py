from typing import Any

from .base import BaseDailySolution


def expand_file(disk_map: str) -> list[str]:
    res: list[str] = []
    file_id = 0

    for i in range(len(disk_map)):
        if i % 2 == 0:
            # Data blocks
            res.extend([str(file_id)] * int(disk_map[i]))
            file_id += 1
        else:
            res.extend(["."] * int(disk_map[i]))
    return res


def compress_file(filestr: list[str]) -> list[str]:
    start_idx = 0
    end_idx = len(filestr) - 1
    res: list[str] = []

    while start_idx <= end_idx:
        start_chr: str = filestr[start_idx]
        end_chr: str = filestr[end_idx]

        if end_chr == ".":
            end_idx -= 1
        elif start_chr == ".":
            res.append(end_chr)
            end_idx -= 1
            start_idx += 1
        else:
            res.append(start_chr)
            start_idx += 1
    return res


def calculate_checksum(filestr: list[str]) -> int:
    checksum = 0
    for i in range(len(filestr)):
        checksum += int(filestr[i]) * i
    return checksum


class Day9Solution(BaseDailySolution):
    DAY = 9

    @classmethod
    def format_data(cls, input_data: list[str]) -> str:
        print(len(input_data[0]))
        return input_data[0].strip()

    @classmethod
    def solve_part_1(cls, input_data: str) -> int:
        """

        :param input_data:
        :return:
        """
        return calculate_checksum(compress_file(expand_file(input_data)))

    @classmethod
    def solve_part_2(cls, input_data: Any) -> int:
        """

        :param input_data:
        :return:
        """
        return 0
