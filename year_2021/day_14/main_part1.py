#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    start = inp[0]
    d = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in inp[1:]}

    for i in range(10):
        list_of_pairs = []
        x = 0
        while x < len(start) - 1:
            list_of_pairs.append(start[x : x + 2])
            x += 1
        newstart = ""
        for p in list_of_pairs:
            newstart += p[0] + d[p]
        start = newstart + start[-1]

    r = {x: start.count(x) for x in start}
    s = {start.count(x) for x in start}

    return max(s) - min(s)


ut.aoc_check(main, __file__, [], True)
