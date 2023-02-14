#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

import re

__version__ = "1.0.0"


def findElem(inp, name):
    for b in inp:
        if b == "\n":
            continue
        if len(re.findall(name, re.split(" bags contain ", b)[0])) > 0:
            return b
    print("Error")


def func(inp, elem):
    b = re.split(" bags contain ", elem)[1]
    if len(re.findall("no other bag", b)) > 0:
        return 1
    else:
        res = 1
        bags = b.split(", ")
        for bag in bags:
            bagsplit = bag.split(" ")
            amount = bagsplit[0]
            name = bagsplit[1] + " " + bagsplit[2]
            res += int(amount) * func(inp, findElem(inp, name))
        return res


def main(inp):
    if inp == [""]:
        return None

    return func(inp, findElem(inp, "shiny gold")) - 1


ut.aoc_check(main, __file__, [])
