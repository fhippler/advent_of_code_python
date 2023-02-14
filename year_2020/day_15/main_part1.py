#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def find_last(spoken, last_number):
    s = spoken.copy()[::-1]
    index = s.index(last_number)
    val = len(spoken) - 1 - index
    return val


def main(inp):
    if inp == [""]:
        return None

    inp = [int(x) for x in inp[0].split(",")]
    spoken = inp.copy()
    last_number = spoken[-1]
    for i in range(len(inp), 2020):
        last_number = spoken[-1]
        if spoken.count(last_number) <= 1:
            spoken.append(0)
        else:
            spoken.append(i - 1 - find_last(spoken[:-1], last_number))
    return spoken[-1]


ut.aoc_check(main, __file__, [])
