#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    basins_list = {}
    # (0,1): {(0,1),(0,2),(0,3),(1,1)}

    # coord x, coord y, dictionary key
    def check_coord(a, b, c):
        elem0 = int(inp[a][b])
        elem1, elem2, elem3, elem4 = 10, 10, 10, 10
        if a - 1 >= 0 and (c == None or not (a - 1, b) in basins_list[c]):
            elem1 = int(inp[a - 1][b])  # above
        if b - 1 >= 0 and (c == None or not (a, b - 1) in basins_list[c]):
            elem2 = int(inp[a][b - 1])  # left
        if b + 1 < len(inp[a]) and (c == None or not (a, b + 1) in basins_list[c]):
            elem3 = int(inp[a][b + 1])  # right
        if a + 1 < len(inp) and (c == None or not (a + 1, b) in basins_list[c]):
            elem4 = int(inp[a + 1][b])  # down
        if (
            elem0 < elem1
            and elem0 < elem2
            and elem0 < elem3
            and elem0 < elem4
            and elem0 < 9
        ):
            if c != None:
                if elem1 < 9:
                    basins_list[c].add((a - 1, b))
                if elem2 < 9:
                    basins_list[c].add((a, b - 1))
                if elem3 < 9:
                    basins_list[c].add((a, b + 1))
                if elem4 < 9:
                    basins_list[c].add((a + 1, b))
            else:
                basins_list[(a, b)] = set()
                basins_list[(a, b)].add((a, b))

    # Find low points and init dictionary
    for a in range(len(inp)):
        for b in range(len(inp[a])):
            check_coord(a, b, None)

    # Check all coords around low points
    for i in range(10):
        basin_copy = basins_list.copy()
        for a, b in basins_list.copy().items():
            for c in b.copy():
                check_coord(c[0], c[1], a)

    # Save sizes of basins
    result_list = []
    for a, b in basins_list.items():
        result_list.append(len(b))

    result_list.sort()
    return result_list[-1] * result_list[-2] * result_list[-3]


ut.aoc_check(main, __file__, [], True)
