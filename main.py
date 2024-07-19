import re
# from typing import Dict, List
from pathlib import Path
import sys
# from numpy.core.multiarray import item
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.сonfig  import ROOT_PATH
from src.utils import get_transactions
from src.read_csv import read_csv
from src.read_excel import read_excel
from src.processing import (sort_by_date, filter_by_state)
from src.search import search
from src.generators import filter_currency
from src.widget import (get_date, mask_account_card)
from src.masks import get_mask_account
# from collections import defaultdict
# from collections import Counter



greetings = """Привет!\nДобро пожаловать в программу работы с банковскими транзакциями. 

Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
def main():
    """Функция, отвечающая за основную логику проекта и связывает
    функциональности между собой"""
    print(greetings)

# пользователь выбирает формат файла, из которого загрузятся транзакции
    while True:
        user_format = input("Введите номер пункта меню и нажмите 'ввод': ")
        if user_format == "1":
            print("Для обработки выбран JSON-файл.")
            transactions = get_transactions(Path(ROOT_PATH, "../data/operations.json"))
            break
        elif user_format == "2":
            print("Для обработки выбран CSV-файл.")
            transactions = read_csv(Path(ROOT_PATH, "../data/transactions.csv"))
            break
        elif user_format == "3":
            print("Для обработки выбран XLSX-файл.")
            transactions = read_excel(Path(ROOT_PATH, "../data/transactions_excel.xlsx"))
            break
        else:
            print("Ошибка. Попробуйте еще раз.")
            continue

# Пользователь выбирает статус операции
    print("""Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    while True:
        user_status = input("Введите статус: ").upper()   #превращаем ввод пользователя в заглавные буквы
        if user_status in ["CANCELED", "PENDING", "EXECUTED"]:
            filtered_list = filter_by_state(transactions, key_dict = user_status)
            print(f"Операции отфильтрованы по статусу {user_status}")
            # print(f"фильтрация по статусу {filtered_list}")
            break
        else:
            print(f"Статус операции {user_status} недоступен.")
            filtered_list = transactions
            # print(f"фильтрация по статусу {filtered_list}")
            continue


# Дополнительные условия фильтрации транзакций

# Сортировка по дате
    while True:
            sort_date = input("Отсортировать операции по дате?\nВведите 'Да' или 'Нет': ").lower()
            if sort_date == "да":
                while True:
                    sort_date_to = input(
                        "Отсортировать по возрастанию или по убыванию?\nВведите 'по возрастанию' или 'по убыванию': "
                    ).lower()
                    if sort_date_to == "по возрастанию":
                        sort_dict = sort_by_date(filtered_list, ascending=False)
                        # print(f"фильтрация по возрастанию {sort_dict}")
                        break
                    elif sort_date_to == "по убыванию":
                        sort_dict = sort_by_date(filtered_list, ascending=True)
                        # print(f"фильтрация по убыванию {sort_dict}")
                        break
                    else:
                        print("Некорректный ввод. Пробуйте еще раз.")
                        continue
                break
            elif sort_date == "нет":
                sort_dict = filtered_list
                # print(f"без фильтрации по дате {sort_dict}")
                break
            else:
                print("Некорректный ввод. Пробуйте еще раз.")
                continue

    # return sort_dict

# Сортировка по валюте
    while True:
            sort_code = str(input("Выводить только рублевые транзакции? \nВведите 'Да' или 'Нет': ")).lower()
            if sort_code == "да":
                filtered_currency = filter_currency(sort_dict, "RUB")
                break
            elif sort_code == "нет":
                filtered_currency = sort_dict
                # print(f"фильтр по валюте {filtered_currency}")
                break
            else:
                print("Некорректный ввод. Пробуйте еще раз.")
                continue

    # Сортировка по пользовательскому запросу
    while True:
        user_input = input("Отфильтровать список транзакций по определенному слову в описании? Введите 'Да' или 'Нет':\n").lower()
        if user_input == "да":
            search_data = input("Введите слово для поиска: ").lower()
            result = search(filtered_currency, search_data)
            # print(f"фильтр пользователя {result}")
            # print(result)
            # list_transactions["description"] = search
            break
        elif user_input == "нет":
            result = filtered_currency
            # print(f"фильтр пользователя {result}")
            # print(result)
            break
        else:
            print("Некорректный ввод. Пробуйте еще раз.")
            continue

    # return result

    transactions = result
    if len(transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    p = print(f"Всего банковских операций в выборке: {len(transactions)}")
    for transaction in transactions:
        date = transaction["date"]
        transaction["date"] = get_date(date)

        account_card_from = str(transaction.get("from"))
        transaction["from"] = mask_account_card(account_card_from)

        account_card_to = str(transaction.get("to"))
        transaction["to"] = mask_account_card(account_card_to)

        print (f"{transaction["date"]} {transaction["description"]}")
        if transaction["from"] != None and transaction["to"] != None:
            print (f"{transaction["from"]} -> {transaction["to"]}")
            print(f"Сумма: {transaction["operationAmount"].get("amount")}")
        else:
            print(f"{transaction["to"]}")
            print(f"Сумма: {transaction["operationAmount"].get("amount")} {transaction["operationAmount"]["currency"].get("name")}")

    return p



    # description = transaction.get("description")
    # if description == "Открытие вклада":
    #     from_ = description
    # else:
    #     from_ = get_mask_card_number(transaction.get("from"))
    #
    # to_ = get_mask_card_number(transaction.get("to"))
    # date = get_data(transaction.get("date"))
    #
    #     amount = transaction["operationAmount"]["amount"]
    #     currency = transaction["operationAmount"]["currency"]["name"]
    #
    #     if description == "Открытие вклада":
    #         print(f"{date} {description}\nСчет {to_}\nСумма: {amount} {currency}\n")
    #     else:
    #         print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()