#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

import copy

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    start = inp[0]
    d = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in inp[1:]}
    pair_counter = {x: 0 for x in d}

    # init the first number of pairs
    z = 0
    while z < len(start) - 1:
        pair_counter[start[z : z + 2]] += 1
        z += 1

    # replace previous pair with the two new pairs
    for i in range(40):
        pc_copy = copy.deepcopy(pair_counter)
        for x, y in pc_copy.items():
            pair_counter[x[0] + d[x]] += y
            pair_counter[d[x] + x[1]] += y
            pair_counter[x[0] + x[1]] -= y

    # counting chars
    r = {}
    for x, y in pair_counter.items():
        if x[0] in r:
            r[x[0]] += y
        else:
            r[x[0]] = y
        if x[1] in r:
            r[x[1]] += y
        else:
            r[x[1]] = y

    # correcting counts as every [except first and last] char is counted twice
    r[start[0]] += 1
    r[start[-1]] += 1
    s = {int(y / 2) for x, y in r.items()}
    return max(s) - min(s)


ut.aoc_check(main, __file__, [], True)
