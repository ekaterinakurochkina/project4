import os
from pathlib import Path
# from mypyc.ir.ops import Float

import src.utils
from src.сonfig import ROOT_PATH
from dotenv import load_dotenv
import requests
from src.utils import get_transactions
from typing import Dict, Any


# Загрузка переменных из .env-файла
load_dotenv()
api_key = os.getenv("API_KEY")


def transaction_amount(transactions: Dict) -> float | Any:
    """функция, которая принимает транзакцию и возвращает сумму транзакции"""
    transactions = src.utils.get_transactions(Path(ROOT_PATH, "../data/operations.json"))
    transaction = transactions[1]
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={currency}&amount={amount}"
    headers = {"apikey": api_key}
    response = requests.request("GET", url, headers=headers)
    result: Any = response.json()
    return result["result"]


print(transaction_amount(get_transactions))
