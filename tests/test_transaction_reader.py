from unittest.mock import mock_open, patch

from src.transaction_reader import read_func_CSV, read_func_Excel


def test_csv_operations():
    mock_file = mock_open(read_data="incorrect csv")
    with patch("builtins.open", mock_file):
        result = read_func_CSV("../data/transactions.csv")
        assert result == []


def test_excel_operation():
    mock_file = mock_open(read_data="incorrect excel")
    with patch("builtins.open", mock_file):
        result = read_func_Excel("../data/transactions_excel.xlsx")
        assert result == []
