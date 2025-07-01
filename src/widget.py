from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(c_b_account: str) -> str:
    """Функция, которая возвращает строку с замаскированным номером"""

    # if c_b_account[:4] == "Счет": # Переделал под домашку 13_2
    if "Счет" in str(c_b_account):
        mask_variant = get_mask_account(c_b_account)
    else:
        mask_variant = get_mask_card_number(c_b_account)
    return str(mask_variant)


def get_date(data_input: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате (ДД.ММ.ГГГГ) "11.03.2024"
    2023-09-05T11:30:32Z"""
    # if data_input == "" or data_input[4] != "-" or len(data_input) != 26:
    #     return "Дата введена не верно"
    return f"{data_input[8:10]}.{data_input[5:7]}.{data_input[:4]}"


if __name__ == "__main__":
    #     c_b_account = input("введите номер карты или счета: ")
    #     print(mask_account_card(c_b_account))
    #
    data_input = input("Введите дату:")
    print(get_date(data_input))
