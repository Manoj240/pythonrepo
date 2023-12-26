import pytest
from snippets import add_test_numbers, add_test_second_numbers, multiply_numbers, multiply_only_numbers

# fixture to run - python -m pytest -k "my_fixture"
@pytest.mark.addtest
class TestAddFunctions:

    def test_add_numbers_with_mock(self):
        result = add_test_numbers(2, 3)
        assert result == 10

    # This fixture (mock_test_second_add_numbers) doesn't have autouse, so we added as arg
    def test_second_add_numbers_with_mock(self, mock_test_second_add_numbers):
        result = add_test_second_numbers(2, 3)
        assert result == 15

@pytest.mark.multiplytest
class TestMultiplyFunctions:

    def test_multiply_numbers(self):
        result = multiply_numbers(2, 3)
        assert result == 6

    # This fixture (mock_test_second_add_numbers) doesn't have autouse, so we added as arg
    def test_second_add_numbers_with_mock(self, mock_test_multiply):
        result = multiply_numbers(2, 3)
        assert result == 99

    def test_multiply_different_type_numbers(self):
        result = multiply_numbers(5, None)
        assert result == "unsupported operand type(s) for *: 'int' and 'NoneType'"

@pytest.mark.multiplytest
class TestMultiplyOnlyNumbers:

    def test_multiply_only_numbers(self):
        result = multiply_only_numbers(2, 3)
        assert result == 6

    def test_multiply_non_numbers_with_error(self):
        with pytest.raises(ValueError, match="Both arguments must be numbers"):
            multiply_only_numbers(5, None)

    with pytest.raises(ValueError) as exc_info:
        result = multiply_only_numbers("2", 3)
    assert str(exc_info.value) == "Both arguments must be numbers (int or float)."
