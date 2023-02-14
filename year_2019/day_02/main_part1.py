#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return 0
    a = [int(x) for x in inp[0].split(",") if x != ""]
    position = 0
    a[1] = 12
    a[2] = 2
    while a[position] != 99:
        if a[position] == 1:
            a[a[position + 3]] = a[a[position + 1]] + a[a[position + 2]]
        elif a[position] == 2:
            a[a[position + 3]] = a[a[position + 1]] * a[a[position + 2]]
        position += 4

    return a[0]


ut.aoc_check(main, __file__, [])
