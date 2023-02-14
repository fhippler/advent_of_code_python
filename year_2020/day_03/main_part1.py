#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None
    result = 0
    xPos, yPos = 0, 0

    while yPos + 1 < len(inp):
        xPos = (xPos + 3) % len(inp[yPos])
        yPos += 1
        if inp[yPos][xPos] == "#":
            result += 1

    return result


ut.aoc_check(main, __file__, [0], True)
