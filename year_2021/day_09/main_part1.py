#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    result = 0

    for a in range(len(inp)):
        c = []
        for b in range(len(inp[a])):
            elem0 = int(inp[a][b])
            elem1 = 10
            elem2 = 10
            elem3 = 10
            elem4 = 10
            if a - 1 >= 0:
                elem1 = int(inp[a - 1][b])  # above
            if b - 1 >= 0:
                elem2 = int(inp[a][b - 1])  # left
            if b + 1 < len(inp[a]):
                elem3 = int(inp[a][b + 1])  # right
            if a + 1 < len(inp):
                elem4 = int(inp[a + 1][b])  # down
            if elem0 < elem1 and elem0 < elem2 and elem0 < elem3 and elem0 < elem4:
                result += 1 + elem0
                c.append([elem0, elem1, elem2, elem3, elem4])

    return result


ut.aoc_check(main, __file__, [], True)
