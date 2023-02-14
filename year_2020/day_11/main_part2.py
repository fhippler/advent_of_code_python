#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None
    result = 0

    current = inp.copy()
    nextP = current.copy()

    a = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    while True:
        for i in range(len(current)):
            for k in range(len(current[i])):
                if current[i][k] == ".":
                    continue
                count_adjacent = 0
                for b in a:
                    factor = 1
                    while True:
                        b0 = i + b[0] * factor
                        b1 = k + b[1] * factor
                        # print("b0: " + str(b0) + " b1: " + str(b1) + " Current: " + str(current[b0][b1]))
                        if (
                            b0 < 0
                            or b1 < 0
                            or b0 >= len(current)
                            or b1 >= len(current[b0])
                        ):
                            break
                        if current[b0][b1] == ".":
                            factor += 1
                        elif current[b0][b1] == "L":
                            break
                        elif current[b0][b1] == "#":
                            count_adjacent += 1
                            break
                if count_adjacent >= 5:
                    nextP[i] = nextP[i][:k] + "L" + nextP[i][k + 1 :]
                elif count_adjacent == 0:
                    nextP[i] = nextP[i][:k] + "#" + nextP[i][k + 1 :]
        if current == nextP:
            break
        current = nextP.copy()

    for i in nextP:
        for k in i:
            if k == "#":
                result += 1

    return result


ut.aoc_check(main, __file__, [])
