import os
import sys
from typing import Callable, Iterable, NamedTuple, TypeVar

T = TypeVar("T")
Grid = list[list[T]]


def count_by(pred: Callable[[T], bool]) -> Callable[[Iterable[T]], int]:
    def counter(seq: Iterable[T]) -> int:
        count = 0
        for x in seq:
            if pred(x):
                count += 1
        return count

    return counter


def transpose(lst: list[list[T]]) -> list[list[T]]:
    transposed = [*zip(*lst)]  # https://stackoverflow.com/a/11387441/586301
    return [list(x) for x in transposed]


def read_input(day: int, *, example: bool = False) -> str:
    input_file = "day" + str(day).zfill(2) + (".example" if example else "") + ".in"
    path = (
        sys.argv[1]
        if len(sys.argv) > 1
        and os.path.exists(sys.argv[1])
        and not sys.argv[1].startswith("tests")
        else os.path.join(os.path.dirname(__file__), "inputs", input_file)
    )
    return open(path, "r").read()


def read_input_lines(
    day: int, mapper: Callable[[str], T], *, example: bool = False
) -> list[T]:
    return [mapper(x) for x in read_input(day, example=example).splitlines()]


class Coordinate(NamedTuple):
    row: int
    col: int


def get_neighbors(
    grid: Grid[T],
    coord: Coordinate,
    include_diagonals: bool = False,
) -> list[tuple[Coordinate, T]]:
    bottom_right = _get_bottom_right(grid)
    return [
        (nb_coord, grid[nb_coord.row][nb_coord.col])
        for nb_coord in _get_neighbor_indexes(
            coord, bottom_right=bottom_right, include_diagonals=include_diagonals
        )
    ]


def _get_neighbor_indexes(
    coordinate: Coordinate, bottom_right: Coordinate, include_diagonals: bool = False
) -> list[Coordinate]:
    def _is_valid(c: Coordinate) -> bool:
        if not include_diagonals:
            if coordinate.row != c.row and coordinate.col != c.col:
                return False
        return (
            c.row >= 0
            and c.row <= bottom_right.row
            and c.col >= 0
            and c.col <= bottom_right.col
        )

    deltas = (
        (-1, 0),
        (-1, 1),
        (-1, -1),
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
        (0, -1),
    )
    neighbors = [
        Coordinate(coordinate.row + dx, coordinate.col + dy) for dx, dy in deltas
    ]
    return [c for c in neighbors if _is_valid(c)]


def _get_bottom_right(grid: Grid[T]) -> Coordinate:
    row = len(grid)
    col = len(grid[0])
    return Coordinate(row - 1, col - 1)
