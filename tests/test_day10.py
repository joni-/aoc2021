import pytest
from day10 import parse, part1, part2


@pytest.mark.parametrize("example, expected", [(True, 26397), (False, 271245)])
def test_day10_part1_1(example: bool, expected: int):
    assert part1(parse(example=example)) == expected


@pytest.mark.parametrize("example, expected", [(True, 288957), (False, 1685293086)])
def test_day10_part2_2(example: bool, expected: int):
    assert part2(parse(example=example)) == expected
