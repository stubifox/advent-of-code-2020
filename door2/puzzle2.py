# --- Day 2: Password Philosophy ---

from requests import get
import re
cookie = {'session': '53616c7465645f5f7a1c0afee4d2e9fb72fcc3a32018d1c6a202919d538d6e88c75d8231785d0255862627b997e7744f'}
input = get('https://adventofcode.com/2020/day/2/input',
            cookies=cookie).content.decode('utf-8').replace(': ', ':')


class Constraints:
    minvalue: int = 0
    maxvalue: int = 0
    password: str = ''
    letter: str = ''

    def __init__(self, min, max, let, pw):
        self.minvalue = min
        self.maxvalue = max
        self.letter = let
        self.password = pw

    def get_dict(self):
        return {
            'min': int(self.minvalue),
            'max': int(self.maxvalue),
            'cha': self.letter,
            'pw': self.password
        }


def produce_readable():
    readable = []
    delimeters = '-, :'
    regex_pattern = '|'.join(map(re.escape, delimeters))
    readable_array = list(map(lambda x: re.split(
        regex_pattern, x.strip()), input.split("\n")))
    readable_array.pop()
    for [min, max, let, pw] in readable_array:
        readable.append(Constraints(min, max, let, pw).get_dict())
    return readable


def validate_1(min, max, cha, pw: str, counter=0):
    if len(pw) == 0:
        return counter >= min and counter <= max
    if counter > max:
        return False
    if pw[0] == cha:
        return validate_1(min, max, cha, pw[1:], counter + 1)
    return validate_1(min, max, cha, pw[1:], counter)


def solution_1():
    count = 0
    for entry in produce_readable():
        count += 1 if validate_1(**entry) == True else 0
    print(count)


solution_1()

# --- Part Two ---


def validate_2(min, max, cha, pw):
    return (pw[min-1] == cha) != (pw[max-1] == cha)


def solution_2():
    count = 0
    for entry in produce_readable():
        count += 1 if validate_2(**entry) == True else 0
    print(count)


solution_2()
