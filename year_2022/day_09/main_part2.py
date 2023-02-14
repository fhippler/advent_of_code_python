#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    directions = {"l": (-1, 0), "r": (1, 0), "u": (0, -1), "d": (0, 1)}
    knots = [(0, 0) for i in range(10)]
    result_states = set()
    result_states.add(knots[0])
    for x in inp:
        temp = x.split(" ")
        direction = temp[0].lower()
        for _ in range(int(temp[1])):
            knots[0] = (
                knots[0][0] + directions[direction][0],
                knots[0][1] + directions[direction][1],
            )
            for i in range(len(knots) - 1):
                c = knots[i][0] - knots[i + 1][0], knots[i][1] - knots[i + 1][1]
                d = abs(c[0]), abs(c[1])
                if (
                    (d[0] > 1 and d[1] == 1)
                    or (d[0] == 1 and d[1] > 1)
                    or (d[0] > 1 and d[1] > 1)
                ):  # move to old h
                    new_x = knots[i + 1][0] + (c[0] if -1 <= c[0] <= 1 else c[0] / 2)
                    new_y = knots[i + 1][1] + (c[1] if -1 <= c[1] <= 1 else c[1] / 2)
                    knots[i + 1] = (new_x, new_y)
                elif d[0] > 1:  # x is different
                    knots[i + 1] = (
                        int((knots[i][0] + knots[i + 1][0]) / 2),
                        knots[i + 1][1],
                    )
                elif d[1] > 1:
                    knots[i + 1] = (
                        knots[i + 1][0],
                        int((knots[i][1] + knots[i + 1][1]) / 2),
                    )
                else:
                    pass
            result_states.add(knots[-1])

    return len(result_states)


ut.aoc_check(main, __file__, [])
