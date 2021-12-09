import pytest
from day09 import parse, part1, part2


@pytest.mark.parametrize("example, expected", [(True, 15), (False, 496)])
def test_day09_part1(example: bool, expected: int):
    assert part1(parse(example=example)) == expected


@pytest.mark.parametrize("example, expected", [(True, 1134), (False, 902880)])
def test_day09_part2(example: bool, expected: int):
    assert part2(parse(example=example)) == expected
