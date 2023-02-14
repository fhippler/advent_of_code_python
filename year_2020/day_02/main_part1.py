#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None
    result = 0

    for a in inp:
        b = a.split()
        c = b[0].split("-")
        counter = 0
        for i in range(len(b[2])):
            if b[2][i] == b[1][0]:
                counter += 1
        if counter >= int(c[0]) and counter <= int(c[1]):
            result += 1
    return result


ut.aoc_check(main, __file__, [], True)
