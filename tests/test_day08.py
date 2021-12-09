import pytest
from day08 import parse, part1, part2


@pytest.mark.parametrize("example, expected", [(True, 26), (False, 532)])
def test_day08_part1_1(example: bool, expected: int):
    assert part1(parse(example=example)) == expected


@pytest.mark.parametrize("example, expected", [(True, 61229), (False, 1011284)])
def test_day08_part2_2(example: bool, expected: int):
    assert part2(parse(example=example)) == expected
