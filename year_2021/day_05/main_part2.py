#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    field = [[0 for x in range(1000)] for y in range(1000)]

    for line in inp:
        first = line.split()[0].split(",")
        second = line.split()[2].split(",")

        counter1 = int(first[0])
        counter2 = int(first[1])
        while True:
            field[counter2][counter1] += 1
            if int(first[0]) < int(second[0]):
                counter1 += 1
            elif int(first[0]) > int(second[0]):
                counter1 -= 1
            if int(first[1]) < int(second[1]):
                counter2 += 1
            elif int(first[1]) > int(second[1]):
                counter2 -= 1
            if counter1 == int(second[0]) and counter2 == int(second[1]):
                field[counter2][counter1] += 1
                break
        continue

    result = 0

    for x in field:
        for y in x:
            if y > 1:
                result += 1

    return result


ut.aoc_check(main, __file__, [], True)
