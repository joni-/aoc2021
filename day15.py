import queue
from collections import defaultdict
from typing import Iterable

from common import Grid, read_input_lines

Coord = tuple[int, int]


def _print_grid(grid: Grid[int], path: set[Coord]) -> None:
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if (i, j) in path:
                print("#".ljust(1), end="")
            else:
                print("".ljust(1), end="")
        print()


def dijkstra(grid: Grid[int]) -> tuple[dict[Coord, int], dict[Coord, Coord]]:
    pq: queue.Queue[tuple[int, Coord]] = queue.PriorityQueue()
    dist: dict[Coord, int] = defaultdict(int)
    prev: dict[Coord, Coord] = {}
    visited: set[Coord] = set()

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            v = (i, j)
            if (i, j) != (0, 0):
                dist[v] = 10000000000000
            pq.put((dist[v], v))

    dist[(0, 0)] = 0
    pq.put((0, (0, 0)))

    while not pq.empty():
        _, u = pq.get()

        for drow, dcol in ((0, 1), (0, -1), (-1, 0), (1, 0)):
            nb = (u[0] + drow, u[1] + dcol)

            if nb not in dist:
                continue

            alt = dist[u] + grid[nb[0]][nb[1]]

            if alt < dist[nb]:
                dist[nb] = alt
                prev[nb] = u
                pq.put((alt, nb))

        visited.add(u)

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
    # path = extract_path(parents, (0, 0), target)
    # _print_grid(input, set(path))
    return distances[target]


def part2(input: Grid[int]) -> int:
    large_grid = [row * 5 for row in input * 5]
    tile_increase: dict[int, int] = {}
    tile_size = len(input[0])

    for tile in range(25):
        increase = int(tile / 5) + tile % 5
        tile_increase[tile] = increase

    for i, row in enumerate(large_grid):
        for j, col in enumerate(row):
            r = i // tile_size
            c = j // tile_size
            tile = r * 5 + c
            large_grid[i][j] = (large_grid[i][j] - 1 + tile_increase[tile]) % 9 + 1

    distances, parents = dijkstra(large_grid)
    max_row = len(large_grid) - 1
    max_col = len(large_grid[0]) - 1
    target = (max_row, max_col)
    # path = extract_path(parents, (0, 0), target)
    # _print_grid(input, set(path))
    return distances[target]


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
