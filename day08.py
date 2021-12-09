from collections import Counter
from dataclasses import dataclass

from common import read_input_lines


@dataclass
class Entry:
    patterns: list[str]
    outputs: list[str]


def get_zero(patterns: list[str]) -> str:
    eight = get_eight(patterns)
    d = segment_d(patterns)
    [zero] = [p for p in patterns if set(eight) - set(p) == set(d)]
    return zero


def get_one(patterns: list[str]) -> str:
    [one] = [p for p in patterns if len(p) == 2]
    return one


def get_two(patterns: list[str]) -> str:
    f = segment_f(patterns)
    [two] = [p for p in patterns if f not in p]
    return two


def get_three(patterns: list[str]) -> str:
    seven = get_seven(patterns)
    g = segment_g(patterns)
    seven_g = set(seven + g)
    [three] = [p for p in patterns if len(set(p) - seven_g) == 1]
    return three


def get_four(patterns: list[str]) -> str:
    [four] = [p for p in patterns if len(p) == 4]
    return four


def get_five(patterns: list[str]) -> str:
    one = set(get_one(patterns))
    nine = set(get_nine(patterns))
    [five] = [p for p in patterns if len(p) == 5 and set(one).union(p) == nine]
    return five


def get_six(patterns: list[str]) -> str:
    one = set(get_one(patterns))
    eight = set(get_eight(patterns))
    [six] = [
        p
        for p in patterns
        if len(p) == 6 and len(set(one).union(p)) == 7 and p != eight
    ]
    return six


def get_seven(patterns: list[str]) -> str:
    [seven] = [p for p in patterns if len(p) == 3]
    return seven


def get_eight(patterns: list[str]) -> str:
    [eight] = [p for p in patterns if len(p) == 7]
    return eight


def get_nine(patterns: list[str]) -> str:
    four = get_four(patterns)
    a = segment_a(patterns)
    four_a = set(four + a)
    nine_candidates = [p for p in patterns if len(p) == 6]
    # add "signal a" to four, find possibilities for 9 and for each, take diff
    # between 9 and 4 and you get g
    [nine] = [c for c in nine_candidates if len(set(c) - set(four_a)) == 1]
    return nine


def segment_a(patterns: list[str]) -> str:
    one = get_one(patterns)
    seven = get_seven(patterns)
    return (set(seven) - set(one)).pop()


def segment_b(patterns: list[str]) -> str:
    four = get_four(patterns)
    one = get_one(patterns)
    zero = get_zero(patterns)
    return (set(four) - set(one)).intersection(zero).pop()


def segment_c(patterns: list[str]) -> str:
    one = get_one(patterns)
    f = segment_f(patterns)
    return (set(one) - set(f)).pop()


def segment_d(patterns: list[str]) -> str:
    three = get_three(patterns)
    seven = get_seven(patterns)
    g = segment_g(patterns)
    return (set(three) - set((seven + g))).pop()


def segment_e(patterns: list[str]) -> str:
    eight = get_eight(patterns)
    nine = get_nine(patterns)
    return (set(eight) - set(nine)).pop()


def segment_f(patterns: list[str]) -> str:
    counts = Counter("".join(patterns))
    [f] = [k for k, v in counts.items() if v == 9]
    return f


def segment_g(patterns: list[str]) -> str:
    four = get_four(patterns)
    a = segment_a(patterns)
    four_a = set(four + a)
    nine = get_nine(patterns)
    return (set(nine) - four_a).pop()


def four_eight(patterns: list[str]):
    [four] = [p for p in patterns if len(p) == 4]
    [eight] = [p for p in patterns if len(p) == 7]
    return (four, eight)


def get_rules(patterns: list[str]) -> dict[str, int]:
    a = segment_a(patterns)
    b = segment_b(patterns)
    c = segment_c(patterns)
    d = segment_d(patterns)
    e = segment_e(patterns)
    f = segment_f(patterns)
    g = segment_g(patterns)

    rules: dict[str, int] = {
        "".join(sorted([a, b, c, e, f, g])): 0,
        "".join(sorted([c, f])): 1,
        "".join(sorted([a, c, d, e, g])): 2,
        "".join(sorted([a, c, d, f, g])): 3,
        "".join(sorted([b, c, d, f])): 4,
        "".join(sorted([a, b, d, f, g])): 5,
        "".join(sorted([a, b, d, e, f, g])): 6,
        "".join(sorted([a, c, f])): 7,
        "".join(sorted([a, b, c, d, e, f, g])): 8,
        "".join(sorted([a, b, c, d, f, g])): 9,
    }

    return rules


def part1(input: list[Entry]) -> int:
    result = 0
    targets = set([1, 4, 7, 8])

    for entry in input:
        rules = get_rules(entry.patterns)
        numbers = [rules["".join(sorted(output))] for output in entry.outputs]
        hits = [n for n in numbers if n in targets]
        result += len(hits)

    return result


def part2(input: list[Entry]) -> int:
    result = 0

    for entry in input:
        rules = get_rules(entry.patterns)
        result += int(
            "".join(
                [
                    str(n)
                    for n in [
                        rules["".join(sorted(output))] for output in entry.outputs
                    ]
                ]
            )
        )

    return result


def parse(*, example: bool = False) -> list[Entry]:
    lines = read_input_lines(8, str, example=example)
    entries: list[Entry] = []
    for line in lines:
        [patterns, outputs] = line.strip().split(" | ")
        entries.append(
            Entry(
                patterns=[p.strip() for p in patterns.split()],
                outputs=[p.strip() for p in outputs.split()],
            )
        )
    return entries


if __name__ == "__main__":
    data_in = parse()
    print(part1(data_in))
    print(part2(data_in))
