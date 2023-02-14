#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    b = inp[0].split()
    b = b[0].split(",")

    counter = 0

    while counter < 80:
        for i in range(len(b)):
            b[i] = str(int(b[i]) - 1)
            if b[i] == "-1":
                b[i] = "6"
                b.append("8")
        counter += 1

    return len(b)


ut.aoc_check(main, __file__, [])
