def is_even(number):
    """
    Check if a number is even.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0


def add_even_numbers(a, b):
    if not is_even(a):
        return f"An error occurred: Given input is not even {a}"
    return a + b

# res = add_even_numbers(1,3)
# print(res)