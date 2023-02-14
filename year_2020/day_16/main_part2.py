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


def check_value(value, ranges):
    if ranges[0][0] <= value <= ranges[0][1] or ranges[1][0] <= value <= ranges[1][1]:
        return True
    return False


def parse_input(inp):
    possible_values, my_ticket, nearby_tickets, stage = {}, "", [], 0
    for b in inp:
        if b == "your ticket:":
            stage = 1
        elif b == "nearby tickets:":
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
    return possible_values, my_ticket, nearby_tickets


def main(inp):
    if inp == [""]:
        return None

    possible_values, my_ticket, nearby_tickets = parse_input(inp)

    valid_tickets = nearby_tickets.copy()

    for ticket in nearby_tickets:
        if check_ticket(ticket, possible_values) != []:
            valid_tickets.remove(ticket)

    valid_tickets.append(my_ticket)

    ticket_values = []
    for i in range(len(my_ticket.split(","))):
        ticket_values.append([])
        for ticket in valid_tickets:
            ticket_values[-1].append(int(ticket.split(",")[i]))

    positions = {a: [] for a in possible_values.keys()}

    for i in range(len(ticket_values)):
        for a, b in possible_values.items():
            # if len(b) > 2: continue
            valid = True
            for value in ticket_values[i]:
                if not check_value(value, b):
                    valid = False
            if valid:
                positions[a].append(i)

    finished = []
    while True:
        item = ""
        for a, b in positions.items():
            if a not in finished and len(b) == 1:
                item = a
                break
        for a, b in positions.items():
            if a != item and positions[item][0] in b:
                b.remove(positions[item][0])
        finished.append(item)
        if len(finished) == len(positions.keys()):
            break

    result = 1
    for a, b in positions.items():
        if "departure" in a:
            result *= int(my_ticket.split(",")[b[0]])
    return result


ut.aoc_check(main, __file__, [], True)
