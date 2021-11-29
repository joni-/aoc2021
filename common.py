import os
import sys


def read_input(day: int) -> str:
    input_file = "day" + str(day).zfill(2) + ".in"
    path = (
        sys.argv[1]
        if len(sys.argv) > 1
        else os.path.join(os.path.dirname(__file__), "inputs", input_file)
    )
    return open(path, "r").read()
