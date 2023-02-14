#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def move_east(inp):
    move_coords = set()
    for b in range(len(inp)):
        for a in range(len(inp[b])):
            if a + 1 == len(inp[b]):
                if inp[b][a] == ">" and inp[b][0] == ".":
                    move_coords.add(((b, a), (b, 0)))
            else:
                if inp[b][a] == ">" and inp[b][a + 1] == ".":
                    move_coords.add(((b, a), (b, a + 1)))
    for (a, b), (c, d) in move_coords:
        if d == 0:
            inp[a] = ">" + inp[a][1:-1] + "."
        else:
            inp[a] = inp[a][:b] + ".>" + inp[a][b + 2 :]
    return inp


def move_south(inp):
    move_coords = set()
    for a in range(len(inp)):
        for b in range(len(inp[a])):
            if a + 1 == len(inp):
                if inp[a][b] == "v" and inp[0][b] == ".":
                    move_coords.add(((a, b), (0, b)))
            else:
                if inp[a][b] == "v" and inp[a + 1][b] == ".":
                    move_coords.add(((a, b), (a + 1, b)))
    for (a, b), (c, d) in move_coords:
        inp[c] = inp[c][:d] + "v" + inp[c][d + 1 :]
        inp[a] = inp[a][:b] + "." + inp[a][b + 1 :]
    return inp


def main(inp):
    if inp == [""]:
        return None

    counter = 0
    while True:
        counter += 1
        copy = inp.copy()
        move_east(inp)
        move_south(inp)
        if inp == copy:
            break
    return counter


ut.aoc_check(main, __file__, [], True)
