#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

import networkx as nx

__version__ = "1.0.0"


def calc_val(a):
    while a >= 10:
        a -= 9
    return a


def main(inp):
    if inp == [""]:
        return None

    ninp = []
    for j in range(5):
        for y in inp:
            newline = []
            for i in range(5):
                for a in [calc_val(int(x) + i + j) for x in y]:
                    newline.append(a)
            ninp.append(newline)

    inp = ninp
    G = nx.DiGraph()

    # add nodes
    c = 0
    for y in inp:
        for x in y:
            G.add_node(c)
            c += 1

    # add edges with weight
    c = 0
    length = len(inp[-1])
    height = len(inp)
    for y in range(height):
        for x in range(length):
            if y < height - 1:
                G.add_edge(c, c + len(inp[-1]), weight=int(inp[x][y + 1]))
                G.add_edge(c + len(inp[-1]), c, weight=int(inp[x][y]))
            if x < length - 1:
                G.add_edge(c, c + 1, weight=int(inp[x + 1][y]))
                G.add_edge(c + 1, c, weight=int(inp[x][y]))
            c += 1

    # shortest path as list
    result = nx.shortest_path(G, source=0, target=c - 1, weight="weight")

    # shortest path length [including the weight]
    result = nx.shortest_path_length(G, source=0, target=c - 1, weight="weight")

    return result


ut.aoc_check(main, __file__, [], True)
