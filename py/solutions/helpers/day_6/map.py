from solutions.helpers.day_6.guard import LabGuard


class LabGuardMap:
    def __init__(self, data: list[str]) -> None:
        self.rows: int = len(data)
        self.cols: int = len(data[0].strip())
        self.start_loc: tuple[int, int] = 0, 0

        self.base_obstacles: list[tuple[int, int]] = []

        for i in range(self.rows):
            for j in range(self.cols):
                if data[i][j] == "^":
                    self.start_loc = i, j
                elif data[i][j] == "#":
                    self.base_obstacles.append((i, j))

        self.obstacles: set[tuple[int, int]] = set(self.base_obstacles)
        self.guard = LabGuard(self.start_loc)

    def reset(self) -> None:
        self.obstacles: set[tuple[int, int]] = set(self.base_obstacles)
        self.guard = LabGuard(self.start_loc)

    def add_obstacle(self, i: int, j: int) -> None:
        # Can't add an obstacle where our guard starts
        assert self.start_loc != (i, j)
        # Doesn't make sense to add an obstacle where one already exists
        assert (i, j) not in self.obstacles
        self.obstacles.add((i, j))

    def do_guard_step(self) -> None:
        if self.guard.get_next_location() in self.obstacles:
            # Can't go through obstacle - try to turn
            self.guard.do_rotate()
        else:
            self.guard.do_step()

    def is_guard_on_map(self) -> bool:
        i, j = self.guard.location
        return 0 <= i < self.rows and 0 <= j < self.cols

    def count_visited(self) -> int:
        return len(self.guard.visited)

    def do_run_guard(self) -> None:
        while self.is_guard_on_map() and not self.guard.is_loop():
            self.do_guard_step()
