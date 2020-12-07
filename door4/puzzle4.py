# --- Day 4: Passport Processing ---

import re
from requests import get


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


def get_count_and_valid_entries():
    count = 0
    valid_entries = []
    for entry in get_arr_of_dict():
        if entry.get('cid'):
            entry.pop('cid')
        if len(entry) == 7:
            valid_entries.append(entry)
            count += 1
    return count, valid_entries


print(get_count_and_valid_entries()[0])

# --- Part Two ---

validation_params = {
    'byr': '(19[2-9]|200[0-2])',
    'iyr': '(201[0-9]|2020)',
    'eyr': '(202[0-9]|2030)',
    'hgt': '^(1[5-8][0-9]|19[0-3])\s?cm$|^(59|6[0-9]|7[0-6])\s?in$',
    'hcl': '^#(\d|[a-f]){6}$',
    'ecl': '^(amb|blu|brn|gry|grn|hzl|oth)$',
    'pid': '^[0-9]{9}$',
    'cid': '(.*?)'
}


def check_with_valid_params():
    count = 0
    _, valid_entries = get_count_and_valid_entries()
    for entry in valid_entries:
        count += 1 if is_matching(entry) else 0
    return count


def is_matching(entry):
    for key, value in entry.items():
        if not bool(re.match(validation_params[key], value)):
            return False
    return True


print(check_with_valid_params())
