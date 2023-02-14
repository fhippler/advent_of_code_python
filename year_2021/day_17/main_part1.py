#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def check_vel(xVelc, yVelc, targetX1, targetX2, targetY1, targetY2):
    xPos, yPos, maxY = 0, 0, 0
    xVel, yVel = xVelc, yVelc

    xR = range(targetX1, targetX2 + 1)
    yR = range(targetY1, targetY2 + 1)

    # print("Pos:", xPos, yPos)
    maxRX = max(abs(targetX1), abs(targetX2)) * 1000
    maxRY = max(abs(targetY1), abs(targetY2)) * 1000
    while abs(xPos) < maxRX and abs(yPos) < maxRY:
        # print("Pos:", xPos, yPos)
        xPos += xVel
        yPos += yVel
        if xVel == 0:
            pass
        elif xVel < 0:
            xVel += 1
        elif xVel > 0:
            xVel -= 1
        yVel -= 1
        if yPos > maxY:
            maxY = yPos
        if xPos in xR and yPos in yR:
            return maxY
    return -1


def main(inp):
    if inp == [""]:
        return None

    inp = inp[0].split(" ")
    x = inp[2].split("=")[1].split(".")
    x1 = int(x[0])
    x2 = int(x[2].split(",")[0])
    if x2 < x1:
        x1, x2 = x2, x1
    y = inp[3].split("=")[1].split(".")
    y1 = int(y[0])
    y2 = int(y[2].split(",")[0])
    if y2 < y1:
        y1, y2 = y2, y1

    val = 0
    maxY = float("-inf")
    for i in range(1, 500):
        for j in range(1, 500):
            val = check_vel(i, j, x1, x2, y1, y2)
            if val != -1 and val > maxY:
                maxY = val

    return maxY


ut.aoc_check(main, __file__, [])
