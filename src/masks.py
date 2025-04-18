# card_number = input("введите номер карты: 7158300734726758")
# mask_account = input("введите номер счета: 35383033474447895560 :")


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    return f"{card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def get_mask_account(mask_account: str) -> str:
    """Функция маскировки номера банковского счета"""
    return f"**{mask_account[-4:]}"
