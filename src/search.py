import re
from typing import Dict, List
from pathlib import Path
import sys
from numpy.core.multiarray import item
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.сonfig  import ROOT_PATH
from src.utils import get_transactions
from collections import defaultdict
from collections import Counter

# готовый код!
# def search(transactions: list[Dict], search_data)-> list[Dict]:
#     """Функция поиска транзакции по описанию"""
#     result = []
#     search_data = "Открытие вклада"
#     for transaction in transactions:
#         my_dict = defaultdict(list)
#         if transaction == {}:
#             continue
#         if re.search(search_data, transaction["description"], flags=0):
#             result.append(transaction)
#     return result


# Проверка кода
# path_to_file = Path(ROOT_PATH, "../data/operations.json")
# transactions = get_transactions(path_to_file)
# print(search(transactions, ""))

# -----------------------------------


def category_search(transactions: list[Dict])-> Dict:
    """Функция, подсчитывающая кол-во операций в каждой категории"""
    category_transactions = []
    for transaction in transactions:
        category = transaction.get("description")
        category_transactions.append(category)
    counted = Counter(category_transactions)
    if counted[None]:
        del counted[None]
    return counted

# Проверка кода
path_to_file = Path(ROOT_PATH, "../data/operations.json")
transactions = get_transactions(path_to_file)
print(category_search(transactions))
