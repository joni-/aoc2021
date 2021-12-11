import re
from collections import defaultdict, namedtuple

from common import count_by, read_input_lines

Point = namedtuple("Point", ["x", "y"])
line_regex = re.compile(r"^(\d+),(\d+) -> (\d+),(\d+)$")


def overlaps(item: tuple[Point, int]) -> bool:
    return item[1] >= 2


count_overlapping_points = count_by(overlaps)


def _parse_lines(input: list[str]) -> list[tuple[Point, Point]]:
    lines: list[tuple[Point, Point]] = []
    for line in input:
        m = re.match(line_regex, line)
        if m:
            x1, y1, x2, y2 = [int(x) for x in m.groups()]
            lines.append((Point(x1, y1), Point(x2, y2)))
    return lines


def part1(input: list[str]) -> int:
    lines = [
        (start, end)
        for start, end in _parse_lines(input)
        if start.x == end.x or start.y == end.y
    ]

    counts: dict[Point, int] = defaultdict(int)

    for start, end in lines:
        for x in range(min(start.x, end.x), max(start.x, end.x) + 1):
            for y in range(min(start.y, end.y), max(start.y, end.y) + 1):
                counts[Point(x, y)] = counts[Point(x, y)] + 1

    # _draw(_parse_lines(input), counts)
    return count_overlapping_points(counts.items())  # type: ignore


def part2(input: list[str]) -> int:
    lines = [
        (start, end)
        for start, end in _parse_lines(input)
        if start.x == end.x or start.y == end.y
    ]
    diagonals = [
        (start, end)
        for start, end in _parse_lines(input)
        if start.x != end.x and start.y != end.y
    ]

    counts: dict[Point, int] = defaultdict(int)

    for start, end in lines:
        for x in range(min(start.x, end.x), max(start.x, end.x) + 1):
            for y in range(min(start.y, end.y), max(start.y, end.y) + 1):
                counts[Point(x, y)] = counts[Point(x, y)] + 1

    for start, end in diagonals:
        for step in range(max(start.x, end.x) - min(start.x, end.x) + 1):
            point = Point(
                start.x - step if start.x > end.x else start.x + step,
                start.y - step if start.y > end.y else start.y + step,
            )
            counts[point] = counts[point] + 1

    # _draw(_parse_lines(input), counts)
    return count_overlapping_points(counts.items())  # type: ignore


def _draw(lines: list[tuple[Point, Point]], counts: dict[Point, int]):
    max_x = max([max(start.x, end.x) for start, end in lines])
    max_y = max([max(start.y, end.y) for start, end in lines])

    for y in range(max_y + 1):
        row = ""
        for x in range(max_x + 1):
            mark = counts[Point(x, y)] or "."
            row += str(mark)
        print(row)


def parse(*, example: bool = False) -> list[str]:
    return read_input_lines(5, str, example=example)


if __name__ == "__main__":
    data_in = parse()
    print(part1(data_in))
    print(part2(data_in))
