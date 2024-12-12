from .base import BaseDailySolution


class LabGuardMap:
    def __init__(self, data: list[str]) -> None:
        self.direction_map: dict[str, tuple[int, int]] = {
            "N": (-1, 0),
            "S": (1, 0),
            "E": (0, 1),
            "W": (0, -1),
        }

        self.rows: int = len(data)
        self.cols: int = len(data[0].strip())
        self.start_loc: tuple[int, int] = 0, 0
        self.start_dir: str = "N"

        self.base_direction_order: list[str] = ["E", "S", "W", "N"]
        self.base_obstacles: set[tuple[int, int]] = set()

        for i in range(self.rows):
            for j in range(self.cols):
                if data[i][j] == "^":
                    self.start_loc = i, j
                elif data[i][j] == "#":
                    self.base_obstacles.add((i, j))

        self.visited: set[tuple[int, int]] = set()
        self.guard_loc: tuple[int, int] = self.start_loc
        self.guard_dir: str = self.start_dir
        self.obstacles: set[tuple[int, int]] = self.base_obstacles

        self.direction_order: list[str] = self.base_direction_order

        # Initialize values for Floyd's cycle-finding algorithm
        self.path: list[tuple[int, int, str]] = []
        self.tortoise: int = 1
        self.hare: int = 2

    def reset_map(self) -> None:
        self.obstacles = set()
        self.visited: set[tuple[int, int]] = set()
        self.guard_loc: tuple[int, int] = self.start_loc
        self.guard_dir: str = self.start_dir
        self.obstacles: set[tuple[int, int]] = self.base_obstacles

        self.direction_order: list[str] = self.base_direction_order

        # Reset values for Floyd's cycle-finding algorithm
        self.path: list[tuple[int, int, str]] = []
        self.tortoise: int = 1
        self.hare: int = 2

    def mark_visited(self, i: int, j: int) -> None:
        self.visited.add((i, j))

    def is_visited(self, i: int, j: int) -> bool:
        return (i, j) in self.visited

    def add_obstacle(self, i: int, j: int) -> None:
        self.obstacles.add((i, j))

    def do_guard_step(self) -> None:
        i, j = self.guard_loc
        self.mark_visited(i, j)
        self.path.append((i, j, self.guard_dir))

        delta_i, delta_j = self.direction_map[self.guard_dir]

        if (i + delta_i, j + delta_j) in self.obstacles:
            # Can't go through obstacle - try to turn
            self.direction_order.append(self.guard_dir)
            self.guard_dir = self.direction_order[0]
            self.direction_order = self.direction_order[1:]
        else:
            self.guard_loc = i + delta_i, j + delta_j

    def is_guard_on_map(self) -> bool:
        i, j = self.guard_loc
        return 0 <= i < self.rows and 0 <= j < self.cols

    def count_visited(self) -> int:
        return len(self.visited)

    def is_loop(self) -> bool:
        try:
            if self.path[self.tortoise] == self.path[self.hare]:
                return True
            else:
                self.tortoise += 1
                self.hare += 2
                return False
        except IndexError:
            return False


class Day6Solution(BaseDailySolution):
    DAY = 6

    @classmethod
    def format_data(cls, input_data: list[str]) -> LabGuardMap:
        return LabGuardMap(input_data)

    @classmethod
    def solve_part_1(cls, input_data: LabGuardMap) -> int:
        input_data.reset_map()

        while input_data.is_guard_on_map():
            input_data.do_guard_step()

        return input_data.count_visited()

    @classmethod
    def solve_part_2(cls, input_data: LabGuardMap) -> int:
        obstacles = 0

        for i in range(input_data.rows):
            for j in range(input_data.cols):
                input_data.reset_map()

                if (i, j) in input_data.obstacles or (i, j) == input_data.start_loc:
                    continue
                input_data.add_obstacle(i, j)
                while input_data.is_guard_on_map() and not input_data.is_loop():
                    input_data.do_guard_step()
                obstacles += int(input_data.is_loop())

        return obstacles
