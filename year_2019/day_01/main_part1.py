#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

import math

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None
    l = [math.floor(int(x) / 3) - 2 for x in inp if x != ""]
    return sum(l)


ut.aoc_check(main, __file__, [0])
