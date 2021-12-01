from common import read_input


def part1(input: str) -> int:
    ns = [int(n) for n in input.splitlines()]
    pairs = zip(ns, ns[1:])

    increments = 0
    for a, b in pairs:
        if a < b:
            increments += 1

    return increments


def part2(input: str) -> int:
    ns = [int(n) for n in input.splitlines()]
    chunks = []

    for i in range(len(ns)):
        chunks.append(sum(ns[i : i + 3]))

    pairs = zip(chunks, chunks[1:])

    increments = 0
    for a, b in pairs:
        if a < b:
            increments += 1

    return increments


if __name__ == "__main__":
    data_in = read_input(1)
    print(part1(data_in))
    print(part2(data_in))
