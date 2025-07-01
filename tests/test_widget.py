import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "c_b_account, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("", "number was entered incorrectly"),
        ("Visa Platinum 89909visa3665229", "number was entered incorrectly"),
        ("Maestro 1596837868705199000", "number was entered incorrectly"),
        ("Счет 646864736788visa9589", "number was entered incorrectly"),
        ("Счет 646864736788947795890000", "number was entered incorrectly"),
    ],
)
def test_mask_account_card(c_b_account: str, expected: str) -> None:
    assert mask_account_card(c_b_account) == expected


@pytest.mark.parametrize(
    "data_input, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-09-05T11:30:32Z", "05.09.2023"),


    ],
)
def test_get_date(data_input: str, expected: str) -> None:
    assert get_date(data_input) == expected
