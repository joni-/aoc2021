from common import count_by, read_input_lines


def _is_increasing(t: tuple[int, int]) -> bool:
    return t[0] < t[1]


count_increasing_pairs = count_by(_is_increasing)


def part1(input: list[int]) -> int:
    pairs = zip(input, input[1:])
    return count_increasing_pairs(pairs)


def part2(input: list[int]) -> int:
    window_sums = [sum(chunk) for chunk in zip(input, input[1:], input[2:])]
    pairs = zip(window_sums, window_sums[1:])
    return count_increasing_pairs(pairs)


if __name__ == "__main__":
    data_in = read_input_lines(1, lambda x: int(x))
    print(part1(data_in))
    print(part2(data_in))
