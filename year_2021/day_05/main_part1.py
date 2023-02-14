#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    field = [[0 for x in range(1000)] for y in range(1000)]
    # print(field)

    for line in inp:
        first = line.split()[0].split(",")
        second = line.split()[2].split(",")
        val1 = -1
        val2 = -1
        val3 = -1
        val4 = -1
        if int(first[0]) < int(second[0]):
            val1 = int(first[0])
            val2 = int(second[0])
        else:
            val1 = int(second[0])
            val2 = int(first[0])
        if int(first[1]) < int(second[1]):
            val3 = int(first[1])
            val4 = int(second[1])
        else:
            val3 = int(second[1])
            val4 = int(first[1])

        range_first = [*range(int(val1), int(val2) + 1)]
        range_second = [*range(int(val3), int(val4) + 1)]

        if len(range_first) > 1 and len(range_second) > 1:
            continue

        for a in range_first:
            for b in range_second:
                field[b][a] += 1

    result = 0

    for x in field:
        for y in x:
            if y > 1:
                result += 1

    return result


ut.aoc_check(main, __file__, [], True)
