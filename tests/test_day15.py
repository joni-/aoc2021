import pytest
from day15 import parse, part1, part2


@pytest.mark.parametrize("example, expected", [(True, 40), (False, 581)])
def test_day15_part1(example: bool, expected: int):
    assert part1(parse(example=example)) == expected


@pytest.mark.parametrize("example, expected", [(True, 0), (False, 0)])
def test_day15_part2(example: bool, expected: int):
    assert part2(parse(example=example)) == expected
