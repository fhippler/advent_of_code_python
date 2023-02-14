#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    forward_counter = 0
    depth_counter = 0
    aim = 0

    for e in inp:
        direction = e.split()[0]
        distance = int(e.split()[1])
        if direction == "forward":
            forward_counter += distance
            depth_counter += aim * distance
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance

    # print("Forward: " + str(forward_counter))
    # print("Depth: " + str(depth_counter))
    # print("Aim: " + str(aim))
    # print("Total: " + str(forward_counter * depth_counter))
    return forward_counter * depth_counter


ut.aoc_check(main, __file__, [], True)
