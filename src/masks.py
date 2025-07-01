import logging

from src.decorators import log


logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(
    "C:\\Users\\yappa\\Homework\\logs\\masks.log"
)
# C:\\Users\\yappa\\Homework\\logs\\masks.log или ../logs/masks.log
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


# @log(filename="../logs/masks.log")
def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    if isinstance(card_number, float):
        card_number = str(card_number)
    if card_number == "":
        return "no input data!"
    elif card_number == "" or card_number[-17] != " " or card_number[-16:].isdigit() is False:
        logger.info("введен некорректный номер карты")
        return "number was entered incorrectly"

    else:
        logger.info(" маскировка номера банковской карты")
        return f"{card_number[:-17]} {card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


# logger.info("печать результаты функции маскировки")
# print(get_mask_card_number("Maestro 1596837868705199"))


# @log(filename="../logs/masks.log")
def get_mask_account(mask_account: str) -> str:
    """Функция маскировки номера банковского счета"""

    if mask_account == "" or mask_account[-21] != " " or mask_account[-20:].isdigit() is False:
        logger.info("введен некорректный номер счета")
        return "number was entered incorrectly"
    else:
        logger.info(" маскировка номера счета")
        return f"{mask_account[:-20]}**{mask_account[-4:]}"

if __name__ == "__main__":
    print(get_mask_account("Счет 64686473678894779589"))
    logger.info("печать результаты функции маскировки")
    print(get_mask_card_number("Maestro 1596837868705199"))
