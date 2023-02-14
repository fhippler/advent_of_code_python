#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    cycle = 0
    register_x = 1
    result_ind = {0: "", 40: "", 80: "", 120: "", 160: "", 200: "", 240: ""}
    for b in inp:
        temp = b.split(" ")
        if temp[0] == "addx":
            for _ in range(2):
                result_ind[cycle - ((cycle) % 40)] += (
                    "#" if register_x - 1 <= (cycle % 40) <= register_x + 1 else "."
                )
                cycle += 1
            register_x += int(temp[1])
        elif temp[0] == "noop":
            for _ in range(1):
                result_ind[cycle - ((cycle) % 40)] += (
                    "#" if register_x - 1 <= (cycle % 40) <= register_x + 1 else "."
                )
                cycle += 1

    for b in result_ind.values():
        print(b)

    # result has to be read visually
    return None


ut.aoc_check(main, __file__, [])
