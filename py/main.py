import inspect
import traceback
from cmd import Cmd
from importlib import reload
from types import ModuleType

import solutions
from core.codegen import generate_daily_template
from solutions.base import BaseDailySolution


def get_solution_classes_by_name() -> dict[str, type[BaseDailySolution]]:
    classes: dict[str, type[BaseDailySolution]] = {}
    modules: list[ModuleType] = [solutions]

    while len(modules) > 0:
        module = modules.pop()
        for name, obj in inspect.getmembers(module):
            if inspect.ismodule(obj):
                modules.append(obj)
            elif inspect.isclass(obj):
                if issubclass(obj, BaseDailySolution):
                    classes[name] = obj

    return classes


SOLUTION_CLASSES_BY_NAME = get_solution_classes_by_name()


def is_valid_day(day_str: str) -> bool:
    return (
        day_str.isdigit() and f"Day{day_str}Solution" in get_solution_classes_by_name()
    )


class AdventOfCodeCmdArgs:
    def __init__(self, day: str) -> None:
        self.day = day

    def is_valid(self) -> bool:
        return is_valid_day(self.day)


def parse_args(arg_str: str) -> AdventOfCodeCmdArgs:
    args = arg_str.split()
    day_str = args[0]
    return AdventOfCodeCmdArgs(day_str)


class AdventOfCodeCmd(Cmd):
    @staticmethod
    def do_exit(_) -> bool:
        print("Goodbye!")
        return True

    @staticmethod
    def do_list_days(_) -> None:
        print("Days with solutions:")
        days: list[str] = list(SOLUTION_CLASSES_BY_NAME.keys())
        for i in range(25):
            if f"Day{i}Solution" in days:
                print(f"* Day {i}")
        print(" ")

    @staticmethod
    def do_solve(args: str) -> None:
        if len(args) == 0:
            print("Error: must provide at least one argument (the day to run)!")
            return
        parsed_args = parse_args(args)
        if not parsed_args.is_valid():
            print(
                f"Error: no solution implemented for 2024 day {parsed_args.day}! Use "
                "the 'list_days' command to see all solved days by year."
            )
            return
        solution_class: type[BaseDailySolution] = SOLUTION_CLASSES_BY_NAME[
            f"Day{parsed_args.day}Solution"
        ]
        print(f"Running solution script for 2024 day {parsed_args.day}")
        try:
            solution_class.solve()
        except Exception:
            print(traceback.format_exc())

    @staticmethod
    def do_setup(args: str) -> None:
        if len(args) == 0:
            print("Error: must provide at least one argument (the day to run)!")
            return
        parsed_args = parse_args(args)
        if parsed_args.is_valid():
            print(
                f"Error: solution file already exists for 2024 day "
                f"{parsed_args.day}! Use the 'list_days' command to see all solved "
                "days by year."
            )
            return
        print(
            f"Generating template solution file and tests for 2024 day "
            f"{parsed_args.day}"
        )
        try:
            generate_daily_template(parsed_args.day)

            # Reload all the daily solutions in order to access our new solution
            reload(solutions)
        except Exception:
            print(traceback.format_exc())


if __name__ == "__main__":
    AdventOfCodeCmd().cmdloop()
