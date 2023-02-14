#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def gen_words(rule, rules):
    words = []
    splits = rule.split(" | ")
    for split in splits:
        t_words = [""]
        t_rules = split.split(" ")
        for t_rule in t_rules:
            sub_words = []
            if t_rule.isnumeric():
                sub_words = gen_words(rules[t_rule], rules)
            else:
                sub_words = t_rule.split('"')[1]
            new_words = []
            for w1 in t_words:
                for w2 in sub_words:
                    new_words.append(w1 + w2)
            t_words = new_words
        words += t_words
    return words


def main(inp):
    if inp == [""]:
        return None

    rules = {}
    some_bool = True
    msg = []
    for b in inp:
        if b == "":
            some_bool = False
        elif some_bool:
            rules[b.split(":")[0]] = b.split(": ")[1]
        else:
            msg.append(b)

    words = set(gen_words(rules["0"], rules))

    result = 0
    for m in msg:
        if m in words:
            result += 1
    return result


ut.aoc_check(main, __file__, [])
