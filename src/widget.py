from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(c_b_account: str) -> str:
    """Функция, которая возвращает строку с замаскированным номером"""

    if c_b_account[:4] == "Счет":
        return f"{get_mask_account(c_b_account)}"
    else:
        return f"{get_mask_card_number(c_b_account)}"


def get_date(data_input: str) -> str:
    """Функция, которая возвращает строку с датой в формате (ДД.ММ.ГГГГ)"""

    if data_input == "" or data_input[4] != "-" or len(data_input) != 26:
        return "Дата введена не верно"
    else:
        return f"{data_input[8:10]}.{data_input[5:7]}.{data_input[:4]}"


# if __name__ == "__main__":
#     c_b_account = input("введите номер карты или счета: ")
#     print(mask_account_card(c_b_account))
#
#     data_input = input("Введите дату:")
#     print(get_date(data_input))
