#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def is_sum(inp, i, pre):
    for a in range(pre):
        for b in range(pre):
            if int(inp[i - a - 1]) + int(inp[i - b - 1]) == int(inp[i]):
                return True


def main(inp):
    if inp == [""]:
        return None

    pre = 25
    for i in range(pre, len(inp)):
        if is_sum(inp, i, pre):
            continue
        else:
            return int(inp[i])


ut.aoc_check(main, __file__, [], True)
