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
    d_loose = {"A": "Z", "B": "X", "C": "Y"}
    d_draw = {"A": "X", "B": "Y", "C": "Z"}
    d_win = {"A": "Y", "B": "Z", "C": "X"}

    values = {"X": 1, "Y": 2, "Z": 3}

    # x loose
    # y draw
    # z win
    for x in inp:
        a, b = x[0], x[2]
        if b == "X":
            c = d_loose[a]
            result += 0 + values[c]
        elif b == "Y":
            c = d_draw[a]
            result += 3 + values[c]
        elif b == "Z":
            c = d_win[a]
            result += 6 + values[c]

    return result


ut.aoc_check(main, __file__, [])
