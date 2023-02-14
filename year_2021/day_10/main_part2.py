#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    a = [[b, []] for b in inp]
    d = {")": "(", "]": "[", "}": "{", ">": "<"}

    for b in a.copy():
        for c in b[0]:
            if c in d.values():
                b[1].append(c)
            elif b[1] and b[1][-1] == d[c]:
                b[1].pop()
            else:
                a.remove(b)
                break

    scores = []
    for b in a:
        result = 0
        while b[1]:
            stack_elem = b[1].pop()
            result *= 5
            if stack_elem == "(":
                result += 1
            elif stack_elem == "[":
                result += 2
            elif stack_elem == "{":
                result += 3
            elif stack_elem == "<":
                result += 4
        scores.append(result)

    scores.sort()
    return scores[int(len(scores) / 2)]


ut.aoc_check(main, __file__, [])
