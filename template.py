#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    print(inp)
    if inp == [""]:
        return None

    return None


ut.aoc_check(main, __file__, [])
