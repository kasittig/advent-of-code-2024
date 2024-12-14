from solutions.helpers.day_6 import LabGuardMap

from .base import BaseDailySolution


def check_obstacle(obstacle: tuple[int, int], lab_map: LabGuardMap) -> bool:
    lab_map.reset()
    try:
        lab_map.add_obstacle(*obstacle)
        lab_map.do_run_guard()
        return lab_map.guard.is_loop()
    except AssertionError:
        return False


class Day6Solution(BaseDailySolution):
    DAY = 6

    @classmethod
    def format_data(cls, input_data: list[str]) -> LabGuardMap:
        return LabGuardMap(input_data)

    @classmethod
    def solve_part_1(cls, input_data: LabGuardMap) -> int:
        """
        How many distinct positions will the guard visit before leaving the mapped area?

        :param input_data: an object representing the base map with starting guard location
        :return: the number locations the guard visits before leaving the bounds of the map
        """
        input_data.reset()
        input_data.do_run_guard()
        return input_data.count_visited()

    @classmethod
    def solve_part_2(cls, input_data: LabGuardMap) -> int:
        """
        You need to get the guard stuck in a loop by adding a single new obstruction.
        How many different positions could you choose for this obstruction?

        Note - this method is pretty slow. It would be great to parallelize this operation!

        :param input_data: an object representing the base map with starting guard location
        :return: the number of possible obstacle locations that would cause the guard to loop
        """
        obstacles = 0
        checked = 0
        options = input_data.rows * input_data.cols

        for i in range(input_data.rows):
            for j in range(input_data.cols):
                obstacles += int(check_obstacle((i, j), input_data))
                checked += 1
                if checked % 100 == 0:
                    print(f"checked {checked}/{options} locations")

        return obstacles
