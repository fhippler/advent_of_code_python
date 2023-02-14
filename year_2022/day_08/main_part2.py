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


def check_score(pos_x, pos_y, width, height, inp):
    tree_size = int(inp[pos_y][pos_x])
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    dir_scores = []
    for d in directions:
        new_pos_x = pos_x
        new_pos_y = pos_y
        dir_score = 0
        lowest_tree = -1
        while 0 <= new_pos_x <= width - 1 and 0 <= new_pos_y <= height - 1:
            new_pos_x = d[0] + new_pos_x
            new_pos_y = d[1] + new_pos_y
            if not (0 <= new_pos_x <= width - 1 and 0 <= new_pos_y <= height - 1):
                break
            if int(inp[new_pos_y][new_pos_x]) >= tree_size:
                dir_score += 1
                break
            else:
                dir_score += 1

        dir_scores.append(dir_score)
    else:
        return dir_scores


def main(inp):
    if inp == [""]:
        return None

    positions = []
    height = len(inp)
    for y in range(height):
        width = len(inp[y])
        for x in range(width):
            scores = check_score(x, y, width, height, inp)
            t = 1
            for s in scores:
                t *= s
            positions.append((x, y, t))
    m = (-1, -1, 0)
    for p in positions:
        if p[2] > m[2]:
            m = p
    return m[2]


ut.aoc_check(main, __file__, [], True)
