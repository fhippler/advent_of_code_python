#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

import re

__version__ = "1.0.0"

d = {}
paths = []
result = 0


def find_path(prev):
    # print(prev)
    curr = prev[-1]
    if curr == "end":
        paths.append(",".join(prev))
        return
    for n in d[curr]:
        if n == "start":
            continue
        # elif n in prev and len(re.findall("[a-z]+", n)) > 0:
        #     continue
        else:
            prev.append(n)
            dupl = [prev.count(m) for m in d.keys() if len(re.findall("[a-z]+", m)) > 0]
            if dupl.count(2) > 1 or 3 in dupl or 4 in dupl:
                prev.pop()
                continue
            find_path(prev)
            prev.pop()


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
