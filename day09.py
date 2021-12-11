import math
from typing import Set

from common import Coordinate, Grid, get_neighbors, read_input_lines


def _get_low_points(input: Grid[int]) -> list[Coordinate]:
    matches: list[Coordinate] = []
    for i, row in enumerate(input):
        for j, col in enumerate(row):
            nbs = get_neighbors(input, Coordinate(i, j))

            if all(map(lambda nb: col < nb, [n for c, n in nbs])):
                matches.append(Coordinate(i, j))

    return matches


def part1(input: Grid[int]) -> int:
    low_points = _get_low_points(input)
    return sum([input[coord.row][coord.col] + 1 for coord in low_points])


def part2(input: Grid[int]) -> int:
    low_points = _get_low_points(input)
    basins = [_get_basin(point, input, {point}) for point in low_points]
    return math.prod(map(len, sorted(basins, key=len, reverse=True)[:3]))


def _get_basin(
    coord: Coordinate, input: Grid[int], acc: Set[Coordinate]
) -> Set[Coordinate]:
    nbs = get_neighbors(input, coord)
    current_value = input[coord.row][coord.col]
    for nb_coord, nb_value in nbs:
        if nb_value > current_value and nb_value != 9:
            acc = _get_basin(nb_coord, input, acc.union({nb_coord}))
    return acc


def parse(*, example: bool = False) -> Grid[int]:
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
