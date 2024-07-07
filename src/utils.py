from pathlib import Path
from src.сonfig import ROOT_PATH
from typing import List
import json


def get_transactions(operations: Path) -> List:
    """Функция, возвращающая из json-файла данные о транзакциях"""
    filename = Path(ROOT_PATH, "../data/operations.json")
    with open(Path(ROOT_PATH, filename)) as json_file:
        try:
            transactions = json.load(json_file)
            return transactions
        except:
            return []


# print(get_transactions(Path(ROOT_PATH, "../data/operations.json")))
# print(type(get_transactions(Path(ROOT_PATH, "../data/operations.json"))))
