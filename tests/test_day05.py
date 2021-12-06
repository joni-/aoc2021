import pytest
from day05 import parse, part1, part2


@pytest.mark.parametrize("example, expected", [(True, 5), (False, 4745)])
def test_day05_part1(example: bool, expected: int):
    assert part1(parse(example=example)) == expected


@pytest.mark.parametrize("example, expected", [(True, 12), (False, 18442)])
def test_day05_part2(example: bool, expected: int):
    assert part2(parse(example=example)) == expected
