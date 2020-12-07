from pprint import pprint
from requests import get
from math import ceil


def get_input() -> list[str]:
    cookie = {'session': '53616c7465645f5f7a1c0afee4d2e9fb72fcc3a32018d1c6a202919d538d6e88c75d8231785d0255862627b997e7744f'}
    return get('https://adventofcode.com/2020/day/5/input', cookies=cookie).content.decode('utf-8').split('\n')[:-1]


def get_encoded_tickets(input=get_input()) -> list:
    if len(input) == 1:
        return [get_ticket_entry(input[0])]
    return [get_ticket_entry(input[0])] + get_encoded_tickets(input[1:])


def generic_get_param(bsp: str, x_range: tuple, lower_letter: str, name: str) -> dict:
    if len(bsp) == 0:
        return {name: x_range[0]} if bsp == lower_letter else {name: x_range[1]}
    if bsp[0] == lower_letter:
        return generic_get_param(bsp[1:], (x_range[0], (x_range[0] + x_range[1])//2), lower_letter, name)
    return generic_get_param(bsp[1:], ((x_range[0] + x_range[1])//2, x_range[1]), lower_letter, name)


def get_ticket_entry(bsp) -> dict:
    row = generic_get_param(bsp[:7], (0, 127), 'F', 'row')
    column = generic_get_param(bsp[-3:], (0, 7), 'L', 'column')
    seat_id = row['row'] * 8 + column['column']
    return {**row, **column, 'seat_id': seat_id}


def get_highest_id() -> int:
    return max(get_encoded_tickets(), key=lambda x: x['seat_id'])['seat_id']


print(get_highest_id())
pprint(get_encoded_tickets())

# --- Part Two ---


# def my_id():
