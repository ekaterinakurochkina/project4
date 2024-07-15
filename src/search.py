import re
from typing import Dict, List
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.сonfig  import ROOT_PATH
from src.utils import get_transactions
from collections import defaultdict


def search(transactions: list[Dict], search_data)-> list[Dict]:
    """Функция поиска транзакции по описанию"""
    result = []
    search_data = "Открытие вклада"
    for transaction in transactions:
        my_dict = defaultdict(list)
        if transaction == {}:
            continue
        if re.search(search_data, transaction["description"], flags=0):
            result.append(transaction)
    return result


# Проверка кода
# path_to_file = Path(ROOT_PATH, "../data/operations.json")
# transactions = get_transactions(path_to_file)
# print(search(transactions, ""))




# def category_search(transactions: list[Dict], search_data: List)-> list[Dict]:
#     """Функция, подсчитывающая кол-во операций в каждой категории"""
#     result = []
#     search_data = ""
#     for transaction in transactions:
#         print(transaction["description"])




# Определяем функцию для значений по умолчанию
# def default_value():
#     return 'неизвестно'
#
# # Создаем defaultdict с функцией по умолчанию
# my_dict = defaultdict(default_value)
# # Выводим значение для отсутствующего ключа
# print(my_dict['two'])




