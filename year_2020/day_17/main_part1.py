#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    neighbors = [
        (a, b, c)
        for a in range(-1, 2)
        for b in range(-1, 2)
        for c in range(-1, 2)
        if not (a == b == c == 0)
    ]

    coords = set()
    for x in range(len(inp)):
        for y in range(len(inp[x])):
            if inp[x][y] == "#":
                coords.add((x, y, 0))

    for i in range(6):
        new_cubes = set()
        inactive_coords = set()
        for coord in coords:
            active_counter = 0
            for n in neighbors:
                c = (coord[0] + n[0], coord[1] + n[1], coord[2] + n[2])
                if c in coords:
                    active_counter += 1
                else:
                    inactive_coords.add(c)
            if 2 <= active_counter <= 3:
                new_cubes.add(coord)

        for coord in inactive_coords:
            active_counter = 0
            for n in neighbors:
                c = (coord[0] + n[0], coord[1] + n[1], coord[2] + n[2])
                if c in coords:
                    active_counter += 1
            if active_counter == 3:
                new_cubes.add(coord)

        coords = new_cubes

    return len(coords)


ut.aoc_check(main, __file__, [])
