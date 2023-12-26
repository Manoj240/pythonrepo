import pytest
from snippetswithmultiplefunctions import add_even_numbers

@pytest.mark.addtest
class TestAddEvenFunctions:

    def test_add_even_numbers_only_pass_with_mock(self, mock_test_add_even_only):
        result = add_even_numbers(1,3)
        assert result == 4


    def test_add_even_numbers_only_fail(self, mock_test_add_even_only):
        # Here 2 is even, but we changed is_even output behaviour by below linw
        mock_test_add_even_only.return_value = False
        
        result = add_even_numbers(2,3)
        assert result == "An error occurred: Given input is not even 2"
