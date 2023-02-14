#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

import networkx as nx
from networkx.algorithms import shortest_paths
from networkx.algorithms.shortest_paths.generic import shortest_path_length


__version__ = "1.0.0"


def choose_path(x, y, path, inp, result):
    path.append([x, y, int(inp[y][x])])
    if y == len(inp) - 1 and x == len(inp[-1]) - 1:
        result.append(path)
        return
    if y + 1 < len(inp):
        choose_path(x, y + 1, path, inp, result)
    if x + 1 < len(inp[-1]):
        choose_path(x + 1, y, path, inp, result)


def main(inp):
    if inp == [""]:
        return None

    G = nx.DiGraph()

    c = 0
    for y in inp:
        for x in y:
            G.add_node(c)
            c += 1

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

    result = nx.shortest_path(G, source=0, target=c - 1, weight="weight")
    # print(result)
    result = nx.shortest_path_length(G, source=0, target=c - 1, weight="weight")
    # print(result)

    return result


ut.aoc_check(main, __file__, [], True)
