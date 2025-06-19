import os

import requests
from dotenv import load_dotenv

# from src.utils import operations_transform
# import json


def exchange_currency(transaction: dict):
    """
    Функция, которая принимает на вход транзакцию(в качестве аргумента словарь из списка словарей
    из файла operations.json), результат работы функции operations_transform() c указанием индекса
    конкретной транзакции и возвращает сумму транзакции (amount) в рублях,
    тип данных — float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для
    получения текущего курса валют и конвертации суммы операции в рубли.
    """
    if "RUB" == transaction["operationAmount"]["currency"]["code"]:
        return float(transaction["operationAmount"]["amount"])
    else:
        url = "https://api.apilayer.com/exchangerates_data/convert"

        payload = {
            "amount": transaction["operationAmount"]["amount"],
            "from": transaction["operationAmount"]["currency"]["code"],
            "to": "RUB",
        }
        load_dotenv()
        api_key = os.getenv("API_KEY")

        headers = {"apikey": api_key}

        response = requests.get(url, headers=headers, params=payload)

        # status_code = response.status_code
        result = response.json()
        # result_dict = json.loads(result)

        return round(float(result["result"]), 2)
        # return response


# trans = operations_transform("../data/operations.json")[0]
# print(exchange_currency(trans))
