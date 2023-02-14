#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None
    # List of passports
    a = []
    b = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    result = 0
    last_start = 0
    for l in range(len(inp)):
        if inp[l] == "":
            a.append([])
            for number in range(last_start, l):
                content = inp[number].split()
                for c in content:
                    a[len(a) - 1].append(c)
            last_start = l

    for passport in a:
        valid = True
        for p in b:
            found = False
            for pair in passport:
                o = pair[0:3]
                if o == p:
                    found = True
                    break
            if found == False:
                valid = False

        if valid == True:
            result += 1
    return result


ut.aoc_check(main, __file__, [])
