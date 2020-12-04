# --- Day 1: Report Repair ---
import itertools
import numpy
from requests import get
number_input = get('https://adventofcode.com/2020/day/1/input',
                   cookies={'session': '53616c7465645f5f7a1c0afee4d2e9fb72fcc3a32018d1c6a202919d538d6e88c75d8231785d0255862627b997e7744f'}).content.decode('utf-8').split('\n')
number_input.pop()
L = list(map(lambda x: int(x), number_input))


def adds_to_2020(L):
    numbers = list(set(L))
    possibilities = []
    for idx, x in enumerate(numbers):
        for y in numbers[idx:]:
            if x + y == 2020:
                possibilities += [[x, y]]
    return possibilities


def results():
    for [a, b] in adds_to_2020(L):
        print(a * b)


results()
# --- Part Two ---


def three_addup2020():
    possibilities = []
    for (a, b, c) in list(itertools.combinations(list(set(L)), 3)):
        if a + b + c == 2020:
            possibilities += [[a, b, c]]
    return possibilities


def three_results():
    for [a, b, c] in three_addup2020():
        print(a * b * c)


three_results()


# generic nesting:
# with number to add to, count of numbers n and List L


def generic_adding_up_number(number, n, L):
    combinations = list(itertools.combinations(list(set(L)), n))
    sums = list(filter(lambda x: sum(list(x)) == number, combinations))
    return list(map(lambda x: numpy.prod(list(x)), sums))
