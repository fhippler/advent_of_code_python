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
    d = {inp[i]: [-1, i] for i in range(len(inp))}
    last_number = inp[-1]
    iterations = 30000000
    for i in range(len(inp), iterations):
        if d[last_number][0] > -1:
            num = d[last_number][1] - d[last_number][0]
        else:
            num = 0
        if num in d:
            d[num] = [d[num][1], i]
        else:
            d[num] = [-1, i]
        last_number = num
    return last_number


ut.aoc_check(main, __file__, [], True)
