#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    inp = inp[0]
    for i in range(len(inp)):
        if (
            inp[i] != inp[i + 1]
            and inp[i] != inp[i + 2]
            and inp[i] != inp[i + 3]
            and inp[i + 1] != inp[i + 2]
            and inp[i + 1] != inp[i + 3]
            and inp[i + 2] != inp[i + 3]
        ):
            return i + 4

    return 0


ut.aoc_check(main, __file__, [])
