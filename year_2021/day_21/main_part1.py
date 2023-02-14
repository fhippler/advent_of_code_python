#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def move(position, steps):
    result = position + steps
    while result > 10:
        result -= 10
    return result


det_roll = 1


def roll():
    global det_roll
    result = 0
    for i in range(3):
        result += det_roll
        det_roll = det_roll + 1
        while det_roll > 100:
            det_roll -= 100
    return result


def main(inp):
    if inp == [""]:
        return None

    turns = 0
    p1 = [int(inp[0].split(" ")[-1]), 0]
    p2 = [int(inp[1].split(" ")[-1]), 0]
    global det_roll
    det_roll = 1
    p1turn = True
    while True:
        curr_roll = roll()
        if p1turn:
            p1[0] = move(p1[0], curr_roll)
            p1[1] += p1[0]
        else:
            p2[0] = move(p2[0], curr_roll)
            p2[1] += p2[0]
        p1turn = not p1turn
        turns += 3
        if p1[1] >= 1000:
            return p2[1] * turns
        if p2[1] >= 1000:
            return p1[1] * turns


ut.aoc_check(main, __file__, [])
