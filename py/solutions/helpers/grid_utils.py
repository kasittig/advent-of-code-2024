from collections import defaultdict


def parse_symbol_locations(
    grid: list[str], skip_char: str = "."
) -> dict[str, list[tuple[int, int]]]:
    locations: dict[str, list[tuple[int, int]]] = defaultdict(list)

    for i in range(len(grid)):
        for j in range(len(grid[0].strip())):
            entry = grid[i][j]
            if entry == skip_char:
                continue
            else:
                locations[entry].append((i, j))
    return locations
