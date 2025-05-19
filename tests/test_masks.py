import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                                   ("MasterCard 71583007347267582123", "Номер введен неверно"),
                                                   ("", "Номер введен неверно"),
                                                   ("Visa Platinum 89909visa3665229", "Номер введен неверно")])


def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize("mask_account, expected", [("Счет 64686473678894779589", "Счет **9589"),
                                                   ("Счет 353830334222274447895560", "Номер введен неверно"),
                                                   ("", "Номер введен неверно"),
                                                   ("Счет 3538303visa4447895560", "Номер введен неверно")])
def test_get_mask_account(mask_account, expected):
    assert get_mask_account(mask_account) == expected
    #
    # with pytest.raises(TypeError):
    #     calculate_tax(100, 2, 3, 1)
