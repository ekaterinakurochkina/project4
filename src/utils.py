import json
import logging
import sys
from pathlib import Path
from typing import List

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.сonfig import ROOT_PATH

# logger = logging.getLogger("utils")
# logger.setLevel(logging.INFO)
# file_handler = logging.FileHandler("../logs/utils.log", "w")
# file_formatted = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s")
# file_handler.setFormatter(file_formatted)
# logger.addHandler(file_handler)


def get_transactions(path_to_file: Path) -> List:
    """Функция, возвращающая из json-файла данные о транзакциях"""
    try:
        with open(path_to_file) as json_file:
            try:
                # logger.info(f"Открываем json-файл {path_to_file}")
                transactions = json.load(json_file)
                return transactions
            except json.JSONDecodeError:
                # logger.error("Ошибка декодирования JSON")
                print("Ошибка декодирования JSON")
                return []
    except FileNotFoundError:
        # logger.error("Файл не найден")
        print("Файл не найден")
        return []


# Проверка кода
# path_to_file = Path(ROOT_PATH, "../data/operations.json")
# transactions = get_transactions(path_to_file)
# print(get_transactions(Path(ROOT_PATH, "../data/operations.json")))
#
#
# print(type(get_transactions(Path(ROOT_PATH, "../data/operations.json"))))
