from requests import get
from pprint import pprint


def get_input() -> list[str]:
    cookie = {'session': '53616c7465645f5f7a1c0afee4d2e9fb72fcc3a32018d1c6a202919d538d6e88c75d8231785d0255862627b997e7744f'}
    return get('https://adventofcode.com/2020/day/7/input', cookies=cookie).content.decode('utf-8').strip().split('\n')[:-1]


class Ruleset:
    type: str
    rule_set: list

    def __init__(self, sentence: str) -> None:
        self.type = sentence.split('contain')[0].strip()
        self.rule_set = list(
            *map(lambda x: list(map(lambda y: self.__set_children(y), x.split(','))), sentence.split('contain')[1:]))

    def __set_children(self, params: str) -> dict:
        return {'amnt': int(params.strip()[:1]), 'type': params.strip()[1:].strip()} if params.strip()[0] != 'n' else {}


def define_rulesets(L=get_input()) -> list(dict):
    if len(L) == 1:
        return [Ruleset(L[0]).__dict__]
    return [Ruleset(L[0]).__dict__] + define_rulesets(L[1:])



pprint(define_rulesets())
