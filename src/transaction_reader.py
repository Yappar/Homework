import pandas as pd
import openpyxl
import csv

from src.decorators import log

# @log(filename='../data/logs/tran_reader.log')
def read_func_CSV(file_path: str) -> list[dict]:
    """
    Функция принимает файл CSV и возвращает список словарей
    заголовок (id;state;date;amount;currency_name;currency_code;from;to;description)
    """
    transact_list = []
    with open(file_path) as f:
        reader = csv.DictReader(f, delimiter= ';')
        for row in reader:
            my_dict = {"id": row['id'], "state": row["state"], "date": row["date"],
                       "amount": row["amount"], "currency_name": row["currency_name"],
                       "currency_code": row["currency_code"], "from": row["from"], "to": row["to"],
                       "description": row["description"]}
            transact_list.append(my_dict)
    print(transact_list)
    return transact_list

# @log(filename="../data/logs/tran_reader.log")
def read_func_Excel(file_path:str) -> list[dict]:
    """ Функция принимает файл Excel и возвращает список словарей"""
    try:
        with open(file_path):
            df = pd.read_excel(file_path)
            # Загружаем Excel-файл в DataFrame
            dict_list = df.to_dict(orient='records')
            # Преобразуем DataFrame в список словарей
            # «list» — ключи — имена столбцов, значения — списки данных столбцов;
            # «records» — список словарей, где каждый словарь представляет строку DataFrame;
            # «index» — ключи — индексы DataFrame, значения — словари с парами «ключ-значение» для каждой строки;
            # «split» — словарь с ключами «индекс», «колонки» и «данные».

            return dict_list

    except Exception:
        return []

# if __name__ == '__main__':
    # transact_new = read_func_CSV("../data/transactions.csv")
    # print(transact_new)
print(read_func_Excel("../data/transactions_excel.xlsx"))
# print(df.shape)
# print(df.head())