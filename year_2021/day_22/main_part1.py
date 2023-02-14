#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    coords = []
    for b in inp:
        te = b.split(",")
        temp = []
        for t in te:
            val = t.split("=")[1].split("..")
            val1 = max(int(val[0]), -50)
            val2 = min(int(val[1]), 50)
            temp.append((val1, val2))
        coords.append(temp + [b.split(" ")[0]])

    core = set()
    for entry in coords:
        for a in range(entry[0][0], entry[0][1] + 1):
            for b in range(entry[1][0], entry[1][1] + 1):
                for c in range(entry[2][0], entry[2][1] + 1):
                    # if -50 <= a <= 50 and -50 <= b <= 50 and -50 <= c <= 50:
                    if entry[3] == "on":
                        core.add((a, b, c))
                    elif entry[3] == "off" and (a, b, c) in core:
                        core.remove((a, b, c))

    return len(core)


ut.aoc_check(main, __file__, [], True)
