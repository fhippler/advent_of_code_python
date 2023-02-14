#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None
    b = []

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
            # print("I: " + str(i) + " a[i]: " + str(a[i]) + " Low: " + str(low) + " Up: " + str(up))
        row = low
        low = 0
        up = 7
        for i in range(7, 10):
            middle = low + int((up - low) / 2)
            if a[i] == "R":
                low = middle + 1
            else:
                up = middle
            # print("I: " + str(i) + " a[i]: " + str(a[i]) + " Low: " + str(low) + " Up: " + str(up))
        column = low
        seatId = row * 8 + column
        b.append(seatId)

    b.sort()
    for x in range(b[0], b[-1] + 1):
        if x not in b:
            return x


ut.aoc_check(main, __file__, [], True)
