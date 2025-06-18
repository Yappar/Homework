import json


def operations_transform(operations_file: list) -> list:
    """
    Функция, которая принимает на вход путь до JSON-файла из директории data (из json
    в данные python) и возвращает список словарей
    с данными о финансовых транзакциях в виде списка.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список [].
    """
    try:
        with open(operations_file, encoding="utf-8") as json_file:
            operations_list = json.load(json_file)
            return operations_list
    except json.JSONDecodeError:
        return []
    except TypeError:
        return []
    except KeyError:
        return []
    except ValueError:
        return []
    except FileNotFoundError:
        return []


# print(operations_transform("../data/operations.json"))
