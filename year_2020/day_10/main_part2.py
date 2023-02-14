#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None
    inp = [int(x) for x in inp if x != ""]
    inp.sort()
    inp = [0] + inp + [inp[-1] + 3]

    d = {key: 0 for key in inp}

    d[0] = 1
    for key, val in d.items():
        if (key + 1) in d:
            d[key + 1] += d[key]
        if (key + 2) in d:
            d[key + 2] += d[key]
        if (key + 3) in d:
            d[key + 3] += d[key]

    return d[inp[-1]]


ut.aoc_check(main, __file__, [])
