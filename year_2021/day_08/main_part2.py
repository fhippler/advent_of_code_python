#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

import re

__version__ = "1.0.0"


def main(inp):
    if inp == [""]:
        return None

    result = 0

    numbers = {
        "abc efg": 0,
        "  c  f ": 1,
        "a cde g": 2,
        "a cd fg": 3,
        " bcd f ": 4,
        "ab d fg": 5,
        "ab defg": 6,
        "a c  f ": 7,
        "abcdefg": 8,
        "abcd fg": 9,
    }
    # 0: 6 abc efg
    # 1: 2   c  f
    # 2: 5 a cde g
    # 3: 5 a cd fg
    # 4: 4  bcd f
    # 5: 5 ab d fg
    # 6: 6 ab defg
    # 7: 3 a c  f
    # 8: 7 abcdefg
    # 9:   abcd fg
    # sum  8687497

    base_list = ["a", "b", "c", "d", "e", "f", "g"]
    m = []
    for a in inp:
        m.append(a.split(" | "))
    n = []
    for a in m:
        n.append([a[0], a[1].split(" "), {a: "" for a in base_list.copy()}])

    def count_chars(somestring):
        chars = {a: 0 for a in base_list.copy()}
        for c in somestring:
            if c != " ":
                chars[c] += 1
        return chars

    for entry in n:
        left_side = " " + entry[0] + " "
        # find mapping of 1
        one_string = re.findall(" [a-g]{2} ", left_side)[0].strip()
        # find mapping of 4
        four_string = re.findall(" [a-g]{4} ", left_side)[0].strip()
        # find mapping of 7
        seven_string = re.findall(" [a-g]{3} ", left_side)[0].strip()
        # find mapping of 8
        eight_string = re.findall(" [a-g]{7} ", left_side)[0].strip()

        one_count = count_chars(one_string)
        seven_count = count_chars(seven_string)
        all_count = count_chars(left_side)

        for inp, y in entry[2].items():
            if one_count[inp] < seven_count[inp]:
                entry[2]["a"] = inp
            if all_count[inp] == 9:
                entry[2]["f"] = inp
            if all_count[inp] == 6:
                entry[2]["b"] = inp
            if all_count[inp] == 4:
                entry[2]["e"] = inp

        entry[2]["c"] = one_string.replace(" ", "").replace(entry[2]["f"], "")
        entry[2]["d"] = (
            four_string.replace(" ", "")
            .replace(entry[2]["b"], "")
            .replace(entry[2]["c"], "")
            .replace(entry[2]["f"], "")
        )
        entry[2]["g"] = (
            eight_string.replace(" ", "")
            .replace(entry[2]["a"], "")
            .replace(entry[2]["b"], "")
            .replace(entry[2]["c"], "")
            .replace(entry[2]["d"], "")
            .replace(entry[2]["e"], "")
            .replace(entry[2]["f"], "")
        )

        value = ""
        for chars in entry[1]:
            temp = ""
            for c in base_list:
                if entry[2][c] in chars:
                    temp += c
                else:
                    temp += " "
            value += str(numbers[temp])
        result += int(value)

    return result


ut.aoc_check(main, __file__, [], True)
