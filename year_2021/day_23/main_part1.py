#!/usr/bin/env python
import os, sys

sys.path.append(os.getcwd())
import util as ut

__version__ = "1.0.0"


def check_finished(node_set):
    if (
        node_set[2][3] == "A"
        and node_set[3][3] == "A"
        and node_set[2][5] == "B"
        and node_set[3][5] == "B"
        and node_set[2][7] == "C"
        and node_set[3][7] == "C"
        and node_set[2][9] == "D"
        and node_set[3][9] == "D"
    ):
        return True
    return False


def find_targets(field, a, b):
    valid_coords = []
    steps = set()
    steps.add((a, b, 0))
    steps_taken = set()
    while steps:
        (s1, s2, s_cost) = steps.pop()
        steps_taken.add((s1, s2))
        for y in [(s1 + m, s2 + n, s_cost + cost[field[a][b]]) for (m, n) in coords]:
            x = (y[0], y[1])
            if x not in steps_taken and field[x[0]][x[1]] == ".":
                steps.add(y)
                if x not in forbidden:
                    valid_coords.append(y)
        # if field[s1][s2] == ".":
        #     # if (s1,s2) not in steps_taken: steps.add((s1,s2))
        #     if (s1,s2) not in forbidden:
        #         valid_coords.append((s1,s2,s_cost))
    # only move into rooms, once in the hallway

    # if in room -> move out of room
    # if in hallway -> move into correct room iff nothing only the correct letter is in there

    # a == 1 -> in hallway
    # only move into target room with only correct letters
    # a != 1 -> in room
    # only move into hallway, except forbidden positions
    result = set()
    for c, d, e in valid_coords:
        if a == 1:  # in hallway
            if (c, d) in targets[field[a][b]]:  # in correct room
                i = 0
                valid = True
                while (
                    True
                ):  # check if room is only used by correct type and if it is the lowest point
                    i += 1
                    if field[c + i][d] == field[a][b] or field[c + i][d] == ".":
                        continue
                    elif field[c + i][d] == "#":
                        break
                    else:
                        valid = False
                        break
                if valid:
                    result.add((c, d, e))
        else:  # in room
            if c == 1:  # into hallway
                if (a, b) not in targets[
                    field[a][b]
                ]:  # iff not already in correct room \ need possible check if theres place below
                    result.add((c, d, e))
            elif (
                c,
                d,
            ) in targets and c > a:  # move deeper into the room - should technically not happen?
                result.add((c, d, e))
    # valid_coords = [(c,d,e) for (c,d,e) in valid_coords if (a != 1 or c != 1) and (c != 2 or field[c+1][d] == field[a][b]) and (a != 1 or ((c,d) in targets[field[a][b]])) and (a == 1 or c == 1)]
    # return valid_coords
    return list(result)


def move_state(game_state):
    global counter, min_energy
    if check_finished(game_state[0]):
        min_energy = min(min_energy, game_state[1])
        mins.append(game_state[1])
        return
    print(
        "Game states:",
        counter,
        "Global min:",
        min_energy,
        "Local min:",
        game_state[1],
        "State:",
        *game_state[0][1:-1],
        "Queue:",
        len(queue),
        "Mins:",
        mins
    )
    field = game_state[0]
    field_as_string = "".join(field[1:-1])
    if field_as_string in visited_game_states or game_state[1] > min_energy:
        return
    else:
        visited_game_states[field_as_string] = game_state[1]
    counter += 1
    for a, b in existing_nodes:
        if field[a][b] in cost:
            # get all moves
            targets = find_targets(field, a, b)
            for a1, b1, c1 in targets:
                new_field = field.copy()  # copy.deepcopy(field)
                new_field[a1] = (
                    new_field[a1][:b1] + field[a][b] + new_field[a1][b1 + 1 :]
                )
                new_field[a] = new_field[a][:b] + "." + new_field[a][b + 1 :]
                new_energy = game_state[1] + c1

                new_field_as_string = "".join(new_field[1:-1])
                if (
                    not (new_field_as_string in visited_game_states)
                ) and new_energy < min_energy:  # or visited_game_states[new_field_as_string] > new_energy:
                    queue.append((new_field, new_energy, game_state[2] + 1))


def main(inp):
    if inp == [""]:
        return None

    global cost, coords, existing_nodes, min_energy, visited_game_states, start, counter, queue, forbidden, mins, targets
    cost = {"A": 1, "B": 10, "C": 100, "D": 1000}
    targets = {
        "A": [(2, 3), (3, 3)],
        "B": [(2, 5), (3, 5)],
        "C": [(2, 7), (3, 7)],
        "D": [(2, 9), (3, 9)],
    }
    forbidden = [(1, 3), (1, 5), (1, 7), (1, 9)]
    coords = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    existing_nodes = set()
    min_energy = float("inf")  #
    visited_game_states = {}
    counter = 0
    queue = []

    for a in range(len(inp)):
        for b in range(len(inp[a])):
            if (
                inp[a][b] == "."
                or inp[a][b] == "A"
                or inp[a][b] == "B"
                or inp[a][b] == "C"
                or inp[a][b] == "D"
            ):
                existing_nodes.add((a, b))

    mins = []
    low_cost = []
    queue.append((inp, 0, 0))
    # element: field, energy, heuristic
    while queue:
        # if low_cost:
        #     elem = low_cost.pop(0)
        #     move_state(elem)
        # else:
        max_elem = queue[0]
        for elem in queue:
            if elem[1] < max_elem[1]:
                # low_cost.append(max_elem)
                max_elem = elem
        prev_min = min_energy
        move_state(max_elem)
        queue.remove(max_elem)
        # max_val = queue[0][1]
        # max_elem = queue[0]
        # for elem in queue:
        #     val = elem[1]
        #     if val < max_val or (val == max_val and elem[1] < max_elem[1]):
        #         max_elem = elem
        #         max_val = val
        # prev_min = min_energy
        # move_state((max_elem[0], max_elem[1], max_elem[2]))
        # queue.remove(max_elem)
        if min_energy != prev_min:
            queue = [x for x in queue if x[1] < min_energy]

    return min_energy


ut.aoc_check(main, __file__, [])
