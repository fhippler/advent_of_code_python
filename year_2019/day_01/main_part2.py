#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

import math

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None
    result = 0
    for x in [int(y) for y in inp if y != ""]:
        total = 0
        new_fuel = x
        while new_fuel > 0:
            new_fuel = max(0, math.floor(new_fuel / 3) - 2)
            total += new_fuel
        result += total
    return result


ut.aoc_check(main, __file__, [1])
