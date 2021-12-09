import math
from typing import NamedTuple, Set

from common import read_input_lines


class Coordinate(NamedTuple):
    row: int
    col: int


def _get_neighbor_indexes(
    coord: Coordinate, max_row: int, max_col: int
) -> list[Coordinate]:
    top = Coordinate(coord.row - 1, coord.col) if coord.row - 1 >= 0 else None
    right = Coordinate(coord.row, coord.col + 1) if coord.col + 1 < max_col else None
    down = Coordinate(coord.row + 1, coord.col) if coord.row + 1 < max_row else None
    left = Coordinate(coord.row, coord.col - 1) if coord.col - 1 >= 0 else None
    return [c for c in [top, right, down, left] if c is not None]


def _get_neighbors(
    input: list[list[int]], coord: Coordinate, max_row: int, max_col: int
) -> list[tuple[Coordinate, int]]:
    nbs = _get_neighbor_indexes(coord, max_row, max_col)
    xs = []
    for coord in nbs:
        xs.append((coord, input[coord.row][coord.col]))
    return xs


def _get_low_points(input: list[list[int]]) -> list[Coordinate]:
    matches: list[Coordinate] = []

    max_row = len(input)
    max_col = len(input[0])

    for i, row in enumerate(input):
        for j, col in enumerate(row):
            nbs = _get_neighbors(input, Coordinate(i, j), max_row, max_col)

            if all(map(lambda nb: col < nb, [n for c, n in nbs])):
                matches.append(Coordinate(i, j))

    return matches


def part1(input: list[list[int]]) -> int:
    low_points = _get_low_points(input)
    return sum([input[coord.row][coord.col] + 1 for coord in low_points])


def part2(input: list[list[int]]) -> int:
    low_points = _get_low_points(input)
    basins = [_get_basin(point, input, {point}) for point in low_points]
    return math.prod(map(len, sorted(basins, key=len, reverse=True)[:3]))


def _get_basin(
    coord: Coordinate, input: list[list[int]], acc: Set[Coordinate]
) -> Set[Coordinate]:
    max_row = len(input)
    max_col = len(input[0])
    nbs = _get_neighbors(input, coord, max_row, max_col)
    current_value = input[coord.row][coord.col]
    for nb_coord, nb_value in nbs:
        if nb_value > current_value and nb_value != 9:
            acc = _get_basin(nb_coord, input, acc.union({nb_coord}))
    return acc


def parse(*, example: bool = False) -> list[list[int]]:
    lines = read_input_lines(9, str, example=example)
    ns = []
    for line in lines:
        nss = []
        for x in line:
            nss.append(int(x))
        ns.append(nss)
    return ns


if __name__ == "__main__":
    data_in = parse()
    print(part1(data_in))
    print(part2(data_in))
