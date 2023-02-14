#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    oxygen_list = inp.copy()
    co2_list = inp.copy()

    counter = 0
    while len(oxygen_list) > 1:
        zeros, ones = 0, 0
        for e in oxygen_list:
            if e[counter] == "0":
                zeros += 1
            else:
                ones += 1
        bit = "0" if zeros > ones else "1"
        oxygen_list = [
            s for s in oxygen_list if s[counter] == bit or len(oxygen_list) == 1
        ]
        counter += 1

    counter = 0
    while len(co2_list) > 1:
        zeros, ones = 0, 0
        for e in co2_list:
            if e[counter] == "0":
                zeros += 1
            else:
                ones += 1
        bit = "1" if ones < zeros else "0"
        co2_list = [s for s in co2_list if s[counter] == bit or len(co2_list) == 1]
        counter += 1

    # print("Oxygen generator rating: " + oxygen_list[0])
    # print("CO2 scrubber rating: " + co2_list[0])
    return ut.toDeci(2, oxygen_list[0]) * ut.toDeci(2, co2_list[0])


ut.aoc_check(main, __file__, [], True)
