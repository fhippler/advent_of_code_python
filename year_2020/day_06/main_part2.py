#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

import string

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None
    a = []
    last = 0
    base_list = [[s, 0] for s in string.ascii_lowercase]
    for i in range(len(inp)):
        if inp[i] == "":
            a.append([e.copy() for e in base_list])
            for k in range(last, i):
                current_line = inp[k]
                a[-1].append([i - last, 0])
                for c in current_line:
                    for b in range(len(a[-1]) - 1):
                        if a[-1][b][0] == c:
                            a[-1][b][1] += 1
            last = i + 1

    result = 0

    for b in a:
        for c in range(len(b) - 1):
            if b[c][1] == b[-1][0]:
                result += 1
    return result


ut.aoc_check(main, __file__, [])
