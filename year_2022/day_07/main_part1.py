#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def add_to_file_system(dir, cdir, e, f):
    if len(cdir) > 1:
        add_to_file_system(dir[cdir[0]], cdir[1:], e, f)
    elif cdir[0] in dir and f != None:
        dir[cdir[0]][e] = f
    elif cdir[0] not in dir and f != None:
        dir[cdir[0]][e] = [f]
    else:
        dir[cdir[0]][e] = {}


def calculate_size(dir):
    result = {}
    total = 0
    for u, v in dir.items():
        if type(v) is str:
            total += int(v)
        else:
            temp = calculate_size(v)
            result[u + "/"] = temp[1]
            # result.update(temp[0])
            for x, y in temp[0].items():
                result[u + "/" + x] = y
            total += result[u + "/"]
    return result, total


def main(inp):
    if inp == [""]:
        return None

    current_dir = ["/"]
    file_system = {"/": {}}
    for x in inp:
        t = x.split(" ")
        if t[0] == "$":  # command
            if t[1] == "cd":
                if t[2] == "/":
                    current_dir = ["/"]
                elif t[2] == "..":
                    current_dir = current_dir[:-1] if len(current_dir) > 1 else ["/"]
                else:
                    current_dir.append(t[2])
            elif t[1] == "ls":
                pass
        elif t[0] == "dir":  # add new dir to current_dir
            add_to_file_system(file_system, current_dir, t[1], None)
        else:  # add new file to current_dir
            add_to_file_system(file_system, current_dir, t[1], t[0])

    # dicts_to_search = [file_system]
    # for d in dicts_to_search:
    #     if calculate_size_only
    total = 0
    small_dirs = set()
    result = calculate_size(file_system)[0]
    for x, y in result.items():
        if int(y) <= 100000:
            small_dirs.add((x, y))
            total += int(y)
    return total


ut.aoc_check(main, __file__, [], True)
