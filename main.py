import re
from typing import Dict, List
from pathlib import Path
import sys
from numpy.core.multiarray import item
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.сonfig  import ROOT_PATH
from src.utils import get_transactions
from src.read_csv import read_csv
from src.read_excel import read_excel
from collections import defaultdict
from collections import Counter



greetings = """Привет!\nДобро пожаловать в программу работы с банковскими транзакциями. 

Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
# def main():
#     """Функция, отвечающая за основную логику проекта и связывает
#     функциональности между собой"""
print(greetings)
while True:
    user_format = input("Введите номер пункта меню и нажмите 'ввод': ")
    if user_format == "1":
        print("Для обработки выбран JSON-файл.")
        transactions = get_transactions(Path(ROOT_PATH, "../data/operations.json"))
    elif user_format == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = read_csv(Path(ROOT_PATH, "../data/transactions.csv"))
    elif user_format == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions = read_excel(Path(ROOT_PATH, "../data/transactions_excel.xlsx"))
    else:
        print("Ошибка. Введите корректный номер пункта меню")
        continue
