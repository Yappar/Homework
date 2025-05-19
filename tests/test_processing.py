import pytest

from src.masks import get_mask_account
from src.processing import filter_by_state, sort_by_date



@pytest.mark.parametrize("list_of_dict, state, expected", [
([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], "EXECUTED",
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], "CANCELED",
    [{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]),
([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], "INVALID_STATE",
    "Введены некорректные данные"),
([{'id': 41428829, 'state': '', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 615064591, 'state': '', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': '', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 939719570, 'state': '', 'date': '2018-06-30T02:08:58.425572'}], "EXECUTED",
    "Введены некорректные данные"),
([{'id': 41428829, 'date': '2019-07-03T18:35:29.512364'},
    {'id': 615064591,  'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'date': '2018-09-12T21:27:25.241689'},
    {'id': 939719570, 'date': '2018-06-30T02:08:58.425572'}], "EXECUTED",
    "Введены некорректные данные")])


def test_filter_by_state(list_of_dict:list, state:str, expected: list)-> None:
    assert filter_by_state(list_of_dict, state) == expected


def test_sort_by_date(list_of_dict: list, sort_p, expected):
    assert sort_by_date(list_of_dict, sort_p) == expected