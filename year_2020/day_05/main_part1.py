#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None
    result = 0

    for a in inp:
        low = 0
        middle = 0
        up = 127
        for i in range(7):
            middle = low + int((up - low) / 2)
            if a[i] == "F":
                up = middle
            else:
                low = middle + 1
        row = low
        low = 0
        up = 7
        for i in range(7, 10):
            middle = low + int((up - low) / 2)
            if a[i] == "R":
                low = middle + 1
            else:
                up = middle
        column = low
        seatId = row * 8 + column
        if seatId > result:
            result = seatId
    return result


ut.aoc_check(main, __file__, [], True)
