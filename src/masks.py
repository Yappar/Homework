def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""

    if card_number == "" or card_number[-17] != " " or card_number[-16:].isdigit() is False:
        return "Номер введен неверно"
    else:
        return f"{card_number[:-17]} {card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def get_mask_account(mask_account: str) -> str:
    """Функция маскировки номера банковского счета"""

    if mask_account == "" or mask_account[-21] != " " or mask_account[-20:].isdigit() is False:
        return "Номер введен неверно"
    else:
        return f"{mask_account[:-20]}**{mask_account[-4:]}"


# if __name__ == "__main__":
#     card_number = input("введите номер карты: 7158300734726758: ")
#     print(get_mask_card_number(card_number))
#     mask_account = input("введите номер счета: 35383033474447895560 :")
#     print(get_mask_account(mask_account))
