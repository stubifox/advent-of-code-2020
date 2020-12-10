import time
import sys
from requests import get
from pprint import pprint
from re import sub


def get_input():
    cookie = {'session': '53616c7465645f5f7a1c0afee4d2e9fb72fcc3a32018d1c6a202919d538d6e88c75d8231785d0255862627b997e7744f'}
    return get('https://adventofcode.com/2020/day/7/input', cookies=cookie).content.decode('utf-8').strip().split('\n')[:-1]


class Ruleset:
    type: str
    rule_set: list

    def __init__(self, sentence: str) -> None:
        self.type = sub('bag.*', '', sentence.split('contain')[0]).strip()
        self.rule_set = list(
            *map(lambda x: list(map(lambda y: self.__set_children(y), x.split(','))), sentence.split('contain')[1:]))

    def __set_children(self, params: str) -> dict:
        return {'amnt': int(params.strip()[:1]), 'type': sub('bag.*', '', params.strip()[1:].replace('.', '')).strip()} if params.strip()[0] != 'n' else {}


def define_rulesets(L=get_input()) -> list:
    if len(L) == 1:
        return [Ruleset(L[0]).__dict__]
    return [Ruleset(L[0]).__dict__] + define_rulesets(L[1:])


def is_dependent(entry, bag_sort: str = 'shiny gold') -> bool:
    return len(list(filter(lambda entry: entry['type'] == bag_sort, entry['rule_set']))) > 0


def get_entries_non_empty_rule_set() -> list:
    return list(filter(lambda entry: entry['rule_set'] != [{}], define_rulesets()))


def get_all_dependables_for_bag_sort(L=get_entries_non_empty_rule_set(), bag_sort: str = 'shiny gold'):
    return list(map(lambda entry: entry['type'], list(filter(lambda x: list(filter(
        lambda y: y['type'] == bag_sort, x['rule_set'])), get_entries_non_empty_rule_set()))))


def get_deepsearch_bags(searched: set = [], default_bag_type: str = 'shiny gold', idx: int = -1):
    if default_bag_type in searched and idx >= len(searched) - 1:
        return searched
    searched += list(filter(lambda x: x not in searched,
                            get_all_dependables_for_bag_sort(bag_sort=default_bag_type)))
    return get_deepsearch_bags(searched=searched, default_bag_type=searched[idx], idx=idx + 1)


print(len(get_deepsearch_bags()))

# --- Part Two ---
