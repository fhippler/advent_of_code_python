#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

import re
import copy

__version__ = "1.0.0"

d = {}
paths = []
result = 0


def find_path(prev):
    curr = prev[-1]
    for n in d[curr]:
        if n == "end":
            prev.append(n)
            if not prev in paths:
                paths.append(prev)
        elif n in prev and len(re.findall("[a-z]+", n)) > 0:
            continue
        else:
            c = copy.deepcopy(prev)
            c.append(n)
            find_path(c)


def main(inp):
    if inp == [""]:
        return None

    for b in inp:
        c = b.split("-")
        if c[0] in d:
            d[c[0]].append(c[1])
        else:
            d[c[0]] = [c[1]]
        if c[1] in d:
            d[c[1]].append(c[0])
        else:
            d[c[1]] = [c[0]]

    find_path(["start"])
    return len(paths)


ut.aoc_check(main, __file__, [], True)
