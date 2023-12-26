import pytest
from snippets import add_test_numbers

@pytest.mark.addtest
class TestAddFunctions:

    @pytest.mark.parametrize("a, b, expected_result", [(1, 2, 3),(0, 0, 0),])
    def test_add_numbers_with_multiple_combinations(self, a, b, expected_result):
        result = add_test_numbers(a, b)
        assert result == expected_result

    @pytest.mark.skip(reason="Test is not ready yet")
    def test_skip_add_numbers_with_multiple_combinations():
        # This test will be skipped.
        assert True