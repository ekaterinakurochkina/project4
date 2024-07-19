# # from asyncio import __main__
# from os import name
# import os
# from time import asctime
import logging
from typing import Union

# logger = logging.getLogger("masks")
# logger.setLevel(logging.INFO)
# file_handler = logging.FileHandler("../logs/masks.log", "w")
# file_formatted = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s")
# file_handler.setFormatter(file_formatted)
# logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> Union[str, None]:
    """Функция маскировки номера карты"""
    if card_number.isdigit() and len(card_number) == 16:
        # logger.info(f"Производим маскировку номера карты {card_number}")
        masks_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
        return masks_card
    else:
        # logger.error("Ошибка")
        return None


def get_mask_account(account: str) -> Union[str, None]:
    """Функция маскировки номера счета"""
    if account.isdigit() and len(account) == 20:
        # logger.info(f"Производим маскировку номера счета {account}")
        masks_account = f"**{account[-4::]}"
        return masks_account
    else:
        # logger.error("Ошибка")
        return None


def mask_account_card(account_card: str) -> Union[str, None]:
    """Функция маскировки номера карты или номера счета"""
    numeral = account_card[-20:]
    if numeral.isdigit():  # account_card[:3] == "Счет" and
        account = str(numeral)
        return f"{account_card[0:-20]} {get_mask_account(account)}"
    else:
        card_number = str(account_card[-16:])
        return f"{account_card[0:-16]} {get_mask_card_number(card_number)}"


# Проверка выполнения кода


# American Express 2932525563014117
# Счет 96692813169753520384
# Mastercard 5612504218607911
# account_card_1 = "Maestro1234567812345678"
# account_card_2 = "Счет12345678901234567890"
# account_card_3 = "American Express 2932525563014117"
# #
# #
# result_3 = print(mask_account_card(account_card_1))
# result_4 = print(mask_account_card(account_card_2))
# result_5 = print(mask_account_card(account_card_3))
