from collections import defaultdict
from typing import Optional

from common import read_input_lines

Maze = dict[str, list[str]]


def visit(
    cave: str,
    maze: Maze,
    visit_counts: dict[str, int],
    current_path: list[str],
    paths: list[list[str]],
    allow_visit_twice: Optional[str] = None,
) -> None:
    current_path = [*current_path, cave]
    visit_counts = visit_counts.copy()
    visit_counts[cave] = visit_counts[cave] + 1

    if cave == "end":
        paths.append(current_path)

    for nb_cave in maze[cave]:
        if nb_cave.islower():
            if nb_cave != allow_visit_twice and visit_counts[nb_cave] >= 1:
                continue
            if nb_cave == allow_visit_twice and visit_counts[nb_cave] >= 2:
                continue
        visit(nb_cave, maze, visit_counts, current_path, paths, allow_visit_twice)


def part1(maze: Maze) -> int:
    found_paths: list[list[str]] = []  # note: this is mutated by visit()
    visit("start", maze, defaultdict(int), [], found_paths)
    return len(found_paths)


def part2(maze: Maze) -> int:
    found_paths: list[list[str]] = []  # note: this is mutated by visit()
    small_caves = [
        cave for cave in maze.keys() if cave.islower() and cave not in ("start", "end")
    ]

    for cave in small_caves:
        visit("start", maze, defaultdict(int), [], found_paths, cave)

    return len(set([tuple(path) for path in found_paths]))


def parse(*, example: bool = False) -> Maze:
    maze: dict[str, list[str]] = defaultdict(list)
    lines = read_input_lines(12, str, example=example)

    for line in lines:
        [start, end] = line.split("-")
        maze[start].append(end)
        maze[end].append(start)

    return maze


if __name__ == "__main__":
    data_in = parse()
    print(part1(data_in))
    print(part2(data_in))
