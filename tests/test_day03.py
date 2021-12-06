import pytest
from day03 import parse, part1, part2


@pytest.mark.parametrize("example, expected", [(True, 198), (False, 3882564)])
def test_day03_part1(example: bool, expected: int):
    assert part1(parse(example=example)) == expected


@pytest.mark.parametrize("example, expected", [(True, 230), (False, 3385170)])
def test_day03_part2(example: bool, expected: int):
    assert part2(parse(example=example)) == expected
