#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def fold(x, coord, field):
    if x == "x":
        # fold x -> fold left
        for y in range(len(field)):
            st1 = field[y][:coord]
            st2 = field[y][coord + 1 :]
            st3 = ""
            for i in range(coord):
                if st1[coord - 1 - i] == "#" or (i < len(st2) and st2[i] == "#"):
                    st3 = "#" + st3
                else:
                    st3 = "." + st3
            field[y] = st3
    else:
        # fold y -> fold up
        del field[coord]  # remove line where it folds
        for j in range(coord):
            if coord >= len(field):
                break
            line1 = coord - 1 - j
            st1 = field[line1]
            st2 = field[coord]  # get next line to combine
            st3 = ""
            if len(st1) != len(st2):
                raise ValueError("Different lengths!")
            for i in range(min(len(st1), len(st2))):
                st3 += "#" if st1[i] == "#" or st2[i] == "#" else "."
            field[line1] = st3
            del field[coord]  # remove next line


def main(inp):
    if inp == [""]:
        return None

    numbers = [x for x in inp if not x.startswith("fold along ")]
    numbers = [(int(x), int(y)) for x, y in [n.split(",") for n in numbers]]
    folds = [
        (a, int(b))
        for a, b in [
            x.split(" ")[-1].split("=") for x in inp if x.startswith("fold along ")
        ]
    ]

    maxX = max(numbers, key=lambda x: x[0])[0] + 1
    maxY = max(numbers, key=lambda y: y[1])[1] + 1

    field = ["." * maxX for _ in range(maxY)]
    for n in numbers:
        x, y = n[0], n[1]
        field[y] = field[y][:x] + "#" + field[y][x + 1 :]

    for f in folds:
        fold(f[0], f[1], field)

    for f in field:
        print(f)
    return None


ut.aoc_check(main, __file__, [0], True)
