#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def solve_equ(expr):
    try:
        return int(expr)
    except ValueError:
        l_index = expr.find("(")
        if l_index != -1:
            stack = "("
            for i in range(l_index + 1, len(expr)):
                if expr[i] == "(":
                    stack += "("
                elif expr[i] == ")":
                    stack = stack[:-1]
                if stack == "":
                    return solve_equ(
                        expr[:l_index]
                        + str(solve_equ(expr[l_index + 1 : i]))
                        + expr[i + 1 :]
                    )
                    # TODO
        l_index = expr.find("+")
        if l_index != -1:
            l = l_index - 1
            while l > 0 and expr[l - 1].isnumeric():
                l -= 1
            r = l_index + 1
            while r < len(expr) and expr[r].isnumeric():
                r += 1
            result = int(expr[l:l_index]) + int(expr[l_index + 1 : r])
            return solve_equ(expr[:l] + str(result) + expr[r:])
        l_index = expr.find("*")
        if l_index != -1:
            return solve_equ(expr[:l_index]) * solve_equ(expr[l_index + 1 :])
    raise ValueError("Something went wrong.")


def main(inp):
    if inp == [""]:
        return None

    result = 0
    for b in inp:
        result += solve_equ(b.replace(" ", ""))

    return result


ut.aoc_check(main, __file__, [], True)
