import re
from requests import get
import pprint


def get_puzzle_input() -> str:
    cookie = {'session': '53616c7465645f5f245849caa3252ad10010d871debd757e848333b617865d4f8218ece243cc20c9c6ae8357bb9e99f6'}
    return get('https://adventofcode.com/2020/day/4/input',
               cookies=cookie).content.decode('utf-8', 'strict').strip().split('\n\n')


def to_dict(s):
    return dict([x.split(':') for x in s.split()])


def get_arr_of_dict() -> str:
    pzz_input = get_puzzle_input()
    for idx, entry in enumerate(pzz_input):
        pzz_input[idx] = to_dict(entry)
    return pzz_input


def check_valid():
    count = 0
    for entry in get_arr_of_dict():
        if entry.get('cid'):
            entry.pop('cid')
        if len(entry) == 7:
            count += 1
    return count


print(check_valid())

validation_params = {
    'byr': }
