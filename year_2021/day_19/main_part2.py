#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

from numpy import rot90, array
import re

__version__ = "1.0.0"


def rotations24(polycube):
    """List all 24 rotations of the given 3d array"""

    def rotations4(polycube, axes):
        """List the four rotations of the given 3d array in the plane spanned by the given axes."""
        for i in range(4):
            yield rot90(polycube, i, axes)

    # imagine shape is pointing in axis 0 (up)

    # 4 rotations about axis 0
    yield from rotations4(polycube, (1, 2))

    # rotate 180 about axis 1, now shape is pointing down in axis 0
    # 4 rotations about axis 0
    yield from rotations4(rot90(polycube, 2, axes=(0, 2)), (1, 2))

    # rotate 90 or 270 about axis 1, now shape is pointing in axis 2
    # 8 rotations about axis 2
    yield from rotations4(rot90(polycube, axes=(0, 2)), (0, 1))
    yield from rotations4(rot90(polycube, -1, axes=(0, 2)), (0, 1))

    # rotate about axis 2, now shape is pointing in axis 1
    # 8 rotations about axis 1
    yield from rotations4(rot90(polycube, axes=(0, 1)), (0, 2))
    yield from rotations4(rot90(polycube, -1, axes=(0, 1)), (0, 2))


def polycubeOf(x, y, z):
    polycube = array(
        [
            [[0, 0, 0], [0, x, 0], [0, 0, 0]],
            [[0, z, 0], [-y, 0, y], [0, -z, 0]],
            [[0, 0, 0], [0, -x, 0], [0, 0, 0]],
        ]
    )
    return polycube


def polycubeTo(polycube):
    x = y = z = 0
    x = polycube[0][1][1]
    y = polycube[1][1][2]
    z = polycube[1][0][1]
    return x, y, z


def allRotations(x, y, z):
    result = [
        (x, y, z),
        (x, -z, y),
        (x, -y, -z),
        (x, z, -y),
        (-x, -y, z),
        (-x, -z, -y),
        (-x, y, -z),
        (-x, z, y),
        (y, -x, z),
        (-z, -x, y),
        (-y, -x, -z),
        (z, -x, -y),
        (-y, x, z),
        (-z, x, -y),
        (y, x, -z),
        (z, x, y),
        (-z, y, x),
        (y, z, x),
        (z, -y, x),
        (-y, -z, x),
        (z, y, -x),
        (y, -z, -x),
        (-z, -y, -x),
        (-y, z, -x),
    ]

    return result


def check(scanner1, beacons):
    # iterate over all 24 rotations
    s1coordsByRotation = []
    for i in range(24):
        temp = []
        for c in scanner1[1]:
            # temp.append(polycubeTo(list(rotations24(polycubeOf(c[0], c[1], c[2])))[i]))
            temp.append(allRotations(c[0], c[1], c[2])[i])
        s1coordsByRotation.append(temp)

    # potential starting positions
    starting_pos = set()
    for rot in s1coordsByRotation:
        for b in beacons:
            for c in rot:
                starting_pos.add((b[0] - c[0], b[1] - c[1], b[2] - c[2], tuple(rot)))

    c_sp = (0, 0, 0)
    for sp in starting_pos:
        temp = []
        for c in sp[3]:
            for b in beacons:
                if (
                    sp[0] + c[0] == b[0]
                    and sp[1] + c[1] == b[1]
                    and sp[2] + c[2] == b[2]
                ):
                    temp.append(b)
                    break
        if len(temp) >= 12:
            c_sp = sp
            break
    if c_sp[0] != 0 and c_sp[1] != 0 and c_sp[2] != 0:
        global counter
        counter += 1
        for c in c_sp[3]:
            beacons.add(tuple([c_sp[0] + c[0], c_sp[1] + c[1], c_sp[2] + c[2]]))

    return c_sp[0], c_sp[1], c_sp[2]


def main(inp):
    if inp == [""]:
        return None

    positions = []
    for b in inp:
        x = re.search("\(\([^)]*\)\)", b)
        print(x.group()[2:-2])
        positions.append(tuple([int(z) for z in x.group()[2:-2].split(", ")]))

    diff = []
    for p in positions:
        for o in positions:
            if p != o:
                diff.append(abs(p[0] - o[0]) + abs(p[1] - o[1]) + abs(p[2] - o[2]))
    return max(diff)


ut.aoc_check(main, __file__, [])
