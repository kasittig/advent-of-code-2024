def add_multiply_values(m: int, n: int) -> list[int]:
    return [m + n, m * n]


def get_possible_totals(entries: list[int], limit: int) -> list[int]:
    totals = []

    for entry in entries:
        if len(totals) < 1:
            totals.append(entry)
        else:
            new_totals: list[int] = []
            for total in totals:
                new_totals.extend(add_multiply_values(entry, total))
            totals = [t for t in new_totals if t <= limit]
    return totals
