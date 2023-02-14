#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"

result = 0
t = [[i, j] for i in range(-1, 2) for j in range(-1, 2) if not (i == 0 and j == 0)]


def increase_energy(inp, x, y, p):
    if x < 0 or x >= len(inp) or y < 0 or y >= len(inp[0]) or (x, y) in p:
        return
    val = int(inp[x][y])
    inp[x] = inp[x][:y] + str((val + 1) % 10) + inp[x][y + 1 :]
    if val == 9:
        p.append((x, y))
        for i, j in t:
            increase_energy(inp, x + i, y + j, p)


def main(inp):
    if inp == [""]:
        return None

    for m in range(1, 1000):
        flashed = []
        for i in range(len(inp)):
            for j in range(len(inp[i])):
                increase_energy(inp, i, j, flashed)
        if len(flashed) == (len(inp) * len(inp[0])):
            result = m
            break
    return result


ut.aoc_check(main, __file__, [], True)
