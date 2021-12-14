import re
from collections import Counter

from common import read_input_lines

Input = tuple[str, dict[str, str]]
insertion_rule_regex = re.compile(r"([A-Z][A-Z]) -> ([A-Z])$")


def _step(input: Input) -> str:
    template, insertion_rules = input
    output: list[str] = []

    pairs = zip(template, template[1:])

    for a, b in pairs:
        output.append(a)
        output.append(insertion_rules[a + b])
    output.append(b)

    return "".join(output)


def part1(input: Input) -> int:
    template, insertion_rules = input
    for _ in range(10):
        template = _step((template, insertion_rules))

    counts = sorted(Counter(template).values())

    least_common = counts[0]
    most_common = counts[-1]
    return most_common - least_common


def part2(input: Input) -> int:
    return 0


def parse(*, example: bool = False) -> Input:
    lines = read_input_lines(14, str, example=example)
    polymer_template = lines[0]
    insertion_rules: dict[str, str] = {}

    for line in lines[2:]:
        m = re.match(insertion_rule_regex, line)
        if m:
            pair = m.groups()[0]
            element = m.groups()[1]
            insertion_rules[pair] = element

    return polymer_template, insertion_rules


if __name__ == "__main__":
    data_in = parse()
    print(part1(data_in))
    print(part2(data_in))
