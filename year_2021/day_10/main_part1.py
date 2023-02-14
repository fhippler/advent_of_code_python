#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    result = 0

    a = [[b, []] for b in inp]
    d = {")": "(", "]": "[", "}": "{", ">": "<"}
    res = []

    for b in a:
        for c in b[0]:
            if c in d.values():
                b[1].append(c)
            elif b[1] and b[1][-1] == d[c]:
                b[1].pop()
            else:
                res.append([c, d[c]])
                break

    for a in res:
        if a[0] == ")":
            result += 3
        elif a[0] == "]":
            result += 57
        elif a[0] == "}":
            result += 1197
        elif a[0] == ">":
            result += 25137

    return result


ut.aoc_check(main, __file__, [])
