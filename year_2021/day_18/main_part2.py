#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

import json, math, copy

__version__ = "1.0.0"


def add_number(lst, number, index):
    if type(lst) is int:
        lst += number
    else:
        lst[index], _ = add_number(lst[index], number, index)
    return lst, 0


def explode(lst, depth):
    if type(lst[0]) is int and type(lst[1]) is int and depth >= 4:
        residue_left, residue_right, lst, exploded = lst[0], lst[1], 0, True
    else:
        wasLeft = wasRight = exploded = False
        residue_left = residue_right = 0
        if type(lst[0]) is list:
            lst[0], residue_left, residue_right, exploded = explode(lst[0], depth + 1)
            if exploded:
                wasLeft = True
        if type(lst[1]) is list and not exploded:
            lst[1], residue_left, residue_right, exploded = explode(lst[1], depth + 1)
            if exploded:
                wasRight = True
        if residue_left != 0 and not wasLeft:
            lst[0], residue_left = add_number(lst[0], residue_left, 1)
        if residue_right != 0 and not wasRight:
            lst[1], residue_right = add_number(lst[1], residue_right, 0)
    return lst, residue_left, residue_right, exploded


def split(lst):
    split_state = False
    if type(lst[0]) is list:
        lst[0], split_state = split(lst[0])
    elif type(lst[0]) is int and lst[0] >= 10:
        lst[0], split_state = [int(lst[0] / 2), math.ceil(lst[0] / 2)], True
    if split_state:
        return lst, split_state
    if type(lst[1]) is list:
        lst[1], split_state = split(lst[1])
    elif type(lst[1]) is int and lst[1] >= 10:
        lst[1], split_state = [int(lst[1] / 2), math.ceil(lst[1] / 2)], True
    return lst, split_state


def reduce(number1, number2):
    result = [number1, number2]
    while True:
        result, _, _, changed = explode(result, 0)
        if changed:
            continue
        result, changed = split(result)
        if not changed:
            break
    return result


def parse_result(value):
    if type(value) is int:
        return value
    return 3 * parse_result(value[0]) + 2 * parse_result(value[1])


def main(inp):
    if inp == [""]:
        return None

    inpa = []
    for b in inp:
        inpa.append(json.loads(b))
    resulting_list = []
    for i in range(len(inpa)):
        for j in range(len(inpa)):
            value = reduce(copy.deepcopy(inpa[i]), copy.deepcopy(inpa[j]))
            if i != j:
                resulting_list.append(parse_result(value))
    return max(resulting_list)


ut.aoc_check(main, __file__, [], True)
