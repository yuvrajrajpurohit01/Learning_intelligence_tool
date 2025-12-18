import pytest
from data_loader import load_data

def test_invalid_file_type():
    try:
        load_data("data.txt")
    except ValueError as e:
        assert "CSV" in str(e)
