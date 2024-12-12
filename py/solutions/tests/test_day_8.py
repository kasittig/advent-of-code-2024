from unittest import TestCase

from solutions.day_8 import Day8Solution, AntennaGrid


example: list[str] = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............",
]


class Day8SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Day8Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(14, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(0, self.solution.solve_part_2(self.data))


class Day8HelpersTestCase(TestCase):
    def test_get_antinode_locations(self) -> None:
        antinodes = AntennaGrid.locate_potential_antinodes((3, 4), (5, 5))
        assert (1, 3) in antinodes
        assert (7, 6) in antinodes

        antinodes = AntennaGrid.locate_potential_antinodes((5, 5), (3, 4))
        assert (1, 3) in antinodes
        assert (7, 6) in antinodes
