def add_multiply_values(m: int, n: int, concatenate: bool = False) -> list[int]:
    res = [m + n, m * n]
    if concatenate:
        res.append(int(f"{m}{n}"))
    return res


def get_possible_totals(
    entries: list[int], limit: int, concatenate: bool = False
) -> list[int]:
    totals = []

    for entry in entries:
        if len(totals) < 1:
            totals.append(entry)
        else:
            new_totals: list[int] = []
            for total in totals:
                new_totals.extend(add_multiply_values(total, entry, concatenate))
            totals = [t for t in new_totals if t <= limit]
    return totals
