def filter_by_state(list_of_dict: list, state: str = "EXECUTED") -> list:
    """
        функция, которая принимает список словарей и опционально значение для ключа
    state(по умолчанию 'EXECUTED') и возвращает новый список словарей,
     содержащий только те словари, у которых ключ state соответствует указанному значению
    """
    finish_list_dict = []
    for dict in list_of_dict:
        if dict["state"] == state:
            finish_list_dict.append(dict)
    return finish_list_dict
