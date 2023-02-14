#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    inp = [int(x) for x in inp]

    counter = 0
    last_depth = inp[0] + inp[1] + inp[2]

    for i in range(len(inp) - 2):
        current_depth = inp[i] + inp[i + 1] + inp[i + 2]
        if current_depth > last_depth:
            counter += 1
        last_depth = current_depth
    return counter


ut.aoc_check(main, __file__, [], True)
