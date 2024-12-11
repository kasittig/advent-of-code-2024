from .base import BaseDailySolution


def is_pair_safe(entry_1: int, entry_2: int, increasing: bool) -> bool:
    return (1 <= abs(entry_2 - entry_1) <= 3) and (
        (entry_1 < entry_2 and increasing) or (entry_1 > entry_2 and not increasing)
    )


def is_report_safe(report: list[int]) -> bool:
    assert len(report) > 2
    increasing: bool = report[0] < report[1]
    safe: bool = True
    for i in range(len(report) - 1):
        safe = is_pair_safe(report[i], report[i + 1], increasing)
        if not safe:
            break
    return safe


class Day2Solution(BaseDailySolution):
    DAY = 2

    @classmethod
    def format_data(cls, input_data: list[str]) -> list[list[int]]:
        ret: list[list[int]] = []
        for line in input_data:
            ret.append([int(i) for i in line.strip().split()])
        return ret

    @classmethod
    def solve_part_1(cls, input_data: list[list[int]]) -> int:
        safe_reports = 0
        for report in input_data:
            safe_reports += int(is_report_safe(report))

        return safe_reports

    @classmethod
    def solve_part_2(cls, input_data: list[list[int]]) -> int:
        safe_reports = 0
        for report in input_data:
            if is_report_safe(report):
                safe_reports += 1
            else:
                for i in range(len(report)):
                    test_report = report[:i] + report[i + 1 :]
                    if is_report_safe(test_report):
                        safe_reports += 1
                        break

        return safe_reports
