#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None
    result = -1
    for a in range(len(inp)):
        for b in range(len(inp)):
            for c in range(len(inp)):
                n1 = int(inp[a])
                n2 = int(inp[b])
                n3 = int(inp[c])
                if (n1 + n2 + n3) == 2020:
                    result = n1 * n2 * n3
                    break
            if result != -1:
                break
        if result != -1:
            break
    return result


ut.aoc_check(main, __file__, [], True)
