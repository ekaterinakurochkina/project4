from unittest.mock import patch
from src.external_api import transaction_amount


@patch("requests.get")
def test_transaction_amount(mock_get):
    mock_get.return_value.json.return_value = {"result": 722707.849876}
    assert (
        transaction_amount(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        == 722707.849876
    )
