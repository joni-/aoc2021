import pytest
from day02 import parse, part1, part2


@pytest.mark.parametrize("example, expected", [(True, 150), (False, 1746616)])
def test_day02_part1(example: bool, expected: int):
    assert part1(parse(example=example)) == expected


@pytest.mark.parametrize("example, expected", [(True, 900), (False, 1741971043)])
def test_day02_part2(example: bool, expected: int):
    assert part2(parse(example=example)) == expected
