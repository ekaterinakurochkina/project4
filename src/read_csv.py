from typing import List
from pathlib import Path
import csv
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.сonfig import ROOT_PATH


def read_csv(path_to_file: Path) -> List:
    """Функция чтения транзакций из csv-файла"""
    try:
        with open(path_to_file, "r", encoding="utf-8") as csv_file:
            try:
                reader = csv.reader(csv_file, delimiter=";")
                header = next(reader)
                result = []
                for row in reader:
                    dict_row = {
                        "id": row[header.index("id")],
                        "state": row[header.index("state")],
                        "date": row[header.index("date")],
                        "operationAmount": {
                            "amount": row[header.index("amount")],
                            "currency": {
                                "name": row[header.index("currency_name")],
                                "code": row[header.index("currency_code")],
                            },
                        },
                        "description": row[header.index("description")],
                        "from": row[header.index("from")],
                        "to": row[header.index("to")],
                    }
                    result.append(dict_row)
                    return result
            except Exception:
                print("Ошибка чтения csv")
                return []
    except Exception:
        print("Файл не найден")
        return []


# Проверка кода
path_to_file = Path(ROOT_PATH, "../data/transactions.csv")
print(read_csv(Path(ROOT_PATH, "../data/transactions.csv")))
