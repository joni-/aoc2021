import pytest
from day04 import parse, part1, part2


@pytest.mark.parametrize("example, expected", [(True, 4512), (False, 16716)])
def test_day04_part1(example: bool, expected: int):
    assert part1(parse(example=example)) == expected


@pytest.mark.parametrize("example, expected", [(True, 1924), (False, 4880)])
def test_day04_part2(example: bool, expected: int):
    assert part2(parse(example=example)) == expected
