import re
from typing import Dict
from typing import List
import json
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.сonfig  import ROOT_PATH
from src.utils import get_transactions


def search(transactions: list[Dict], search_data)-> list[Dict]:
    """Функция поиска транзакции по описанию"""
    search_data = "Открытие вклада"
    result =[]
    for transaction in transactions:
        search_result = re.search(search_data, transaction["description"], flags=0)
        if search_result != None:
            result.append(transaction)

    return result


# Проверка кода
path_to_file = Path(ROOT_PATH, "../data/operations.json")
transactions = get_transactions(path_to_file)
search_data = "Открытие вклада"
print(search(transactions, search_data))
