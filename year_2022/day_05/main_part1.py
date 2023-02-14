#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    field = []
    moves = []
    b = True
    for x in inp:
        if x == "":
            b = False
            continue
        if b == True:
            field.insert(0, x)
        else:
            moves.append(x)
    # print(*field, sep="\n")
    # print(field[1].split(" "))
    field_dict = {}
    for i in range(1, len(field[0].split("   ")) + 1):
        for x in field[1:]:
            y = ut.slice_list(x, [3], 1)
            # print(len(y), i, y)
            y = y[i - 1]
            if y == "" or y == "   ":
                continue
            if i in field_dict:
                field_dict[i].append(y)
            else:
                field_dict[i] = [y]
    # print("\n", *(field_dict.items()), "\n", sep="\n")

    for m in moves:
        # print(*(field_dict.items()), "\n", sep="\n")
        n = m.split(" ")
        amount = int(n[1])
        fromx = int(n[3])
        tox = int(n[5])
        # print(amount, fromx, tox)
        # paste elements
        field_dict[tox] = field_dict[tox] + list(reversed(field_dict[fromx][-amount:]))
        # cut elements
        field_dict[fromx] = field_dict[fromx][:-amount]

    # print(*(field_dict.items()), "\n", sep="\n")
    result = ""
    for fd in field_dict.values():
        result += fd[-1][1]
    # print(result)
    return result


ut.aoc_check(main, __file__, [])
