#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    north = 0
    east = 0
    w_north = 1
    w_east = 10
    for b in inp:
        if b[0] == "F":
            north += int(b[1:]) * w_north
            east += int(b[1:]) * w_east
        elif b[0] == "N":
            w_north += int(b[1:])
        elif b[0] == "S":
            w_north -= int(b[1:])
        elif b[0] == "E":
            w_east += int(b[1:])
        elif b[0] == "W":
            w_east -= int(b[1:])
        else:
            val = -1
            if b[0] == "L":
                val = 4 - int(int(b[1:]) / 90) % 4
            elif b[0] == "R":
                val = int(int(b[1:]) / 90)
            for i in range(val):
                w_north, w_east = -w_east, w_north

    return abs(north) + abs(east)


ut.aoc_check(main, __file__, [], True)
