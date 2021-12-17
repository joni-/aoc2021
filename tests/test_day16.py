import pytest
from day16 import parse, part1, part2


@pytest.mark.parametrize("example, expected", [(True, 14), (False, 979)])
def test_day16_part1(example: bool, expected: int):
    assert part1(parse(example=example)) == expected


@pytest.mark.parametrize("example, expected", [(True, 3), (False, 277110354175)])
def test_day16_part2(example: bool, expected: int):
    assert part2(parse(example=example)) == expected
