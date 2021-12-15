from collections import defaultdict
from typing import Iterable

from common import Grid, read_input_lines

Coord = tuple[int, int]


def _print_grid(grid: Grid[int], path: set[Coord]) -> None:
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if (i, j) in path:
                print("#".ljust(2), end="")
            else:
                print(str(col).ljust(2), end="")
        print()


def dijkstra(grid: Grid[int]) -> tuple[dict[Coord, int], dict[Coord, Coord]]:
    dist: dict[Coord, int] = defaultdict(int)
    prev: dict[Coord, Coord] = {}
    q: set[Coord] = set()

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            dist[(i, j)] = 100000000000
            q.add((i, j))
    dist[(0, 0)] = 0
    u = (0, 0)

    while q:
        u = _find_min(q, dist)
        q.remove(u)

        for drow, dcol in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nb = (u[0] + drow, u[1] + dcol)
            if nb not in q:
                continue

            alt = dist[u] + grid[nb[0]][nb[1]]

            if alt < dist[nb]:
                dist[nb] = alt
                prev[nb] = u

    return dist, prev


def extract_path(
    parents: dict[Coord, Coord], start: Coord, target: Coord
) -> Iterable[Coord]:
    path: list[Coord] = [target]
    v = parents[target]
    while v != start:
        path.append(v)
        v = parents[v]
    path.append(start)
    return reversed(path)


def part1(input: Grid[int]) -> int:
    distances, parents = dijkstra(input)
    max_row = len(input) - 1
    max_col = len(input[0]) - 1
    target = (max_row, max_col)
    path = extract_path(parents, (0, 0), target)
    return distances[target]


def _find_min(
    q: set[Coord],
    dist: dict[Coord, int],
) -> Coord:
    min_dist = 1000000000000
    min_v = None

    for v in q:
        if not v:
            min_v = v
        if dist[v] < min_dist:
            min_v = v
            min_dist = dist[v]

    return min_v  # type: ignore


def part2(input: Grid[int]) -> int:
    return 0


def parse(*, example: bool = False) -> Grid[int]:
    lines = read_input_lines(15, str, example=example)
    rows: Grid[int] = []
    for line in lines:
        row: list[int] = []
        for n in line:
            row.append(int(n))
        rows.append(row)
    return rows


if __name__ == "__main__":
    data_in = parse()
    print(part1(data_in))
    print(part2(data_in))
