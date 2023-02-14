#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def find_common_item(x):
    a = int(len(x) / 2)
    b = x[:a]
    c = x[a:]
    for m in b:
        for n in c:
            if m == n:
                return m


def get_counters(x):
    a = {}
    for m in x:
        if m in a:
            a[m] += 1
        else:
            a[m] = 1
    return a


def new_ord(x):
    o = ord(x)
    if o < 95:
        return o - 38  # 64+26
    else:
        return o - 96


def main(inp):
    if inp == [""]:
        return None

    l = [x for x in inp]

    result = []
    f = ut.slice_list(inp, [3])
    for x in f:
        if x == [""]:
            continue
        temp = []
        for y in x:
            temp.append(get_counters(y))

        for z in temp[0]:
            if z in temp[1] and z in temp[2]:
                result.append(z)

    result = [new_ord(x) for x in result]
    return sum(result)


ut.aoc_check(main, __file__, [])
