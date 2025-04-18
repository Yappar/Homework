from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(c_b_account: str) -> str:
    """Функция, которая возвращает строку с замаскированным номером"""
    if c_b_account[-17].isdigit() == True:
    # len_list = ""
    # for symbol in c_b_account:
    #     if symbol.isdigit() == True:
    #         len_list += symbol
    # if len(len_list) == 16:
        return f"{c_b_account[:-20]}{get_mask_account(c_b_account)}"
    else:
        return f"{c_b_account[:-16]}{get_mask_card_number(c_b_account)}"

def get_date(data_input: str) -> str:
    """Функция, которая возвращает строку с датой в формате (ДД.ММ.ГГГГ)"""
    return f"{data_input[8:10]}.{data_input[5:7]}.{data_input[:4]}"

if __name__ == '__main__':
    c_b_account = input("введите номер карты или счета: ")
    print(mask_account_card(c_b_account))

    data_input = input("Введите дату:")
    print(get_date(data_input))
