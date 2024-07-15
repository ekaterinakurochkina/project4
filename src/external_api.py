import os
from pathlib import Path

import src.utils
from src.сonfig import ROOT_PATH
from dotenv import load_dotenv
import requests
from src.utils import get_transactions
from typing import Dict, Any


# Загрузка переменных из .env-файла
load_dotenv()
api_key = os.getenv("API_KEY")


def transaction_amount(transaction: Dict) -> float | Any:
    """функция, которая принимает транзакцию и возвращает сумму транзакции"""
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={currency}&amount={amount}"
    headers = {"apikey": api_key}
    response = requests.request("GET", url, headers=headers)
    result: Any = response.json()
    return result["result"]

# Проверка работы кода
transactions = src.utils.get_transactions(Path(ROOT_PATH, "../data/operations.json"))

transaction = {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
print(transaction_amount(transaction))
