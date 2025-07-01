import re
from src.transaction_reader import read_func_CSV, read_func_Excel
from src.utils import operations_transform
from collections import Counter


def process_bank_search(operations: str, search_string: str):
    """Функция принимает список банковских операций (список словарей из функций operations_transform() из
    utils, read_func_CSV() из transactions_reader, read_func_Excel() из transactions_reader) и
    строку поиска и выводит список словарей содержащие данные из строки поиска"""

    if ".json" in operations:
        operations_list = operations_transform(operations)
    elif ".csv" in operations:
        operations_list = read_func_CSV(operations)
    elif ".xlsx" in operations:
        operations_list = read_func_Excel(operations)
    search_list = []
    for operation in operations_list:
        operation_state = str(operation.get("state"))
        search_result = re.search(search_string, operation_state, flags=re.IGNORECASE)
        if search_result is not None:
            search_list.append(operation)
    return search_list


def process_bank_operations(operations: str, categories: list):
    """Функция принимает список банковских операций (список словарей из функций operations_transform() из
    utils, read_func_CSV() из read_func_Excel, excel_operation() из transactions_reader) и
    список категорий операций и выводит словарь, в котором ключи — это названия категорий, а значения
    — это количество операций в каждой категории"""
    if "json" in operations:
        operations_list = operations_transform(operations)
    elif "csv" in operations:
        operations_list = read_func_CSV(operations)
    elif "xlsx" in operations:
        operations_list = read_func_Excel(operations)
    else:
        return "incorrect input data!"
    categories_list = []
    for operation in operations_list:
        operation_state = str(operation.get("description"))
        for category in categories:
            search_result = re.search(category, operation_state, flags=re.IGNORECASE)
            if search_result is not None:
                categories_list.append(operation.get("description"))
    counted_category_list = Counter(categories_list)
    return str(counted_category_list)


if __name__ == "__main__":
    # print(process_bank_search("C:\\Users\\yappa\\Homework\\data\\transactions_excel.xlsx", "PENDING"))
    print(process_bank_operations('../data/operations.json',
                      ['Перевод организации', 'Перевод с карты на карту', 'Перевод со счета на счет']))
