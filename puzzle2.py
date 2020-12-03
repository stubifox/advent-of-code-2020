'''
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
'''
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

'''
The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
'''


def validate_2(min, max, cha, pw):
    return (pw[min-1] == cha) != (pw[max-1] == cha)


def solution_2():
    count = 0
    for entry in produce_readable():
        count += 1 if validate_2(**entry) == True else 0
    print(count)


solution_2()
