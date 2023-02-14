#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


class Field:
    def __init__(self, lines):
        self.my5x5field = []
        for line in lines:
            self.my5x5field.append(line.split())

    def mark(self, number):
        for x in range(len(self.my5x5field)):
            for y in range(len(self.my5x5field[x])):
                if self.my5x5field[x][y] == number:
                    self.my5x5field[x][y] = "-1"

    def check(self):
        for x in range(5):
            sum1 = 0
            sum2 = 0
            for y in range(5):
                sum1 += int(self.my5x5field[x][y])
                sum2 += int(self.my5x5field[y][x])
                if sum1 == -5 or sum2 == -5:
                    print("Found result")
                    return True
        return False

    def __str__(self):
        return str(self.my5x5field)

    def sum_unmarked(self):
        sum = 0
        for x in self.my5x5field:
            for y in x:
                if int(y) > 0:
                    sum += int(y)
        return sum


def main(inp):
    if inp == [""]:
        return None

    numbers = inp[0].split(",")
    last_called_number = -1
    sum_unmarked = -1
    fields = []

    for i in range(1, len(inp[1:])):
        if len(inp[i].split()) == 0:
            fields.append(Field(inp[i + 1 : i + 6]))

    result = None

    for number in numbers:
        for field in fields:
            field.mark(number)
            if field.check() == True:
                result = field
                break
        if result != None:
            last_called_number = number
            break

    sum_unmarked = result.sum_unmarked()

    return sum_unmarked * int(last_called_number)


ut.aoc_check(main, __file__, [])
