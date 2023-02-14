#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def bin_to_dec(x):
    return ut.toDeci(2, x)


def hex_to_bin(someinp):
    bin = ""
    for hex in someinp:
        if hex == "0":
            bin += "0000"
        elif hex == "1":
            bin += "0001"
        elif hex == "2":
            bin += "0010"
        elif hex == "3":
            bin += "0011"
        elif hex == "4":
            bin += "0100"
        elif hex == "5":
            bin += "0101"
        elif hex == "6":
            bin += "0110"
        elif hex == "7":
            bin += "0111"
        elif hex == "8":
            bin += "1000"
        elif hex == "9":
            bin += "1001"
        elif hex == "A":
            bin += "1010"
        elif hex == "B":
            bin += "1011"
        elif hex == "C":
            bin += "1100"
        elif hex == "D":
            bin += "1101"
        elif hex == "E":
            bin += "1110"
        elif hex == "F":
            bin += "1111"
    return bin


def eval_node(node):
    if node[0] == "op":
        v = bin_to_dec(node[2])
        if v == 0:
            res = 0
            for n in node[6]:
                res += eval_node(n)
            return res
        elif v == 1:
            res = 1
            for n in node[6]:
                res *= eval_node(n)
            return res
        elif v == 2:
            mini = float("inf")
            for n in node[6]:
                mini = min(eval_node(n), mini)
            return mini
        elif v == 3:
            maxi = float("-inf")
            for n in node[6]:
                maxi = max(eval_node(n), maxi)
            return maxi
        elif v == 5:
            if eval_node(node[6][0]) > eval_node(node[6][1]):
                return 1
            else:
                return 0
        elif v == 6:
            if eval_node(node[6][0]) < eval_node(node[6][1]):
                return 1
            else:
                return 0
        elif v == 7:
            if eval_node(node[6][0]) == eval_node(node[6][1]):
                return 1
            else:
                return 0
    elif node[0] == "lit":
        return node[4]


def compile_packet(bin, package_list, counter):
    if bin == "":
        return counter + 1
    v = bin[counter : counter + 3]
    counter += 3
    t = bin[counter : counter + 3]
    counter += 3
    if bin_to_dec(t) == 4:
        # literal value
        binval = ""
        while True:
            flag = True
            if bin[counter] == "0":
                flag = False
            counter += 1
            binval += bin[counter : counter + 4]
            counter += 4
            if flag == False:
                break
        binvalv = bin_to_dec(binval)
        package_list.append(["lit", v, t, binval, binvalv])
    else:
        # operator
        i = bin[counter]
        counter += 1
        length = 0
        if i == "0":
            length = 15
        elif i == "1":
            length = 11
        l = bin[counter : counter + length]
        counter += length
        lv = bin_to_dec(l)
        subnodes = []
        if i == "0":
            ccounter = counter
            while counter - ccounter < lv:
                counter = compile_packet(bin, subnodes, counter)
        elif i == "1":
            for i in range(lv):
                counter = compile_packet(bin, subnodes, counter)
        package_list.append(["op", v, t, i, l, lv, subnodes])

    return counter


def main(inp):
    if inp == [""]:
        return None

    res = []
    sinp = hex_to_bin(inp[0])
    compile_packet(sinp, res, 0)

    return eval_node(res[0])


ut.aoc_check(main, __file__, [])
