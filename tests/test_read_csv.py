from unittest.mock import patch
from src.read_csv import read_csv
import os
from unittest.mock import patch
from typing import Dict
from pathlib import Path
import csv
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.сonfig  import ROOT_PATH

path_to_file = Path(ROOT_PATH, "../data/transactions.csv")
@patch('csv.reader')
def test_read_csv(mock_reader):
  # Настраиваем mock_reader чтобы он возвращал нужный результат
  mock_reader.return_value = iter([
    ['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description'],
    ['650703', 'EXECUTED', '2023-09-05T11:30:32Z', '16210', 'SoL', 'PEN', 'Счет 58803664651298323391', 'Счет 39746506635466619397', 'Перевод организации']
  ])

  result = read_csv(path_to_file)
  expected_result = [
    {
      "id": "650703",
      "state": "EXECUTED",
      "date": "2023-09-05T11:30:32Z",
      "amount": "16210",
      "currency_name": "SoL",
      "currency_code": "PEN",
      "from": "Счет 58803664651298323391",
      "to": "Счет 39746506635466619397",
      "description": "Перевод организации"
    }
  ]
  assert result == expected_result