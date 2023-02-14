#!/usr/bin/env python
from typing import Optional, Union, Callable
import time, os, filecmp

# region timers
timers = {}


def start_timer(name: Optional[str], precise: bool = False):
    """
    Start a timer with default precision (second) or increased precision (nanoseconds).
    Returns the name of the created timer.
    """
    if name:
        name = "timer_{}{}".format(name, "_ns" if precise else "_s")
    else:  # find available name
        for i in range(1000):
            if (temp := "timer_{}{}".format(i, "_ns" if precise else "_s")) in timers:
                continue
            else:
                name = temp
                break
        raise ValueError("No viable timer name found.")

    timers[name] = time.perf_counter_ns() if precise else time.perf_counter()
    return name


def get_timer(name: str) -> Union[float, int]:
    """Return time between now and the most recent start of timer [name]."""
    if name not in timers:
        raise ValueError(f"Timer '{name}' not found/started.")
    if name.endswith("_ns"):
        return time.perf_counter_ns() - timers[name]
    elif name.endswith("_s"):
        return time.perf_counter() - timers[name]
    else:
        raise ValueError(f"Timer '{name}' has incorrect precision.")


# endregion timers


def copy_from_template(dest_name: str, src_name: str) -> bool:
    if os.path.isfile(dest_name):
        return False
    else:
        with open(dest_name, "w") as file:
            with open(src_name, "r") as template_file:
                for line in template_file:
                    file.write(line)
        return True


# region aoc
AOC_TEMPLATE_PY = os.path.join(os.getcwd(), "template.py")
AOC_TEMPLATE_TXT = os.path.join(os.getcwd(), "template.txt")


def aoc_create_year(year: int) -> None:
    # create year_{year} directory
    directory_year = os.path.join(os.getcwd(), f"year_{year:04d}")
    if not os.path.isdir(directory_year):
        os.makedirs(directory_year)

    # create day_{day} directories
    for day in range(1, 26):
        directory_day = os.path.join(directory_year, f"day_{day:02d}")
        if not os.path.isdir(directory_day):
            os.makedirs(directory_day)

        # create python file from template
        for part in range(1, 3):
            py_file = os.path.join(directory_day, f"main_part{part}.py")
            copy_from_template(py_file, AOC_TEMPLATE_PY)

        # create input file from template
        puzzle_file = os.path.join(directory_day, f"puzzle_input.txt")
        copy_from_template(puzzle_file, AOC_TEMPLATE_TXT)
        aoc_create_example_txt(year, day, 1)


def aoc_create_example_txt(year: int, day: int, count: int):
    # create {count} number of new input files with next available name
    for _ in range(count):
        for i in range(1000):
            txt_file = os.path.join(
                os.getcwd(), f"year_{year:04d}", f"day_{day:02d}", f"example_{i}.txt"
            )
            if copy_from_template(txt_file, AOC_TEMPLATE_TXT):
                break


def aoc_remove_unused_files():
    for path, directories, files in os.walk(os.getcwd()):
        for file in files:
            file_type = file.split(".")[-1]
            if file_type not in ["py", "txt"] or "template" in file:
                continue
            if filecmp.cmp(
                os.path.join(path, file),
                os.path.join(os.getcwd(), f"template.{file_type}"),
            ):
                os.remove(os.path.join(path, file))

    # remove empty folders
    for path, _, _ in os.walk(os.getcwd(), topdown=False):
        if len(os.listdir(path)) == 0:
            os.rmdir(path)


def __compile_input(file: str):
    with open(file, "r") as f:
        lines = f.readlines()
        if lines and lines[-1].startswith("exp_val="):
            expected_result_input = lines[-1].split("=")[1]
            if "," in expected_result_input:
                temp = expected_result_input.split(", ")
                expected_result = (
                    __parse_expected_value(temp[0]),
                    __parse_expected_value(temp[1]),
                )
            else:
                expected_result = __parse_expected_value(expected_result_input)

        else:
            raise ValueError(f"Missing 'expected_value=' in input file '{file}'.")
        return [l.rstrip("\n") for l in lines[:-1]], expected_result


def __parse_expected_value(value: str):
    if value.isdigit():
        return int(value)
    elif value in ["None", "none"]:
        return None
    else:
        return value


def aoc_check(
    func: Callable,
    file: str,
    input_file_indices: list[str],
    remove_blanks=False,
    ignore_result: bool = False,
):
    input_files = [
        os.path.join(os.path.split(file)[0], f"example_{ind}.txt")
        for ind in input_file_indices
    ]
    input_files += [os.path.join(os.path.split(file)[0], "puzzle_input.txt")]
    for input_file in input_files:
        puzzle_input, expected_value = __compile_input(input_file)
        if remove_blanks:
            puzzle_input = [p for p in puzzle_input if p != ""]
        if type(expected_value) == tuple:
            expected_value = expected_value[int(file[-4]) - 1]
        computation_timer = start_timer("computation")
        computation_result = func(puzzle_input)
        if computation_result == expected_value:
            print(f"'{input_file}' passed with value '{computation_result}'.")
            print(f"Time: {get_timer(computation_timer):.3g} seconds.\n")
        else:
            print(
                f"'{input_file}' failed with value '{computation_result}' instead of '{expected_value}'."
            )
            print(f"Time: {get_timer(computation_timer):.3g} seconds.\n")
            if not ignore_result:
                break


def aoc_check_all():
    from subprocess import Popen, PIPE

    jobs = []

    for path, _, files in os.walk(os.getcwd()):
        for file in files:
            if "main_part" in file:
                jobs.append(os.path.join(path, file))

    results = [Popen([j], stdout=PIPE, stderr=PIPE, shell=True) for j in jobs]
    outputs = []
    import subprocess

    for r in results:
        try:
            outputs.append(str(r.communicate(timeout=5)[0]))
        except subprocess.TimeoutExpired:
            pass

    for o in outputs:
        if o == "b''":
            continue
        i1 = o.index("year_")
        year = o[i1 + 5 : i1 + 9]
        i2 = o.index("day_")
        day = o[i2 + 4 : i2 + 6]
        i3 = o.index("Time: ")
        time = o[i3 + 6 : o.find(" seconds")]

        if "failed" in o or float(time) > 1:
            print(f"year {year} day {day} time {time}")


# endregion aoc


# region helper
def slice_list(lst, lengths=[1], leave_out=0):
    result = []
    i, x = 0, 0
    while True:
        if i - 1 > len(lst):
            break
        jump_length = lengths[x]
        result.append(lst[i : i + jump_length])
        i += jump_length + leave_out
        x = (x + 1) % len(lengths)
    return result


def __toDeci_val(c):
    if c >= "0" and c <= "9":
        return ord(c) - ord("0")
    else:
        return ord(c) - ord("A") + 10


def toDeci(base, sstr):
    llen = len(sstr)
    power = 1
    num = 0
    for i in range(llen - 1, -1, -1):
        if __toDeci_val(sstr[i]) >= base:
            print("Invalid Number")
            return -1
        num += __toDeci_val(sstr[i]) * power
        power = power * base
    return num


# endregion helper

if __name__ == "__main__":
    # aoc_remove_unused_files()
    # for year in range(2015, 2023):
    #     aoc_create_year(year)
    aoc_check_all()
    pass
