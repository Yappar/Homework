c_b_account = input("введите номер счета:")


def mask_account_card(c_b_account: str) -> str:
    """Функция, которая возвращает строку с замаскированным номером"""
    len_list = 0
    mask_name = ""
    for symbol in c_b_account:
        if symbol.isalpha() == True:
            mask_name += symbol
        if symbol.isdigit() == True:
            len_list += 1
    if len_list == 16:
        return f"{mask_name} {c_b_account[-16:-12]} {c_b_account[-12:-10]}** ****{c_b_account[-4:]}"
    else:
        return f"{mask_name} **{c_b_account[-4:]}"


print(mask_account_card(c_b_account))

data_input = input("Введите дату:")


def get_date(data_input: str) -> str:
    """Функция, которая возвращает строку с датой в формате (ДД.ММ.ГГГГ) """
    return f"{data_input[8:10]}.{data_input[5:7]}.{data_input[:4]}"


print(get_date(data_input))
