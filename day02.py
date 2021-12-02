from typing import List, Tuple

from common import read_input_lines


def _get_direction(instruction: str) -> Tuple[str, int]:
    direction, step_size = instruction.split(" ")
    return direction, int(step_size)


def part1(input: List[str]) -> int:
    x, y = 0, 0
    steps = [_get_direction(step) for step in input]

    for direction, amount in steps:
        if direction == "forward":
            x += amount
        elif direction == "down":
            y += amount
        elif direction == "up":
            y -= amount

    return x * y


def part2(input: List[str]) -> int:
    x, y, aim = 0, 0, 0
    steps = [_get_direction(step) for step in input]

    for direction, amount in steps:
        if direction == "forward":
            x += amount
            y += aim * amount
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount

    return x * y


if __name__ == "__main__":
    data_in = read_input_lines(2, lambda x: x)
    print(part1(data_in))
    print(part2(data_in))
