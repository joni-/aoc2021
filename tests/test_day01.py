import pytest
from day01 import parse, part1, part2


@pytest.mark.parametrize("example, expected", [(True, 7), (False, 1624)])
def test_day01_part1(example: bool, expected: int):
    assert part1(parse(example=example)) == expected


@pytest.mark.parametrize("example, expected", [(True, 5), (False, 1653)])
def test_day01_part2(example: bool, expected: int):
    assert part2(parse(example=example)) == expected
