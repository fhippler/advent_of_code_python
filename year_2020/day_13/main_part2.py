#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None
    temp = inp[1].split(",")

    mods = {int(temp[b]): -b % int(temp[b]) for b in range(len(temp)) if temp[b] != "x"}

    vals = list(reversed(sorted(mods)))
    val = mods[vals[0]]
    r = vals[0]
    for b in vals[1:]:
        while val % b != mods[b]:
            val += r
        r *= b

    return val


ut.aoc_check(main, __file__, [])
