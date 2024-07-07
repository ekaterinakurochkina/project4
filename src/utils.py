from pathlib import Path
from src.сonfig import ROOT_PATH
from typing import List
import json


def get_transactions(path_to_file: Path) -> List:
    """Функция, возвращающая из json-файла данные о транзакциях"""
    try:
        with open(path_to_file) as json_file:
            try:
                transactions = json.load(json_file)
                return transactions
            except json.JSONDecodeError:
                print("Ошибка декодирования JSON")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []


path_to_file = Path(ROOT_PATH, "../data/operations.json")
transactions = get_transactions(path_to_file)

# print(get_transactions(Path(ROOT_PATH, "../data/operations.json")))
# print(type(get_transactions(Path(ROOT_PATH, "../data/operations.json"))))
