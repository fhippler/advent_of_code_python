#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    cycle = 1
    register_x = 1
    result_ind = {20: None, 60: None, 100: None, 140: None, 180: None, 220: None}
    for b in inp:
        temp = b.split(" ")
        if temp[0] == "addx":
            for _ in range(2):
                if cycle in result_ind.keys():
                    result_ind[cycle] = register_x
                    print("#####", cycle, ":", register_x)
                cycle += 1
            register_x += int(temp[1])
            # cycle += 2
        elif temp[0] == "noop":
            for _ in range(1):
                if cycle in result_ind.keys():
                    result_ind[cycle] = register_x
                    print("#####", cycle, ":", register_x)
                cycle += 1
    result = 0
    for a, b in result_ind.items():
        result += a * b
    print(result_ind)
    return result


ut.aoc_check(main, __file__, [])
