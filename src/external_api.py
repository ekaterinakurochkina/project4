import os
from pathlib import Path
from mypyc.ir.ops import Float
from src.сonfig import ROOT_PATH
from dotenv import load_dotenv
import requests
from src.utils import get_transactions
from typing import Dict, Any

# Загрузка переменных из .env-файла
load_dotenv()
api_key = os.getenv("API_KEY")
url = "https://apilayer.com/exchangerates_data-api"
headers = {"apikey": api_key}
# def transaction_amount(transactions: Dict) -> float | Any:
#     """функция-генератор, которая принимает транзакцию и возвращает сумму транзакции"""
transactions = get_transactions(Path(ROOT_PATH, "../data/operations.json"))
for transaction in transactions:
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        result = float(transaction["operationAmount"]["amount"])
        # return float(transaction["operationAmount"]["amount"])
        # amount = transaction["operationAmount"]["amount"]
        # response = requests.get(url, headers=headers, to=to, from = from, amount = amount)
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    apikey = os.getenv("API_KEY")
    response = requests.get(
        f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={currency}&amount={amount}"
    )
    result = response.json()
    # return print(result)
    print(result)

    # {
    #     "id": 441945886,
    #     "state": "EXECUTED",
    #     "date": "2019-08-26T10:50:58.294041",
    #     "operationAmount": {
    #         "amount": "31957.58",
    #         "currency": {
    #             "name": "руб.",
    #             "code": "RUB"
    #         }
    #     },
    #     "description": "Перевод организации",
    #     "from": "Maestro 1596837868705199",
    #     "to": "Счет 64686473678894779589"
    # },
# def filter_by_currency(transactions, currency):
#     """функция-генератор, которая принимает список словарей с банковскими операциями
#     и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта"""
#     for transaction in transactions:
#         if transaction["operationAmount"]["currency"]["code"] == currency:
#             yield transaction
#
#
# def transaction_descriptions(transactions):
#     """генератор, который принимает список словарей и возвращает описание каждой операции по очереди"""
#     for transaction in transactions:
#         yield transaction["description"]
# fetch("https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}", requestOptions)
#   .then(response => response.text())
# https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}
# fetch("https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}", requestOptions)
#   .then(response => response.text())
#   .then(result => console.log(result))
#   .catch(error => console.log('error', error));
