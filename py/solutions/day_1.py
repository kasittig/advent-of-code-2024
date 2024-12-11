from .base import BaseDailySolution
from core.utils import get_frequency_counts


class Day1Solution(BaseDailySolution):
    DAY = 1

    @classmethod
    def format_data(cls, input_data: list[str]) -> tuple[list[int], list[int]]:
        list1: list[int] = []
        list2: list[int] = []

        for line in input_data:
            line = line.strip().split()
            list1.append(int(line[0]))
            list2.append(int(line[1]))
        return list1, list2

    @classmethod
    def solve_part_1(cls, input_data: tuple[list[int], list[int]]) -> int:
        list_1, list_2 = input_data

        list_1.sort()
        list_2.sort()
        difference = 0

        for a, b in zip(list_1, list_2):
            difference += abs(a - b)
        return difference

    @classmethod
    def solve_part_2(cls, input_data: tuple[list[int], list[int]]) -> int:
        list_1, list_2 = input_data

        list_2_counts: dict[int, int] = get_frequency_counts(list_2)

        similarity_score = 0
        for elt in list_1:
            similarity_score += elt * list_2_counts[elt]
        return similarity_score
