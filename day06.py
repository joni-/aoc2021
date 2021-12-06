from collections import defaultdict

from common import read_input


def _count_fishes(input: list[int], days: int) -> int:
    counts: dict[int, int] = defaultdict(int)

    for n in input:
        counts[n] = counts[n] + 1

    for _ in range(days):
        new_counts: dict[int, int] = defaultdict(int)
        for days_left, fish_count in counts.items():
            if days_left != 0:
                new_counts[days_left - 1] = fish_count
        new_counts[6] = new_counts[6] + counts[0]
        new_counts[8] = counts[0]
        counts = new_counts
    return sum(counts.values())


def part1(input: list[int]) -> int:
    return _count_fishes(input, 80)


def part2(input: list[int]) -> int:
    return _count_fishes(input, 256)


def parse(*, example: bool = False) -> list[int]:
    return [int(x) for x in read_input(6, example=example).split(",")]


if __name__ == "__main__":
    data_in = parse()
    print(part1(data_in))
    print(part2(data_in))
