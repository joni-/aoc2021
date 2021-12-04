from typing import Callable

from common import count_by, read_input_lines, transpose


def _is_one(c: str) -> bool:
    return c == "1"


count_ones = count_by(_is_one)


def part1(input: list[str]) -> int:
    columns: list[str] = transpose(input)  # type: ignore
    size = len(input)
    gamma = ""
    epsilon = ""

    for col in columns:
        ones = count_ones(col)
        zeros = size - ones
        gamma = gamma + ("0" if ones > zeros else "1")
        epsilon = epsilon + ("1" if ones > zeros else "0")

    return int(gamma, 2) * int(epsilon, 2)


def part2(input: list[str]) -> int:
    ogr = _get_rating(input, _bit_criteria_ogr)
    co2_sr = _get_rating(input, _bit_criteria_co2_sr)
    return int(ogr, 2) * int(co2_sr, 2)


def _get_rating(input: list[str], bit_criteria: Callable[[int, int], str]) -> str:
    for position in range(len(input[0])):
        columns: list[str] = transpose(input)  # type: ignore
        bits = columns[position]
        ones = count_ones(bits)
        zeros = len(bits) - ones
        bit_to_keep = bit_criteria(ones, zeros)

        input = [row for row in input if row[position] == bit_to_keep]

        if len(input) == 1:
            return input[0]

    raise ValueError(f"Could not calculate rating for input {input}")


def _bit_criteria_ogr(ones: int, zeros: int) -> str:
    return "1" if ones >= zeros else "0"


def _bit_criteria_co2_sr(ones: int, zeros: int) -> str:
    return "0" if ones >= zeros else "1"


if __name__ == "__main__":
    data_in = read_input_lines(3, str)
    print(part1(data_in))
    print(part2(data_in))
