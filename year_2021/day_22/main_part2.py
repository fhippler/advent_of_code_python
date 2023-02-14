#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def cutSingleRange(rangeA, rangeB):
    resultingRanges = []
    if (
        rangeA[0] < rangeB[0]
        and rangeB[0] < rangeA[1]
        and rangeA[0] < rangeB[1]
        and rangeB[1] < rangeA[1]
    ):
        # range enclosed
        range1 = (rangeA[0], rangeB[0] - 1)
        range2 = (rangeB[1] + 1, rangeA[1])
        resultingRanges.append(range1)
        resultingRanges.append(range2)
    elif rangeB[0] > rangeA[1] or rangeB[1] < rangeA[0]:
        # range completely different
        resultingRanges.append(rangeA)
    elif rangeB[1] >= rangeA[0] and rangeB[1] < rangeA[1]:
        # range cut lower
        range1 = (rangeB[1] + 1, rangeA[1])
        resultingRanges.append(range1)
    elif rangeB[0] <= rangeA[1] and rangeB[0] > rangeA[0]:
        # range cut upper
        range1 = (rangeA[0], rangeB[0] - 1)
        resultingRanges.append(range1)
    elif rangeA[0] >= rangeB[0] and rangeA[1] <= rangeB[1]:
        # range disappears
        pass
    else:
        print("Some other case:", rangeA, rangeB)
    return resultingRanges


def cutRange(rangeA, rangeB):
    resultingRanges = []
    if (
        (rangeA[0][0] > rangeB[0][1] or rangeB[0][0] > rangeA[0][1])
        or (rangeA[1][0] > rangeB[1][1] or rangeB[1][0] > rangeA[1][1])
        or (rangeA[2][0] > rangeB[2][1] or rangeB[2][0] > rangeA[2][1])
    ):
        return [rangeA]
    for xRange in cutSingleRange(rangeA[0], rangeB[0]):
        resultingRanges.append((xRange, rangeA[1], rangeA[2]))
    for yRange in cutSingleRange(rangeA[1], rangeB[1]):
        resultingRanges.append((rangeA[0], yRange, rangeA[2]))
    for zRange in cutSingleRange(rangeA[2], rangeB[2]):
        resultingRanges.append((rangeA[0], rangeA[1], zRange))
    return resultingRanges


def cubesOnCounter(someRange):
    return (
        (someRange[0][1] + 1 - someRange[0][0])
        * (someRange[1][1] + 1 - someRange[1][0])
        * (someRange[2][1] + 1 - someRange[2][0])
    )


def mergeRanges(rangeA, rangeB):
    resultingRanges = []
    resultingRanges.append(rangeA)
    for x in cutRange(rangeB, rangeA):
        resultingRanges.append(x)
    return resultingRanges


def main(inp):
    if inp == [""]:
        return None

    coords = []
    for b in inp:
        temp = []
        for t in b.split(","):
            val = t.split("=")[1].split("..")
            temp.append((int(val[0]), int(val[1])))
        coords.append(temp + [b.split(" ")[0]])

    rangesOn = set()
    for i in range(len(coords)):
        entry = coords[i]
        if entry[3] == "on":
            rangesOn.add((entry[0], entry[1], entry[2]))
        elif entry[3] == "off":
            new_set = set()
            for rangeOn in rangesOn:
                for result in cutRange(rangeOn, entry):
                    new_set.add(tuple(result))
            rangesOn = new_set

    on = rangesOn.copy()
    cubes = 0
    while on:
        elem = on.pop()
        new_on = set()
        cubes += cubesOnCounter(elem)
        for r in on:
            for x in cutRange(r, elem):
                new_on.add(x)
        on = new_on

    return cubes


ut.aoc_check(main, __file__, [], True)
