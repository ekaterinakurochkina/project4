import pytest
import json
from unittest.mock import patch
from src.utils import get_transactions


def test_get_transactions():
    with patch ("builtins.open") as mock_open:
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = json.dumps(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58","currency": {"name": "руб.","code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        assert get_transactions("../data/operations.json")=={
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }



    # mock_transactions.return_value = [5, 5]
    # assert get_transactions(mock_transactions) == [5, 5]
    # mock_transactions.assert_called_once_with([5, 5])
