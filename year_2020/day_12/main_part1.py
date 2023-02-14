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
    direction = ["east", "south", "west", "north"]
    for b in inp:
        if b[0] == "N":
            north += int(b[1:])
        if b[0] == "S":
            north -= int(b[1:])
        if b[0] == "E":
            east += int(b[1:])
        if b[0] == "W":
            east -= int(b[1:])
        if b[0] == "L":
            val = int(int(b[1:]) / 90)
            for i in range(val):
                direction = direction[-1:] + direction[:-1]
        if b[0] == "R":
            val = int(int(b[1:]) / 90)
            for i in range(val):
                direction = direction[1:] + direction[:1]
        if b[0] == "F":
            if direction[0] == "east":
                east += int(b[1:])
            if direction[0] == "west":
                east -= int(b[1:])
            if direction[0] == "north":
                north += int(b[1:])
            if direction[0] == "south":
                north -= int(b[1:])

    return abs(north) + abs(east)


ut.aoc_check(main, __file__, [])
