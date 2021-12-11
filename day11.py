from common import Coordinate, Grid, get_neighbors, read_input_lines


def _step(
    neighbors: dict[Coordinate, list[Coordinate]], values: dict[Coordinate, int]
) -> tuple[dict[Coordinate, int], int]:

    for coord, value in values.items():
        values[coord] = values[coord] + 1

    flashed = set()
    process: list[Coordinate] = [coord for coord, _ in values.items()]

    while process:
        coord = process.pop()
        value = values[coord]

        if value > 9 and coord not in flashed:
            flashed.add(coord)

            for nb_coord in neighbors[coord]:
                values[nb_coord] = values[nb_coord] + 1

                if nb_coord not in flashed:
                    process.append(nb_coord)

    for coord in flashed:
        values[coord] = 0

    return values, len(flashed)


def part1(input: Grid[int]) -> int:
    neighbors: dict[Coordinate, list[Coordinate]] = {}
    values: dict[Coordinate, int] = {}

    for i, row in enumerate(input):
        for j, current_value in enumerate(row):
            current_coord = Coordinate(i, j)
            nbs = get_neighbors(input, current_coord, include_diagonals=True)
            neighbors[current_coord] = [coord for coord, value in nbs]
            values[current_coord] = current_value

    flashes = 0
    for _ in range(100):
        values, step_flashes = _step(neighbors, values)
        flashes += step_flashes

    return flashes


def part2(input: Grid[int]) -> int:
    neighbors: dict[Coordinate, list[Coordinate]] = {}
    values: dict[Coordinate, int] = {}

    for i, row in enumerate(input):
        for j, current_value in enumerate(row):
            current_coord = Coordinate(i, j)
            nbs = get_neighbors(input, current_coord, include_diagonals=True)
            neighbors[current_coord] = [coord for coord, value in nbs]
            values[current_coord] = current_value

    step = 1
    while True:
        values, _ = _step(neighbors, values)
        if all(map(lambda x: x == 0, values.values())):
            return step
        step += 1


def parse(*, example: bool = False) -> Grid[int]:
    lines = read_input_lines(11, str, example=example)
    result: list[list[int]] = []
    for line in lines:
        xs: list[int] = []
        for x in line:
            xs.append(int(x))
        result.append(xs)
    return result


if __name__ == "__main__":
    data_in = parse()
    print(part1(data_in))
    print(part2(data_in))
