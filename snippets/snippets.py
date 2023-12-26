def add_test_numbers(a, b):
    return a + b

def add_test_second_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    """
    This function multiplies two numbers and handles exceptions.
    """
    try:
        result = a * b
    except TypeError as e:
        return str(e)  # Return the exception message as a string
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
    return result

# In math_operations.py

def multiply_only_numbers(a, b):
    """
    This function multiplies two numbers and raises custom exceptions.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers (int or float).")
    
    result = a * b
    return result

