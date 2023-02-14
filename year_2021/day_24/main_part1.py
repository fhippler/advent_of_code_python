#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def test_number(inp, numbers):
    vars = {"w": numbers[0], "x": 0, "y": 0, "z": numbers[1]}
    for b in inp:
        op = b[:3]
        var = b[6:]
        if var.lstrip("-").isdigit():
            var = int(var)
        elif var != "":
            var = vars[var]
        if op == "add":
            current = b[4]
            vars[current] += var
        elif op == "sub":
            current = b[4]
            vars[current] -= var
        elif op == "mul":
            current = b[4]
            vars[current] *= var
        elif op == "div":
            current = b[4]
            vars[current] = int(vars[current] / var)
        elif op == "mod":
            current = b[4]
            vars[current] = int(vars[current] % var)
        elif op == "eql":
            current = b[4]
            vars[current] = 1 if vars[current] == var else 0
    return vars


def main(inp):
    if inp == [""]:
        return None

    programs = []
    help_c = 0
    for b in range(len(inp)):
        if inp[b] == "NL":
            elem = inp[help_c + 1 : b]
            elem.remove("mul x 0")
            elem.remove("mul y 0")
            programs.append(elem)
            print(elem)
            help_c = b + 1

    values = set()
    values.add((0, ""))
    while programs:
        program = programs.pop(0)
        curr_values = []
        remaining_divs = 0
        for p in programs:
            if ("div z 26") in p:
                remaining_divs += 1
        max_Z = pow(25, remaining_divs)
        for w in range(1, 10):
            for z, d in values:
                value = test_number(program, [w, z])
                if value["z"] <= max_Z:
                    curr_values.append((value["z"], d + str(w)))
        values = set(curr_values)
    max_elem = min_elem = values.pop()
    for a, b in values:
        if int(b) > int(max_elem[1]):
            max_elem = (a, b)
        if int(b) < int(min_elem[1]):
            min_elem = (a, b)
    print("Results:", min_elem[1], max_elem[1])
    # 18116121134117 39999698799429
    return int(min_elem[1])


ut.aoc_check(main, __file__, [])
