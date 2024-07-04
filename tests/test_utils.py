import pytest
import json
from unittest.mock import patch
from src.utils import get_transactions

@patch('json.load')
def test_get_transactions(mock_transactions):
    mock_transactions.return_value = [5, 5]
    assert get_transactions(mock_transactions) == [5, 5]
    mock_transactions.assert_called_once_with([5, 5])



