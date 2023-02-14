#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    inp = inp[0].split(",")

    differences = []
    min = 100000000000000000000
    ind = -1

    for i in range(1500):
        # print("Round: " + str(i))
        diff = 0
        for a in inp:
            diff += abs(int(a) - i)
            # print(abs(int(a) - i))
        if diff < min:
            min = diff
            ind = i
        differences.append(diff)

    return min


ut.aoc_check(main, __file__, [])
