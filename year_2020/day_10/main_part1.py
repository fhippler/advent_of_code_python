#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None
    a = [0, 0, 0]
    inp = [int(x) for x in inp if x != ""]
    inp.sort()
    inp = [0] + inp + [inp[-1] + 3]
    for b in range(1, len(inp)):
        a[inp[b] - inp[b - 1] - 1] += 1

    return a[0] * a[2]


ut.aoc_check(main, __file__, [])
