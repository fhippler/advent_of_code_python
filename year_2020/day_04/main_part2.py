#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

import re

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
                    a[len(a) - 1].append(c.rstrip())
            a[len(a) - 1].sort()
            last_start = l

    for passport in a:
        valid = True
        for p in b:
            found = False
            for pair in passport:
                if pair[0:3] == p:
                    found = True
                    # Additional value check
                    value = pair[4:]
                    if p == "byr":
                        if len(re.findall("^(19[2-9][0-9]|200[0-2])$", value)) == 0:
                            found = False
                    if p == "iyr":
                        if len(re.findall("^(201[0-9]|2020)$", value)) == 0:
                            found = False
                    if p == "eyr":
                        if len(re.findall("^(202[0-9]|2030)$", value)) == 0:
                            found = False
                    if p == "hgt":
                        if (
                            len(
                                re.findall(
                                    "^(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)$",
                                    value,
                                )
                            )
                            == 0
                        ):
                            found = False
                    if p == "hcl":
                        if len(re.findall("^(#([0-9]|[a-f]){6})$", value)) == 0:
                            found = False
                    if p == "ecl":
                        if (
                            len(re.findall("^(amb|blu|brn|gry|grn|hzl|oth)$", value))
                            == 0
                        ):
                            found = False
                    if p == "pid":
                        # if len(re.findall("^([0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9])$", value)) == 0:
                        if len(re.findall("^(\d{9})$", value)) == 0:
                            found = False
                    break
            if found == False:
                valid = False

        if valid == True:
            result += 1
            # print(passport)
    return result


ut.aoc_check(main, __file__, [])
