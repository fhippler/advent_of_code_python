#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def check(v, w):
    if v == 0 or v == (w - 1):
        return True
    else:
        return False


def check_visible(pos_x, pos_y, width, height, inp):
    if pos_x == 0 or pos_y == 0 or pos_x == width - 1 or pos_y == height - 1:
        return True
    tree_size = int(inp[pos_y][pos_x])
    lb, ub, rb, db = False, False, False, False
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    for d in directions:
        new_pos_x = pos_x
        new_pos_y = pos_y
        dir_blocked = False
        while 0 <= new_pos_x <= width - 1 and 0 <= new_pos_y <= height - 1:
            new_pos_x = d[0] + new_pos_x
            new_pos_y = d[1] + new_pos_y
            if int(inp[new_pos_y][new_pos_x]) >= tree_size:
                dir_blocked = True
            if dir_blocked:
                break
            if check(new_pos_x, width) or check(new_pos_y, height):
                return True

    return False


def main(inp):
    if inp == [""]:
        return None

    result = 0
    positions = []
    height = len(inp)
    for y in range(height):
        width = len(inp[y])
        for x in range(width):
            # one tree element
            if check_visible(x, y, width, height, inp):
                result += 1
                positions.append((x, y, inp[y][x]))
    return result


ut.aoc_check(main, __file__, [], True)
