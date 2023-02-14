#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

import copy

__version__ = "1.0.0"


def func(b):
    acc = 0
    programcounter = 0
    while True:
        if b[programcounter] == "-1":
            return -1
        if b[programcounter] == "eof":
            return acc
        line = b[programcounter].split(" ")
        b[programcounter] = "-1"
        if line[0] == "nop":
            programcounter += 1
        elif line[0] == "acc":
            acc += int(line[1])
            programcounter += 1
        elif line[0] == "jmp":
            programcounter += int(line[1])


def main(inp):
    if inp == [""]:
        return None
    a = []
    for c in range(len(inp)):
        line = inp[c].split(" ")
        if line[0] == "acc":
            continue
        d = copy.deepcopy(inp)
        if line[0] == "jmp":
            d[c] = "nop " + line[1]
        if line[0] == "nop":
            d = inp.copy()
            d[c] = "jmp " + line[1]
        d.append("eof")
        a.append(d)

    result = 0

    for c in a:
        val = func(c)
        if val != -1:
            result = val
    return result


ut.aoc_check(main, __file__, [], True)
