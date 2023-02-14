#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    result = 0
    for x in inp:
        lr = x.split(",")
        l = lr[0].split("-")
        l = (int(l[0]), int(l[1]))
        r = lr[1].split("-")
        r = (int(r[0]), int(r[1]))
        if (
            l[0] <= r[0] <= l[1]
            or l[0] <= r[1] <= l[1]
            or r[0] <= l[0] <= r[1]
            or r[0] <= l[1] <= r[1]
        ):
            result += 1
    return result


ut.aoc_check(main, __file__, [])
