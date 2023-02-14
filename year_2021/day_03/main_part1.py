#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    gamma_rate, epsilon_rate = "", ""

    for pos in range(len(inp[0])):
        zeros, ones = 0, 0
        for n in inp:
            if n[pos] == "0":
                zeros += 1
            elif n[pos] == "1":
                ones += 1

        gamma_rate += "0" if zeros > ones else "1"
        epsilon_rate += "1" if zeros > ones else "0"

    return ut.toDeci(2, gamma_rate) * ut.toDeci(2, epsilon_rate)


ut.aoc_check(main, __file__, [], True)
