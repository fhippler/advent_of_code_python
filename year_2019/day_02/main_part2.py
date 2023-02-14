#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def calc(a, noun, verb):
    counter = 0
    position = 0
    a[1] = noun
    a[2] = verb
    while a[position] != 99 or counter > 1000:
        if a[position] == 1:
            a[a[position + 3]] = a[a[position + 1]] + a[a[position + 2]]
        elif a[position] == 2:
            a[a[position + 3]] = a[a[position + 1]] * a[a[position + 2]]
        position += 4
        counter += 1
    return a[0]


def main(inp):
    if inp == [""]:
        return 0
    a = [int(x) for x in inp[0].split(",") if x != ""]

    for i in range(100):
        for j in range(100):
            if calc(a.copy(), i, j) == 19690720:
                return 100 * i + j

    return -1


ut.aoc_check(main, __file__, [])
