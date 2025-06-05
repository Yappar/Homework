import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "c_b_account, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("", "Номер введен неверно"),
        ("Visa Platinum 89909visa3665229", "Номер введен неверно"),
        ("Maestro 1596837868705199000", "Номер введен неверно"),
        ("Счет 646864736788visa9589", "Номер введен неверно"),
        ("Счет 646864736788947795890000", "Номер введен неверно"),
    ],
)
def test_mask_account_card(c_b_account: str, expected: str) -> None:
    assert mask_account_card(c_b_account) == expected


@pytest.mark.parametrize(
    "data_input, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024vis-11T02:26:18.671407", "Дата введена не верно"),
        ("", "Дата введена не верно"),
        ("2024-03-11T02:26:18.671407123", "Дата введена не верно"),
    ],
)
def test_get_date(data_input: str, expected: str) -> None:
    assert get_date(data_input) == expected
