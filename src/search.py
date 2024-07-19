import re
import sys
from pathlib import Path
from typing import Dict, List

sys.path.append(str(Path(__file__).resolve().parent.parent))
from collections import Counter, defaultdict

from src.utils import get_transactions
from src.сonfig import ROOT_PATH


def search(transactions: list[Dict], search_data) -> list[Dict]:
    """Функция поиска транзакции по описанию"""
    result = []
    for transaction in transactions:
        my_dict = defaultdict(list)
        if transaction == {}:
            continue
        if re.search(search_data, transaction["description"], re.IGNORECASE):
            result.append(transaction)
    return result


# Проверка кода
# path_to_file = Path(ROOT_PATH, "../data/operations.json")
# transactions = get_transactions(path_to_file)
# print(search(transactions, "открытие вклада"))


def category_search(transactions: list[Dict], category_transactions: List) -> Dict:
    """Функция, подсчитывающая кол-во операций в каждой категории"""
    # category_transactions = []
    # for transaction in transactions:
    #     category = transaction.get(category_transactions)
    #     category_transactions.append(category)
    counted = Counter(category_transactions)
    if counted[None]:
        del counted[None]
    return counted


# Проверка кода
# path_to_file = Path(ROOT_PATH, "../data/operations.json")
# transactions = get_transactions(path_to_file)
# category_transactions = ["Перевод организации", "Открытие вклада", "Перевод со счета на счет", "Перевод с карты на карту"]
# print(category_search(transactions, category_transactions))
