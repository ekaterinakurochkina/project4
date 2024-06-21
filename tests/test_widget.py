import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize(
    "account_card, mask_account_card",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("abcdefghigklmnopqrstuvwxwz", "None"),
    ],
)
def test_mask_account_card(account_card, expected):
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize(
    "data, get_data",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("", ""),
    ],
)
def test_get_data(data, expected):
    assert get_data(data) == expected
