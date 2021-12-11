import pytest
from day11 import parse, part1, part2


@pytest.mark.parametrize("example, expected", [(True, 1656), (False, 1725)])
def test_day11_part1(example: bool, expected: int):
    assert part1(parse(example=example)) == expected


@pytest.mark.parametrize("example, expected", [(True, 195), (False, 308)])
def test_day11_part2(example: bool, expected: int):
    assert part2(parse(example=example)) == expected
