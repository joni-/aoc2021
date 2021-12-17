import re
from collections import namedtuple

from common import read_input_lines

target_regex = re.compile(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d)")

Coord = namedtuple("Coord", ["x", "y"])


def _in_bounds(coord: Coord, bounds: tuple[Coord, Coord]) -> bool:
    top_left, bottom_right = bounds
    x_in_bounds = coord.x >= top_left.x and coord.x <= bottom_right.x
    y_in_bounds = coord.y >= top_left.y and coord.y <= bottom_right.y
    return x_in_bounds and y_in_bounds


def _out_of_reach(coord: Coord, bounds: tuple[Coord, Coord]) -> bool:
    top_left, bottom_right = bounds
    x_out = coord.x >= bottom_right.x
    y_out = coord.y <= bottom_right.y
    return x_out or y_out


def _draw(
    target: tuple[Coord, Coord],
    probe_positions: set[Coord],
) -> None:
    min_coord, max_coord = target
    max_y = max(max_coord.y, 0)
    min_y = min_coord.y - 1
    min_x = min(min_coord.x, 0)
    max_x = max_coord.x + 1

    for coord in probe_positions:
        max_y = max(max_y, coord.y)
        max_x = max(max_x, coord.x)

    for y in range(max_y, min_y, -1):
        for x in range(min_x, max_x):
            if x == 0 and y == 0:
                print("S", end="")
            elif Coord(x, y) in probe_positions:
                print("#", end="")
            elif _in_bounds(Coord(x, y), target):
                print("T", end="")
            else:
                print(".", end="")
        print()


def _step(coord: Coord, velocity: Coord) -> tuple[Coord, Coord]:
    coord = Coord(x=coord.x + velocity.x, y=coord.y + velocity.y)
    velocity_x = velocity.x
    if velocity_x != 0:
        velocity_x = velocity_x - 1 if velocity_x > 0 else velocity_x + 1

    return coord, Coord(x=velocity_x, y=velocity.y - 1)


def part1(input: tuple[Coord, Coord]) -> int:
    min_coord, max_coord = input
    ys: set[int] = set()

    # todo: slow as hell :D
    for y in range(1, 1000):
        for x in range(1, 1000):
            initial_velocity = Coord(x, y)
            velocity = Coord(x, y)
            probe = Coord(0, 0)
            probe_positions = set()

            while not _out_of_reach(probe, input):
                probe, velocity = _step(probe, velocity)
                probe_positions.add(probe)

            if any([_in_bounds(coord, input) for coord in probe_positions]):
                # print(initial_velocity)
                # _draw(input, probe_positions)
                # print()
                ys.add(max([coord.y for coord in probe_positions]))

    return max(ys)


def part2(input: tuple[Coord, Coord]) -> int:
    return 0


def parse(*, example: bool = False) -> tuple[Coord, Coord]:
    target = read_input_lines(17, str, example=example)[0]
    m = re.match(target_regex, target)
    x1, x2, y1, y2 = [int(x) for x in m.groups()]
    return (Coord(x1, y1), Coord(x2, y2))


if __name__ == "__main__":
    data_in = parse()
    print(part1(data_in))
    print(part2(data_in))
