import pytest
from snippets import add_numbers

@pytest.fixture
def mock_add_numbers(mocker):
    print("in fixture")
    return mocker.patch("snippets.add_numbers", return_value=10)


def test_add_numbers_with_mock(mock_add_numbers):
    result = add_numbers(2, 3)
    assert result == 10
