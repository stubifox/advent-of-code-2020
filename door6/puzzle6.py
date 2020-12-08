# --- Day 6: Custom Customs ---

from requests import get


def get_input() -> list:
    cookie = {'session': '53616c7465645f5f7a1c0afee4d2e9fb72fcc3a32018d1c6a202919d538d6e88c75d8231785d0255862627b997e7744f'}
    return get('https://adventofcode.com/2020/day/6/input',
               cookies=cookie).content.decode('utf-8').split('\n\n')


def convert_to_set(L) -> list(set):
    return list(map(lambda x: {c for c in x if c != '\n'}, L))


def sum_of_sets(S=convert_to_set(get_input())) -> int:
    if len(S) == 1:
        return len(S[0])
    return len(S[0]) + sum_of_sets(S[1:])


print(sum_of_sets())

# --- Part Two ---


def convert_to_set_p2() -> list(set):
    return list(map(lambda l: intersection_of_sets_in_list(convert_to_set(l)), [x.strip().split('\n') for x in get_input()]))


def intersection_of_sets_in_list(L) -> set:
    if len(L) == 1:
        return L[0]
    return L[0] & intersection_of_sets_in_list(L[1:])


print(sum_of_sets(convert_to_set_p2()))
