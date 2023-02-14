#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None
    a = [[1, 1, 0], [3, 1, 0], [5, 1, 0], [7, 1, 0], [1, 2, 0]]

    result = 1

    for b in a:
        xPos, yPos = 0, 0
        while yPos + 1 < len(inp):
            xPos = (xPos + b[0]) % len(inp[yPos])
            yPos = yPos + b[1]
            if inp[yPos][xPos] == "#":
                b[2] += 1
        result *= b[2]

    return result


ut.aoc_check(main, __file__, [0], True)
