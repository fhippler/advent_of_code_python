#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    inp = inp[0].split(",")
    inp.sort()

    differences = []
    min = 100000000000000000000
    ind = -1

    def tri(n):
        return int((n * (n + 1)) / 2)

    for i in range(800):
        diff = 0
        for a in inp:
            temp = abs(int(a) - i)
            diff += tri(temp)
        if diff < min:
            min = diff
            ind = i
        differences.append(diff)

    return min


ut.aoc_check(main, __file__, [])
