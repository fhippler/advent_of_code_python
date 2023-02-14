#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    b = inp[0].split(",")

    #    0  1  2  3  4  5  6  7  8
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(b)):
        a[int(b[i])] += 1

    for i in range(256):
        temp = a[0]
        for i in range(len(a) - 1):
            a[i] = a[i + 1]
        a[6] += temp
        a[8] = temp

    result = 0
    for n in a:
        result += n

    return result


ut.aoc_check(main, __file__, [])
