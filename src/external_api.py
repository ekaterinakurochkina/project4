import os
from dotenv import load_dotenv
import requests


# Загрузка переменных из .env-файла
load_dotenv()
api_key = os.getenv("API_KEY")


https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}
