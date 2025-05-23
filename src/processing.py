from typing import Union


def filter_by_state(list_of_dict: list, state: str = "EXECUTED") -> Union[str, list]:
    """
        функция, которая принимает список словарей и опционально значение для ключа
    state(по умолчанию 'EXECUTED') и возвращает новый список словарей,
     содержащий только те словари, у которых ключ state соответствует указанному значению
    """
    finish_list_dict = []
    for dict_l in list_of_dict:
        if dict_l.get("state"):
            if dict_l["state"] == state:
                finish_list_dict.append(dict_l)

    if finish_list_dict == []:
        return "Введены некорректные данные"
    else:
        return finish_list_dict


def sort_by_date(list_of_dict: list, sort_p: bool = True) -> Union[str, list]:
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки"""

    for dict_l in list_of_dict:
        if "date" not in dict_l:
            return "Нет данных"
        if len(dict_l["date"]) != 26:
            return "Введены некорректные данные"
    sorted_list_of_dict = sorted(list_of_dict, key=lambda dict: dict["date"], reverse=sort_p)
    if sorted_list_of_dict == []:
        return "Нет данных"
    return sorted_list_of_dict


# if __name__ == "__main__":
#     list_of_dict = [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ]
#     print(filter_by_state(list_of_dict))
#     print(sort_by_date(list_of_dict))
