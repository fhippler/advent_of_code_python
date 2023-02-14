#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def solve_equ(expr):
    try:
        return int(expr)
    except ValueError:
        if expr[-1] == ")":
            stack = ")"
            for j in range(2, len(expr) + 1):
                i = len(expr) - j
                if expr[i] == ")":
                    stack += ")"
                elif expr[i] == "(":
                    stack = stack[:-1]
                if stack == "":
                    if i == 0:
                        return solve_equ(expr[1:-1])
                    elif expr[i - 1] == "*":
                        return solve_equ(expr[: i - 1]) * solve_equ(expr[i + 1 : -1])
                    elif expr[i - 1] == "+":
                        return solve_equ(expr[: i - 1]) + solve_equ(expr[i + 1 : -1])
        else:
            if expr[-2] == "*":
                return solve_equ(expr[:-2]) * int(expr[-1])
            elif expr[-2] == "+":
                return solve_equ(expr[:-2]) + int(expr[-1])
    raise ValueError("Something went wrong.")


def main(inp):
    if inp == [""]:
        return None

    result = 0
    for b in inp:
        result += solve_equ(b.replace(" ", ""))

    return result


ut.aoc_check(main, __file__, [], True)
