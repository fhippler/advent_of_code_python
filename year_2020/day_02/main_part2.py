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
        b = a.split()
        c = b[0].split("-")
        counter = 0
        c1 = b[1][0] == b[2][int(c[0]) - 1]
        c2 = b[1][0] == b[2][int(c[1]) - 1]
        if (c1 or c2) and not (c1 and c2):
            result += 1
    return result


ut.aoc_check(main, __file__, [], True)
