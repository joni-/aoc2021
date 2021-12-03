import os
import sys
from collections.abc import Iterator
from typing import Callable, TypeVar, Union

T = TypeVar("T")


def count_by(
    pred: Callable[[Union[T, str]], bool]
) -> Callable[[Union[Iterator[T], str]], int]:
    def counter(seq: Union[Iterator[T], str]) -> int:
        count = 0
        for x in seq:
            if pred(x):
                count += 1
        return count

    return counter


def read_input(day: int) -> str:
    input_file = "day" + str(day).zfill(2) + ".in"
    path = (
        sys.argv[1]
        if len(sys.argv) > 1
        else os.path.join(os.path.dirname(__file__), "inputs", input_file)
    )
    return open(path, "r").read()


def read_input_lines(day: int, mapper: Callable[[str], T]) -> list[T]:
    return [mapper(x) for x in read_input(day).splitlines()]
