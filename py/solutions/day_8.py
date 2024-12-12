from typing import Any

from .base import BaseDailySolution
from solutions.helpers.grid_utils import parse_symbol_locations


class AntennaGrid:
    def __init__(self, data: list[str]) -> None:
        self.rows: int = len(data)
        self.cols: int = len(data[0].strip())
        self.antenna_locations: dict[str, list[tuple[int, int]]] = (
            parse_symbol_locations(data)
        )

    @classmethod
    def locate_potential_antinodes(
        cls, antenna_1: tuple[int, int], antenna_2: tuple[int, int]
    ) -> tuple[tuple[int, int], tuple[int, int]]:
        a1x, a1y = antenna_1
        a2x, a2y = antenna_2

        return (a1x + (a1x - a2x), a1y + (a1y - a2y)), (
            a2x + (a2x - a1x),
            a2y + (a2y - a1y),
        )

    def get_all_antinode_locations(self) -> set[tuple[int, int]]:
        locations: set[tuple[int, int]] = set()

        for _, coords in self.antenna_locations.items():
            for entry1 in coords:
                for entry2 in coords[1:]:
                    if entry1 == entry2:
                        continue
                    antinode1, antinode2 = self.locate_potential_antinodes(
                        entry1, entry2
                    )
                    if self.is_in_bounds(antinode1):
                        locations.add(antinode1)
                    if self.is_in_bounds(antinode2):
                        locations.add(antinode2)

        return locations

    def is_in_bounds(self, location: tuple[int, int]) -> bool:
        i, j = location
        return 0 <= i < self.rows and 0 <= j < self.cols


class Day8Solution(BaseDailySolution):
    DAY = 8

    @classmethod
    def format_data(cls, input_data: list[str]) -> AntennaGrid:
        return AntennaGrid(input_data)

    @classmethod
    def solve_part_1(cls, input_data: AntennaGrid) -> int:
        """
        Antennas have frequencies (character or letter label)
        Each pair of antennas creates two "antinodes" that are in line with the two antenna

        :param input_data:
        :return:
        """
        antinode_locations = input_data.get_all_antinode_locations()
        return len(antinode_locations)

    @classmethod
    def solve_part_2(cls, input_data: Any) -> int:
        """

        :param input_data:
        :return:
        """
        return 0
