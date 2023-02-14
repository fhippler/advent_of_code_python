#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def check_ticket(ticket, possible_values):
    invalid_numbers = []
    for v in ticket.split(","):
        valid = False
        for ranges in possible_values.values():
            for range in ranges:
                if range[0] <= int(v) <= range[1]:
                    valid = True
        if not valid:
            invalid_numbers.append(int(v))
    return invalid_numbers


def main(inp):
    if inp == [""]:
        return None

    possible_values = {}
    stage = 0
    nearby_tickets = []
    for b in inp:
        if b == "your ticket:":
            stage = 1
        if b == "nearby tickets:":
            stage = 2
        elif stage == 1:
            my_ticket = b
        elif stage == 2:
            nearby_tickets.append(b)
        else:
            values = b.split(": ")
            possible_values[values[0]] = []
            for c in values[1].split(" or "):
                t = c.split("-")
                possible_values[values[0]].append((int(t[0]), int(t[1])))

    invalid_numbers = []
    for ticket in nearby_tickets:
        invalid_numbers += check_ticket(ticket, possible_values)
    result = 0
    for v in invalid_numbers:
        result += v
    return result


ut.aoc_check(main, __file__, [], True)
