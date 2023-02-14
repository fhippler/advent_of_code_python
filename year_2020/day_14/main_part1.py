#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def val(c):
    if c >= "0" and c <= "9":
        return ord(c) - ord("0")
    else:
        return ord(c) - ord("A") + 10


def toDeci(sstr, base):
    llen = len(sstr)
    power = 1
    num = 0
    for i in range(llen - 1, -1, -1):
        if val(sstr[i]) >= base:
            print("Invalid Number")
            return -1
        num += val(sstr[i]) * power
        power = power * base
    return num


# fromDeci
def reVal(num):
    if num >= 0 and num <= 9:
        return chr(num + ord("0"))
    else:
        return chr(num - 10 + ord("A"))


def fromDeci(res, base, inputNum):
    while inputNum > 0:
        res += reVal(inputNum % base)
        inputNum = int(inputNum / base)
    res = res[::-1]
    return res


def index_masked(mask, index):
    bin = fromDeci("", 2, index)
    bin = "0" * (len(mask) - len(bin)) + bin
    result_list = [""]

    for index in range(len(mask)):
        for r in range(len(result_list)):
            if mask[index] == "0":
                result_list[r] += bin[index]
            elif mask[index] == "1":
                result_list[r] += "1"
            elif mask[index] == "X":
                result_list.append(result_list[r] + "1")
                result_list[r] += "0"

    return [toDeci(x, 2) for x in result_list]


def val_masked(mask, value):
    bin = fromDeci("", 2, value)
    # print(bin)
    bin = "0" * (len(mask) - len(bin)) + bin
    result = ""

    for index in range(len(mask)):
        result += mask[index] if mask[index] != "X" else bin[index]

    return toDeci(result, 2)


def main(inp):
    if inp == [""]:
        return None

    arr = [0] * 10000000
    mask = ""
    for line in inp:
        if line[:4] == "mask":
            mask = line[7:]
            # print("Mask:", mask)
        elif line[:3] == "mem":
            index = int(line.split("]")[0].split("[")[1])
            value = int(line.split("=")[1].rstrip())
            if index >= len(arr):
                return "error"
            arr[index] = val_masked(mask, value)

    sum = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            sum += arr[i]

    return sum


ut.aoc_check(main, __file__, [])
