from .base import BaseDailySolution

"""
Map each direction to an ordinal value to track directions:
1 2 3
4 X 5
6 7 8
"""


class WordSearchGrid:
    data: list[str]

    def __init__(self, data: list[str]) -> None:
        self.data = data
        self.xmas = "XMAS"
        self.rows = len(self.data)
        self.cols = len(self.data[0].strip())

    def get(self, i: int, j: int) -> str:
        """
        Get the letter entry at (i, j).

        :param i: the row of the target letter
        :param j: the column of the target letter
        :return: the value at (i, j)
        """
        try:
            return self.data[i][j]
        except IndexError:
            # It appears that there's one line that's misformatted
            return ""

    def is_in_bounds(self, i: int, j: int) -> bool:
        """
        Check if a value (i, j) is within the bounds of the grid.

        :param i: the row of the target letter
        :param j: the column of the target letter
        :return: a boolean representing whether (i, j) is within the bounds of the grid
        """

        return 0 <= i < self.rows and 0 <= j < self.cols

    def check_xmas(self, i: int, j: int, direction: tuple[int, int]) -> bool:
        for k in range(len(self.xmas)):
            if (not self.is_in_bounds(i, j)) or (self.get(i, j) != self.xmas[k]):
                return False
            else:
                i += direction[0]
                j += direction[1]
        return True

    def check_x_mas(self, i: int, j: int) -> bool:
        """
        Inspired by @francescopeluso (https://github.com/francescopeluso/AOC24/blob/main/day4/main.py#L51C1-L65C15)

        :param i: the row of the A
        :param j: the column of the A
        :return: whether this A is an X-MAS
        """
        if not (
            self.is_in_bounds(i - 1, j - 1)
            and self.is_in_bounds(i + 1, j - 1)
            and self.is_in_bounds(i - 1, j + 1)
            and self.is_in_bounds(i + 1, j + 1)
        ):
            return False

        patterns = ["MAS", "SAM"]

        l_diag = "".join(
            [self.data[i - 1][j - 1], self.data[i][j], self.data[i + 1][j + 1]]
        )
        r_diag = "".join(
            [self.data[i - 1][j + 1], self.data[i][j], self.data[i + 1][j - 1]]
        )

        if (l_diag in patterns and r_diag in patterns) or (
            l_diag[::-1] in patterns and r_diag[::-1] in patterns
        ):
            return True

        return False


class Day4Solution(BaseDailySolution):
    """
    Word search - find all instances of XMAS

    This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping
    other words.
    """

    DAY = 4

    @classmethod
    def format_data(cls, input_data: list[str]) -> WordSearchGrid:
        return WordSearchGrid(input_data)

    @classmethod
    def solve_part_1(cls, input_data: WordSearchGrid) -> int:
        """
        Strategy:

        For each X, explore the surrounding letters to check if any of them spell XMAS

        Map each direction to an ordinal value to track directions:
        1 2 3
        4 X 5
        6 7 8

        :param input_data: a list of rows in the word search
        :return: the number of times XMAS appears
        """
        grid = input_data
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        count = 0
        for i in range(grid.rows):
            for j in range(grid.cols):
                if grid.get(i, j) == "X":
                    for direction in directions:
                        count += int(grid.check_xmas(i, j, direction))
        return count

    @classmethod
    def solve_part_2(cls, input_data: WordSearchGrid) -> int:
        """
        Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle;
        it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is
        like this:

        M.S
        .A.
        M.S
        :param input_data: a list of rows in the word search
        :return: the number of X-MASes that appear
        """
        grid = input_data

        count = 0
        for i in range(grid.rows):
            for j in range(grid.cols):
                if grid.get(i, j) == "A":
                    count += int(grid.check_x_mas(i, j))
        return count
