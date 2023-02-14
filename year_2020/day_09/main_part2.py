#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def is_sum(inp, i, pre):
    for a in range(pre):
        for b in range(pre):
            if int(inp[i - a - 1]) + int(inp[i - b - 1]) == int(inp[i]):
                return True


def main(inp):
    if inp == [""]:
        return None

    pre = 25
    for i in range(pre, len(inp)):
        if is_sum(inp, i, pre):
            continue
        else:
            result1 = int(inp[i])

    a = []
    current_sum = 0
    result2 = -1

    i = 0
    while i < len(inp):
        b = int(inp[i])
        if current_sum < result1:
            current_sum += b
            a.append(b)
            i += 1
        elif current_sum > result1:
            current_sum -= a[0]
            a.remove(a[0])
        else:
            v1 = float("inf")
            v2 = float("-inf")
            for c in a:
                if c < v1:
                    v1 = c
                if c > v2:
                    v2 = c
            result2 = v1 + v2
            break
    return result2


ut.aoc_check(main, __file__, [], True)
