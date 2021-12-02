from day02 import part1, part2

input = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]


def test_day02_part1():
    assert part1(input) == 150


def test_day02_part2():
    assert part2(input) == 900
