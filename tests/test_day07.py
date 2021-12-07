import pytest
from day07 import parse, part1, part2


@pytest.mark.parametrize("example, expected", [(True, 37), (False, 336701)])
def test_day07_part1_1(example: bool, expected: int):
    assert part1(parse(example=example)) == expected


@pytest.mark.parametrize("example, expected", [(True, 168), (False, 95167302)])
def test_day07_part2_2(example: bool, expected: int):
    assert part2(parse(example=example)) == expected
