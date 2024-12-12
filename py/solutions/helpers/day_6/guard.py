class LabGuard:
    direction_map: dict[str, tuple[int, int]] = {
        "N": (-1, 0),
        "S": (1, 0),
        "E": (0, 1),
        "W": (0, -1),
    }
    next_direction: dict[str, str] = {"N": "E", "E": "S", "S": "W", "W": "N"}

    def __init__(
        self, start_location: tuple[int, int], start_direction: str = "N"
    ) -> None:
        self.location: tuple[int, int] = start_location
        self.direction: str = start_direction
        self.visited: set[tuple[int, int]] = set()

        # Initialize values for Floyd's cycle-finding algorithm
        self.path: list[tuple[int, int, str]] = []
        self.tortoise: int = 1
        self.hare: int = 2

    def get_next_location(self) -> tuple[int, int]:
        i, j = self.location
        delta_i, delta_j = self.direction_map[self.direction]
        return i + delta_i, j + delta_j

    def do_step(self) -> None:
        i, j = self.location
        self.path.append((i, j, self.direction))
        self.visited.add((i, j))
        self.location = self.get_next_location()

    def do_rotate(self) -> None:
        self.direction = self.next_direction[self.direction]

    def is_visited(self, i: int, j: int) -> bool:
        return (i, j) in self.visited

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
