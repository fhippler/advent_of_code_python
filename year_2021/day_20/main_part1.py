#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"

fields = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]


def check_image(area, algorithm):
    pixel = ""
    for a in area:
        if a == "#":
            pixel += "1"
        else:
            pixel += "0"

    number = ut.toDeci(2, pixel)
    return algorithm[number]


def copy_with_padding(image, amount):
    new_image = []
    t = "." * (len(image[0]) + 2 * amount)
    for i in range(amount):
        new_image.append(t)
    for b in image:
        new_image.append("." * amount + b + "." * amount)
    for i in range(amount):
        new_image.append(t)
    return new_image


def main(inp):
    if inp == [""]:
        return None

    algorithm = ""
    for i in range(len(inp)):
        if inp[i] == "":
            break
        algorithm += inp[i]
    image = []
    for j in range(i + 1, len(inp)):
        if inp[j] == "":
            continue
        image.append(inp[j])

    iterations = 2
    image = copy_with_padding(image, iterations)
    replacer = "."
    for i in range(iterations):
        new_image = []
        for h in range(len(image)):
            newline = ""
            for w in range(len(image)):
                temp = [
                    image[h + x][w + y]
                    if (h + x) >= 0
                    and (w + y) >= 0
                    and (h + x) < len(image)
                    and (w + y) < len(image[0])
                    else replacer
                    for (x, y) in fields
                ]
                a = "".join(temp)
                newline = newline[:w] + check_image(a, algorithm) + newline[w + 1 :]
            new_image.append(newline)
        replacer = check_image(replacer * 9, algorithm)
        image = new_image

    lit = 0
    for a in image:
        for b in a:
            if b == "#":
                lit += 1
    return lit


ut.aoc_check(main, __file__, [])
