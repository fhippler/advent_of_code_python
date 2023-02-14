#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None
    acc = 0
    programcounter = 0
    while True:
        if inp[programcounter] == "-1":
            break
        line = inp[programcounter].split(" ")
        if line[0] == "acc":
            acc += int(line[1])
            inp[programcounter] = "-1"
            programcounter += 1
        if line[0] == "jmp":
            inp[programcounter] = "-1"
            programcounter += int(line[1])
        if line[0] == "nop":
            programcounter += 1
    return acc


ut.aoc_check(main, __file__, [])
