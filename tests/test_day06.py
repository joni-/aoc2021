import pytest
from day06 import parse, part1, part2


@pytest.mark.parametrize("example, expected", [(True, 5934), (False, 391671)])
def test_day06_part1(example: bool, expected: int):
    assert part1(parse(example=example)) == expected


@pytest.mark.parametrize(
    "example, expected", [(True, 26984457539), (False, 1754000560399)]
)
def test_day06_part2(example: bool, expected: int):
    assert part2(parse(example=example)) == expected
