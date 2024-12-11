import os
from collections import defaultdict
from typing import Any, Iterable


def validate_and_read_file(filepath: str) -> list[str]:
    """
    Helper function to read a file from a directory, if the file exists.
    Throws an error if the file does not exist.

    :param filepath: the string location of the file to be read
    :return: a list of lines in the file
    :raises: FileNotFoundError if the file does not exist
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Error: no file found at {filepath}")
    return open(filepath).readlines()


def get_default_input_filename(day: str) -> str:
    """
    Helper function to get the path of a given day's input data file.

    :param day: The Advent of Code day for this problem
    :return: string location of the input file (e.g. inputs/day_{day}.txt)
    """
    return f"inputs/day_{day}.txt"


def get_default_solution_filename(day: str) -> str:
    """
    Helper function to get the path of a given day's solution file.

    :param day: The Advent of Code day for this problem
    :return: string location of the solution file (e.g. solutions/day_{day}.py)
    """
    return f"solutions/day_{day}.py"


def get_default_test_filename(day: str) -> str:
    """
    Helper function to get the path of a given day's test file for its solutions.

    :param day: The Advent of Code day for this problem
    :return: string location of the test file (e.g. solutions/tests/test_day_{day}.py)
    """
    return f"solutions/tests/test_day_{day}.py"


def group_entries_by_line_break(input_lines: list[str]) -> list[list[str]]:
    entries: list[list[str]] = []
    current_entry: list[str] = []

    for line in input_lines:
        line = line.strip()
        if line == "":
            entries.append(current_entry)
            current_entry = []
        else:
            current_entry.append(line.strip())

    if current_entry:
        entries.append(current_entry)
    return entries


def get_frequency_counts(input_list: Iterable[Any]) -> dict[Any, int]:
    """
    Count the number of times each entry appears in an input_list.

    :param input_list: a list of input values to be counted
    :return: a dict mapping {entry: count} for each entry in the input_list
    """
    count_dict: dict[Any, int] = defaultdict(int)
    for elt in input_list:
        count_dict[elt] += 1
    return count_dict


def get_unique_entries(entry: Iterable[Any]) -> set[Any]:
    return {e for e in entry}
