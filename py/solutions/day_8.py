from typing import Any

from solutions.helpers.grid_utils import parse_symbol_locations

from .base import BaseDailySolution


class AntennaGrid:
    def __init__(self, data: list[str]) -> None:
        self.rows: int = len(data)
        self.cols: int = len(data[0].strip())
        self.antenna_locations: dict[str, list[tuple[int, int]]] = (
            parse_symbol_locations(data)
        )

    @classmethod
    def locate_antinodes_part_1(
        cls, antenna_1: tuple[int, int], antenna_2: tuple[int, int]
    ) -> tuple[tuple[int, int], tuple[int, int]]:
        a1x, a1y = antenna_1
        a2x, a2y = antenna_2

        return (a1x + (a1x - a2x), a1y + (a1y - a2y)), (
            a2x + (a2x - a1x),
            a2y + (a2y - a1y),
        )

    def locate_antinodes_part_2(
        self, antenna_1: tuple[int, int], antenna_2: tuple[int, int]
    ) -> set[tuple[int, int]]:
        antinodes: set[tuple[int, int]] = set()

        a1x, a1y = antenna_1
        a2x, a2y = antenna_2

        anti1: tuple[int, int] = antenna_1
        while self.is_in_bounds(anti1):
            antinodes.add(anti1)
            anti1x, anti1y = anti1
            anti1 = (anti1x + (a1x - a2x), anti1y + (a1y - a2y))

        anti2: tuple[int, int] = antenna_2
        while self.is_in_bounds(anti2):
            antinodes.add(anti2)
            anti2x, anti2y = anti2
            anti2 = (
                anti2x + (a2x - a1x),
                anti2y + (a2y - a1y),
            )

        return antinodes

    def get_antinode_locations_part_1(self) -> set[tuple[int, int]]:
        locations: set[tuple[int, int]] = set()

        for _, coords in self.antenna_locations.items():
            for entry1 in coords:
                for entry2 in coords[1:]:
                    if entry1 == entry2:
                        continue
                    antinode1, antinode2 = self.locate_antinodes_part_1(entry1, entry2)
                    if self.is_in_bounds(antinode1):
                        locations.add(antinode1)
                    if self.is_in_bounds(antinode2):
                        locations.add(antinode2)

        return locations

    def get_antinode_locations_part_2(self) -> set[tuple[int, int]]:
        locations: set[tuple[int, int]] = set()

        for _, coords in self.antenna_locations.items():
            for entry1 in coords:
                for entry2 in coords[1:]:
                    if entry1 == entry2:
                        continue
                    locations.update(self.locate_antinodes_part_2(entry1, entry2))

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

        :param input_data: the AntennaGrid with locations marked
        :return: the number of antinodes on the grid
        """
        antinode_locations = input_data.get_antinode_locations_part_1()
        return len(antinode_locations)

    @classmethod
    def solve_part_2(cls, input_data: Any) -> int:
        """
        Each pair of antennas creates as many antinodes that are in line with the two antenna as can fit on the grid

        :param input_data: the AntennaGrid with locations marked
        :return: the number of antinodes on the grid
        """
        antinode_locations = input_data.get_antinode_locations_part_2()
        return len(antinode_locations)
