from day01 import part1, part2


def test_day01_part1():
    input = """199
200
208
210
200
207
240
269
260
263
"""
    assert part1(input) == 7


def test_day01_part2():
    input = """199
200
208
210
200
207
240
269
260
263
"""
    assert part2(input) == 5
