from common import read_input_lines


def _is_corrupted(line: str) -> tuple[bool, str]:
    stack: list[str] = []
    counterparts = {"[": "]", "(": ")", "{": "}", "<": ">"}
    reversed_counterparts = {v: k for k, v in counterparts.items()}

    for c in line:
        if c in counterparts.keys():
            stack.append(c)
        if c in counterparts.values():
            expected = stack.pop()
            if expected != reversed_counterparts[c]:
                return (True, c)

    return (False, "")


def _complete(line: str) -> str:
    stack: list[str] = []
    counterparts = {"[": "]", "(": ")", "{": "}", "<": ">"}
    reversed_counterparts = {v: k for k, v in counterparts.items()}

    for c in line:
        if c in counterparts.keys():
            stack.append(c)
        if c in counterparts.values():
            expected = stack.pop()
            if expected != reversed_counterparts[c]:
                raise ValueError("Not incomplete line" + line)

    while stack:
        missing = stack.pop()
        counterpart = counterparts[missing]
        line += counterpart

    return line


def part1(input: list[str]) -> int:
    scores: list[int] = []
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}

    for line in input:
        corrupted, illegal_char = _is_corrupted(line)
        if corrupted:
            scores.append(points[illegal_char])

    return sum(scores)


def part2(input: list[str]) -> int:
    incomplete: list[str] = []
    points = {")": 1, "]": 2, "}": 3, ">": 4}
    scores: list[int] = []

    for line in input:
        corrupted, _ = _is_corrupted(line)
        if not corrupted:
            incomplete.append(line)

    for line in incomplete:
        score = 0
        new_line = _complete(line)
        diff = new_line[len(line) :]
        for c in diff:
            score = score * 5 + points[c]
        scores.append(score)

    mid = int(len(scores) / 2)
    return sorted(scores)[mid]


def parse(*, example: bool = False) -> list[str]:
    return read_input_lines(10, str, example=example)


if __name__ == "__main__":
    data_in = parse()
    print(part1(data_in))
    print(part2(data_in))
