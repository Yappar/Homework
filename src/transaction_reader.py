import csv

import pandas as pd


# @log(filename='../data/logs/tran_reader.log')
def read_func_CSV(file_path: str) -> list[dict]:
    """
    Функция принимает файл CSV и возвращает список словарей
    заголовок (id;state;date;amount;currency_name;currency_code;from;to;description)
    """

    try:
        with open(file_path, encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            transaction_list = []
            for row in reader:
                for head, content in row.items():
                    head_list = head.split(";")
                    content_list = content.split(";")
                    transaction_dict = {}
                    for i in range(len(head_list)):
                        key = head_list[i]
                        value = content_list[i]
                        transaction_dict[key] = value
                transaction_list.append(transaction_dict)
            return transaction_list
    except Exception:
        return []


# @log(filename="../data/logs/tran_reader.log")
def read_func_Excel(file_path: str) -> list[dict]:
    """Функция принимает файл Excel и возвращает список словарей"""
    try:
        with open(file_path):
            df = pd.read_excel(file_path, dtype=str)
            """df.astype(str).mask(df.isna(), None) преобразует все значения в столбце DataFrame в строки,
            а пропущенные значения (пустые ячейки в Excel) заменяет на None."""
            df = df.astype(str).mask(df.isna(), None)
            # Загружаем Excel-файл в DataFrame
            dict_list = df.to_dict(orient="records")
            # Преобразуем DataFrame в список словарей
            # «list» — ключи — имена столбцов, значения — списки данных столбцов;
            # «records» — список словарей, где каждый словарь представляет строку DataFrame;
            # «index» — ключи — индексы DataFrame, значения — словари с парами «ключ-значение» для каждой строки;
            # «split» — словарь с ключами «индекс», «колонки» и «данные».

            return dict_list

    except Exception:
        return []


if __name__ == "__main__":
    # transact_new = read_func_CSV("../data/transactions.csv")
    # print(transact_new)
    print(read_func_Excel("../data/transactions_excel.xlsx"))
    # print(df.shape)
    # print(df.head())
