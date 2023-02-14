#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def is_adjacent(a, b):
    v = abs(a[0] - b[0])
    w = abs(a[1] - b[1])
    return v, w


def main(inp):
    if inp == [""]:
        return None

    directions = {"l": (-1, 0), "r": (1, 0), "u": (0, -1), "d": (0, 1)}
    h, t = (0, 0), (0, 0)
    result_states = set()
    result_states.add(t)
    for x in inp:
        temp = x.split(" ")
        direction = temp[0].lower()
        steps = int(temp[1])
        for i in range(steps):
            old_h = h
            h = (h[0] + directions[direction][0], h[1] + directions[direction][1])
            d = is_adjacent(h, t)
            if (d[0] > 1 and d[1] == 1) or (d[0] == 1 and d[1] > 1):  # move to old h
                t = old_h
            elif d[0] > 1:  # x is different
                t = (int((h[0] + t[0]) / 2), t[1])
            elif d[1] > 1:
                t = (t[0], int((h[1] + t[1]) / 2))
            else:
                pass
            result_states.add(t)

    return len(result_states)


ut.aoc_check(main, __file__, [])
