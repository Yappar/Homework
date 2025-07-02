import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("", "no input data!"),
        ("Visa Platinum 89909visa3665229", "number was entered incorrectly"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "mask_account, expected",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 353830334222274447895560", "number was entered incorrectly"),
        ("", "number was entered incorrectly"),
        ("Счет 3538303visa4447895560", "number was entered incorrectly"),
    ],
)
def test_get_mask_account(mask_account: str, expected: str) -> None:
    assert get_mask_account(mask_account) == expected
