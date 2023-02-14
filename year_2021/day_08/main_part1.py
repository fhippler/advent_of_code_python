#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    result = {x: 0 for x in range(0, 10)}

    # 1: 2 cf
    # 4: 4 acf
    # 7: 3
    # 8: 7

    m = []
    for a in inp:
        m.append(a.split(" | "))
    n = []
    for a in m:
        n.append([a[0].split(" "), a[1].split(" ")])

    for entry in n:
        right_side = entry[1]
        for a in right_side:
            if len(a) == 2:
                result[1] += 1
            elif len(a) == 3:
                result[7] += 1
            elif len(a) == 4:
                result[4] += 1
            elif len(a) == 7:
                result[8] += 1

    final = result[1] + result[4] + result[7] + result[8]

    return final


ut.aoc_check(main, __file__, [], True)
