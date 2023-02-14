#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    counter = 0

    for i in range(1, len(inp)):
        if int(inp[i]) >= int(inp[i - 1]):
            counter += 1

    return counter


ut.aoc_check(main, __file__, [0], True)
