'''
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:
'''
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


'''
Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
What do you get if you multiply together the number of trees encountered on each of the listed slopes?
'''
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
