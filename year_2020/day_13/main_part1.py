#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    busID = -1
    mini = float("inf")
    for b in inp[1].split(","):
        if b == "x":
            continue
        temp = 0
        while True:
            temp += int(b)
            if temp > int(inp[0]):
                break
        if temp < mini:
            mini = temp
            busID = int(b)

    return (mini - int(inp[0])) * busID


ut.aoc_check(main, __file__, [])
