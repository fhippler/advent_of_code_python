#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def move(position, steps):
    result = position + steps
    while result > 10:
        result -= 10
    return result


def main(inp):
    if inp == [""]:
        return None

    p1 = int(inp[0].split(" ")[-1])
    p2 = int(inp[1].split(" ")[-1])
    p1wins, p2wins = 0, 0
    d = {(p1, 0, p2, 0, 0): 1}
    dmap = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    while True:
        for dstate, counter in d.items():
            if counter == 0:
                del d[dstate]
                break
            new_state = ()
            for elem, c in dmap.items():
                if dstate[4] == 0:
                    new_pos = move(dstate[0], elem)
                    new_score = dstate[1] + new_pos
                    if new_score >= 21:
                        p1wins += c * counter
                        continue
                    new_state = (new_pos, new_score, dstate[2], dstate[3], 1)
                else:
                    new_pos = move(dstate[2], elem)
                    new_score = dstate[3] + new_pos
                    if new_score >= 21:
                        p2wins += c * counter
                        continue
                    new_state = (dstate[0], dstate[1], new_pos, new_score, 0)
                if new_state in d:
                    d[new_state] += c * counter
                else:
                    d[new_state] = c * counter
            del d[dstate]
            break
        if not d:
            break
    return max(p1wins, p2wins)


ut.aoc_check(main, __file__, [])
