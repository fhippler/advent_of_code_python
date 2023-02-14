#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def count_chars(x):
    d = {}
    for i in x:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


def main(inp):
    if inp == [""]:
        return None

    inp = inp[0]
    n = 14
    for i in range(len(inp)):
        if all([x <= 1 for x in count_chars(inp[i : i + n]).values()]):
            return i + n

    return 1


ut.aoc_check(main, __file__, [])
