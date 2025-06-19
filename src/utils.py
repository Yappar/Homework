import json
import logging

from decorators import log

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


@log(filename="../logs/utils.log")
def operations_transform(operations_file: list) -> list:
    """
    Функция, которая принимает на вход путь до JSON-файла из директории data (из json
    в данные python) и возвращает список словарей
    с данными о финансовых транзакциях в виде списка.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список [].
    """
    try:
        logger.info("открываем JSON файл")
        with open(operations_file, encoding="Windows-1251") as json_file:
            operations_list = json.load(json_file)
            return operations_list
    except json.JSONDecodeError as ex:
        logger.info(f"произошла ошибка: {ex}")
        return []
    except TypeError as ex:
        logger.info(f"произошла ошибка: {ex}")
        return []
    except KeyError as ex:
        logger.info(f"произошла ошибка: {ex}")
        return []
    except ValueError as ex:
        logger.info(f"произошла ошибка: {ex}")
        return []
    except FileNotFoundError as ex:
        logger.info(f"произошла ошибка: {ex}")
        return []


print(operations_transform("../data/operations.json"))
