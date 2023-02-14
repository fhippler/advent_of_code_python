#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    result = 0
    # A rock, B paper, C scissor
    # X rock 1, Y paper 2, Z scissors 3
    d = {"A": "Y", "B": "Z", "C": "X"}
    values = {"X": 1, "Y": 2, "Z": 3}
    for x in inp:
        a, b = x[0], x[2]
        if b == d[a]:
            result += 6 + values[b]
        else:
            if (
                (a == "A" and b == "X")
                or (a == "B" and b == "Y")
                or (a == "C" and b == "Z")
            ):
                result += 3 + values[b]
            else:
                result += values[b]

    return result


ut.aoc_check(main, __file__, [])
