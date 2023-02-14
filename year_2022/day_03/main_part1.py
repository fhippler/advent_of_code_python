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
    for x in inp:
        if x == "":
            continue
        result.append(find_common_item(x))

    result = [new_ord(x) for x in result]
    # result = [new_ord(x) for x in ['a', 'A', 'z', 'Z']]

    return sum(result)


ut.aoc_check(main, __file__, [])
