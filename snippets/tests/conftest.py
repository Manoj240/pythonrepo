import pytest

@pytest.fixture(autouse=True)
def mock_test_add_numbers(mocker):
    return mocker.patch("test_snippets.add_test_numbers", return_value=10)

@pytest.fixture()
def mock_test_second_add_numbers(mocker):
    return mocker.patch("test_snippets.add_test_second_numbers", return_value=15)

@pytest.fixture()
def mock_test_multiply(mocker):
    return mocker.patch("test_snippets.multiply_numbers", return_value=99)

@pytest.fixture()
def mock_test_add_even_only(mocker):
    return mocker.patch("snippetswithmultiplefunctions.is_even", return_value=True)

    # return AttrDict(
    #     "test",
    #     {
    #         "is_even_mock": is_even_mock,
    #     },
    # )