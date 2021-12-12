import pytest
from day12 import parse, part1, part2


@pytest.mark.parametrize("example, expected", [(True, 226), (False, 4413)])
def test_day12_part1(example: bool, expected: int):
    assert part1(parse(example=example)) == expected


@pytest.mark.parametrize("example, expected", [(True, 3509), (False, 118803)])
def test_day12_part2(example: bool, expected: int):
    assert part2(parse(example=example)) == expected
