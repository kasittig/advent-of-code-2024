from unittest import TestCase

from solutions.day_6 import Day6Solution, check_obstacle

example = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
]


class Day6SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Day6Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(41, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(6, self.solution.solve_part_2(self.data))

    def test_check_obstacle(self) -> None:
        looping_obstacles = [(9, 7), (6, 3), (7, 6), (7, 7), (8, 1), (8, 3)]

        for obstacle in looping_obstacles:
            assert check_obstacle(obstacle, self.data)

        for i in range(len(example)):
            for j in range(len(example[0].strip())):
                if (i, j) not in looping_obstacles:
                    assert not check_obstacle((i, j), self.data)


class Day6HelpersTestCase(TestCase):
    def test_helper(self) -> None:
        pass
