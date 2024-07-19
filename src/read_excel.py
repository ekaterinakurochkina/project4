import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.сonfig import ROOT_PATH


def read_excel(path_to_file: Path) -> list:
    """Функция чтения транзакций из excel-файла"""
    with open(path_to_file, "r", encoding="utf-8") as excel_file:
        try:
            df = pd.read_excel(path_to_file)
            # df = my_df.astype(float)
            transactions = []
            for i in range(0, len(df)):
                row_dict = {
                    "id": df.loc[i, "id"],
                    "date": df.loc[i, "date"],
                    "state": df.loc[i, "state"],
                    "operationAmount": {
                        "amount": df.loc[i, "amount"],
                        "currency": {
                            "name": df.loc[i, "currency_name"],
                            "code": df.loc[i, "currency_code"],
                        },
                    },
                    "description": df.loc[i, "description"],
                    "from": df.loc[i, "from"],
                    "to": df.loc[i, "to"],
                }
                transactions.append(row_dict)
            return transactions
        except Exception:
            print("Ошибка чтения excel")
            return []


# if __name__ == "__main__":
#     path_to_file = Path(ROOT_PATH, "../data/transactions_excel.xlsx")
#     print(read_excel(Path(ROOT_PATH, "../data/transactions_excel.xlsx")))


# Проверка кода
# path_to_file = Path(ROOT_PATH, "../data/transactions_excel.xlsx")
# print(read_excel(Path(ROOT_PATH, "../data/transactions_excel.xlsx")))

# def reader_file_transaction_excel(file: str) -> list[dict]:
#     """Функция считывающая файл в формате excel и возвращающая список словарей"""
#     df = pd.read_excel(file)  # читаем из экселя в DataFrame
#     result = []
#     rows_count = len(df)  # Получение количества строк в DataFrame
#     for i in range(0, rows_count):
#         row_dict = {
#             "id": df.at[i, "id"],
#             "state": df.at[i, "state"],
#             "date": df.at[i, "date"],
#             "operationAmount": {
#                 "amount": df.at[i, "amount"],
#                 "currency": {
#                     "name": df.at[i, "currency_name"],
#                     "code": df.at[i, "currency_code"],
#                 },
#             },
#             "description": df.at[i, "description"],
#             "from": df.at[i, "from"],
#             "to": df.at[i, "to"],
#         }
#         result.append(row_dict)
#     return result
#
#
# if __name__ == "__main__":
#     result = reader_file_transaction_excel("..\\data\\transactions_excel.xlsx")
#     print(result)
