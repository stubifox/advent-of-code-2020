# --- Day 3: Toboggan Trajectory ---

from requests import get
from pprint import pprint
cookie = {'session': '53616c7465645f5f7a1c0afee4d2e9fb72fcc3a32018d1c6a202919d538d6e88c75d8231785d0255862627b997e7744f'}


def get_input():
    return get('https://adventofcode.com/2020/day/3/input', cookies=cookie).content.decode('utf-8')


def parse_input():
    puzzle_input = get_input()
    return list(map(lambda x: [replace_char(p) for p in x], puzzle_input.split('\n')))


# parse_input()
def replace_char(char):
    return 0 if char == '.' else 1


def check_tree_encounters(xs, ys):
    count = 0
    x_step, y_step = xs, ys
    value_list = parse_input()
    value_list.pop()
    width = len(value_list[0])
    while y_step < len(value_list):
        count += value_list[y_step][x_step]
        x_step = (x_step + xs) % width
        y_step += ys
    return count


print(check_tree_encounters(3, 1))

# --- Part Two ---


slopes = [{'xs': 1, 'ys': 1},
          {'xs': 3, 'ys': 1},
          {'xs': 5, 'ys': 1},
          {'xs': 7, 'ys': 1},
          {'xs': 1, 'ys': 2}]


def product_of_slopes(slope):
    if len(slope) == 1:
        return check_tree_encounters(**slope[0])
    return check_tree_encounters(**slope[0]) * product_of_slopes(slope[1:])


print(product_of_slopes(slopes))
