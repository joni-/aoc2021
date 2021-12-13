import re

from common import Coordinate, Grid, read_input

Input = tuple[list[Coordinate], list[tuple[str, int]]]
fold_regex = re.compile(r"fold along ([xy])=(\d+)$")


def _max_coordinate(coordinates: list[Coordinate]) -> Coordinate:
    rows = [c.row for c in coordinates]
    cols = [c.col for c in coordinates]
    return Coordinate(max(rows), max(cols))


def _fold_up(grid: Grid[bool], position: int) -> Grid:
    grid = grid.copy()
    top = grid[:position]
    bottom = grid[position + 1 :]

    new_grid = top if len(top) >= len(bottom) else bottom[::-1]
    overlays = bottom[::-1] if new_grid is top else top
    delta_row = len(new_grid) - len(overlays)

    for i, row in enumerate(overlays):
        for j, col in enumerate(row):
            new_grid[delta_row + i][j] = new_grid[delta_row + i][j] or col

    return new_grid


def _fold_right(grid: Grid[bool], position: int) -> Grid:
    grid = grid.copy()
    new_grid: Grid[bool] = []

    for i, row in enumerate(grid):
        left = row[:position]
        right = row[position + 1 :]

        new_row = right if len(right) >= len(left) else left[::-1]
        overlays = left[::-1] if new_row is right else right

        for j, col in enumerate(new_row):
            if j < len(overlays):
                new_row[j] = new_row[j] or overlays[j]
            else:
                new_row[j] = new_row[j]

        new_grid.append(new_row)

    return new_grid


def part1(input: Input) -> int:
    coordinates, folds = input
    max_coord = _max_coordinate(coordinates)
    coord_set = set(coordinates)
    grid: Grid[bool] = []

    for row in range(max_coord.row + 1):
        r: list[bool] = []
        for col in range(max_coord.col + 1):
            r.append(True if Coordinate(row, col) in coord_set else False)
        grid.append(r)

    axis, index = folds[0]
    folded_grid = grid
    if axis == "y":
        folded_grid = _fold_up(folded_grid, index)
    else:
        folded_grid = _fold_right(folded_grid, index)

    return sum([col for row in folded_grid for col in row if col])


def _draw(grid: Grid[bool]) -> list[str]:
    drawing: list[str] = []
    for row in grid:
        r = []
        for col in row[::-1]:
            r.append("#" if col else " ")
        drawing.append("".join(r))
    return drawing


def part2(input: Input) -> list[str]:
    coordinates, folds = input
    max_coord = _max_coordinate(coordinates)
    coord_set = set(coordinates)

    grid: Grid[bool] = []

    for row in range(max_coord.row + 1):
        r: list[bool] = []
        for col in range(max_coord.col + 1):
            r.append(True if Coordinate(row, col) in coord_set else False)
        grid.append(r)

    folded_grid = grid

    for axis, index in folds:
        if axis == "y":
            folded_grid = _fold_up(folded_grid, index)
        else:
            folded_grid = _fold_right(folded_grid, index)

    drawing = _draw(folded_grid)
    return drawing


def parse(*, example: bool = False) -> Input:
    full_input = read_input(13, example=example)
    [coordinates, folds] = full_input.split("\n\n")

    coords: list[Coordinate] = []
    for coord in coordinates.splitlines():
        [col, row] = coord.split(",")
        coords.append(Coordinate(int(row), int(col)))

    foldss: list[tuple[str, int]] = []

    for fold in folds.splitlines():
        m = re.match(fold_regex, fold)
        if m:
            direction = m.groups()[0]
            along = int(m.groups()[1])
            foldss.append((direction, along))

    return (coords, foldss)


if __name__ == "__main__":
    data_in = parse()
    print(part1(data_in))
    print(part2(data_in))
