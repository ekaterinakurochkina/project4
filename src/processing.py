import re
from collections import Counter, defaultdict
from typing import Dict, List


def filter_by_state(transactions: List[Dict], key_dict: str = "") -> List[Dict]:
    """Функция фильтрации операций по ключу"""
    filtered_list = []
    for i in range(len(transactions)):
        if str(transactions[i].get("state")).upper() == str(key_dict).upper():
            filtered_list.append(transactions[i])
    # print(f" фильтрация по статусу {filtered_list}")
    return filtered_list


def sort_by_date(transactions: list[Dict], ascending: bool = True) -> list[Dict]:
    """Функция сортировки операций по убыванию даты"""
    # Находим в транзакциях значения даты:
    # for transaction in transactions:
    #     if transaction.get("date") is None:
    #         pattern = re.compile(r'\d{4}-\d{2}-\w{5}:\d{2}')
    #         matches = pattern.search(transaction)
    #         for value in transaction.values():
    #             if value == matches:
    #                 transaction["date"] = value
    for transaction in transactions:
        if transaction.get("date") is None:
            sort_dict = transactions
            return sort_dict
        else:
            sort_dict = sorted(transactions, key=lambda x: x["date"], reverse=ascending)
    return sort_dict


# """Проверка работы кода"""
# transactions = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
# key_dict = "EXECUTED"
# # key_dict = "CANCELED"
# print(filter_by_state(transactions, key_dict))


# print(sort_by_date(transactions, ascending = False))
