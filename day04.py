from common import read_input, transpose


class Board:
    lines: list[list[int]]
    numbers: dict[int, bool]

    def __init__(self, board: str):
        numbers = _parse_board(board)
        self.lines = []
        self.numbers = {}

        for row in numbers:
            for n in row:
                self.numbers[n] = False
            self.lines.append(row)

        for col in transpose(numbers):
            self.lines.append(list(col))

    def play(self, number: int) -> "Board":
        if number in self.numbers:
            self.numbers[number] = True
        return self

    def has_bingo(self) -> bool:
        for line in self.lines:
            if all([self.numbers[cell] for cell in line]):
                return True
        return False

    def unmarked(self) -> list[int]:
        return [n for n, hit in self.numbers.items() if not hit]


def _parse_board(input: str) -> list[list[int]]:
    rows = [v.strip() for v in input.strip().split("\n")]
    numbers = [[int(n) for n in row.split()] for row in rows]
    return numbers


def _play(numbers: list[int], boards: list[Board]) -> list[tuple[list[int], Board]]:
    drawn: list[int] = []
    results: list[tuple[list[int], Board]] = []
    for n in numbers:
        drawn.append(n)
        for b in boards:
            if b.has_bingo():
                continue
            b.play(n)
            if b.has_bingo():
                results.append((drawn.copy(), b))
    return results


def part1(input: str) -> int:
    parts = input.split("\n\n")
    drawn_numbers = [int(v.strip()) for v in parts[0].split(",")]
    boards = [Board(v) for v in parts[1:]]
    results = _play(drawn_numbers, boards)
    drawn, winning_board = results[0]
    drawn_last = drawn[-1]
    return drawn_last * sum(winning_board.unmarked())


def part2(input: str) -> int:
    parts = input.split("\n\n")
    drawn_numbers = [int(v.strip()) for v in parts[0].split(",")]
    boards = [Board(v) for v in parts[1:]]
    results = _play(drawn_numbers, boards)
    drawn, losing_board = results[-1]
    drawn_last = drawn[-1]
    return drawn_last * sum(losing_board.unmarked())


if __name__ == "__main__":
    data_in = read_input(4)
    print(part1(data_in))
    print(part2(data_in))
