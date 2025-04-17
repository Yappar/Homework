card_number = input("введите номер карты: ")
mask_account = input("введите номер счета: ")


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:16]}"


def get_mask_account(mask_account: str) -> str:
    """Функция маскировки номера банковского счета"""
    return f"**{mask_account[16:20]}"
