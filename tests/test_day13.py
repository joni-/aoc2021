import pytest
from day13 import parse, part1, part2


@pytest.mark.parametrize("example, expected", [(True, 17), (False, 747)])
def test_day13_part1(example: bool, expected: int):
    assert part1(parse(example=example)) == expected


drawing = [
    " ##  ###  #  # #### ###   ##  #  # #  # ",
    "#  # #  # #  #    # #  # #  # #  # #  # ",
    "#  # #  # ####   #  #  # #    #  # #### ",
    "#### ###  #  #  #   ###  #    #  # #  # ",
    "#  # # #  #  # #    #    #  # #  # #  # ",
    "#  # #  # #  # #### #     ##   ##  #  # ",
]


@pytest.mark.parametrize("example, expected", [(False, drawing)])
def test_day13_part2(example: bool, expected: int):
    assert part2(parse(example=example)) == expected
