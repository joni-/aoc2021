from typing import Callable

from common import read_input


def _align_crabs(input: list[int], get_fuel_consumption: Callable[[int], int]) -> int:
    min_fuel = 10000000000000

    for target in range(min(input), max(input) + 1):
        fuel_to_target = 0
        for position in input:
            steps = abs(target - position)
            fuel_to_target += get_fuel_consumption(steps)
        min_fuel = min(fuel_to_target, min_fuel)

    return min_fuel


def part1(input: list[int]) -> int:
    return _align_crabs(input, lambda steps: steps)


def part2(input: list[int]) -> int:
    return _align_crabs(input, lambda steps: int((steps ** 2 + steps) / 2))


def parse(*, example: bool = False) -> list[int]:
    return [int(x.strip()) for x in read_input(7, example=example).strip().split(",")]


if __name__ == "__main__":
    data_in = parse()
    print(part1(data_in))
    print(part2(data_in))
