#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

import re

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None
    a = []
    s = []
    for b in inp:
        if b == "":
            continue
        a.append(re.split(" bags contain ", b))
        if len(re.findall("no other bag", a[-1][1])) > 0:
            a.remove(a[-1])
        if len(re.findall("shiny gold bag", a[-1][1])) > 0:
            s.append(a[-1])
            a.remove(a[-1])

    while True:
        length = len(s)
        for b in s:
            for c in a.copy():
                if len(re.findall(b[0], c[1])) > 0:
                    s.append(c)
                    a.remove(c)
        if length == len(s):
            break
    return len(s)


ut.aoc_check(main, __file__, [])
