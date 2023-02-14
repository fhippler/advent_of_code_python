#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    newl = []
    temp = []
    for x in inp:
        if x != "":
            temp.append(int(x))
        else:
            newl.append(temp)
            temp = []

    res = sorted([sum(x) for x in newl])
    return sum(res[-3:])


ut.aoc_check(main, __file__, [])
