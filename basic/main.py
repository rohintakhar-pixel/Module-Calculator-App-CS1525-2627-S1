
def add(number_1: float, number_2: float) -> float:
    """
    Add two numbers together.

    Args:
        number_1 (float): The first number.
        number_2 (float): The second number.

    Returns:
        float: The sum of number_1 and number_2.
    """
    return number_1 + number_2


def subtract(number_1: float, number_2: float) -> float:
    """
    Subtract the second number from the first.

    Args:
        number_1 (float): The first number.
        number_2 (float): The second number.

    Returns:
        float: The difference between number_1 and number_2.
    """
    return number_1 - number_2


def multiply(number_1: float, number_2: float) -> float:
    """
    Multiply two numbers together.

    Args:
        number_1 (float): The first number.
        number_2 (float): The second number.

    Returns:
        float: The product of number_1 and number_2.
    """
    return number_1 * number_2


def divide(number_1: float, number_2: float) -> float:
    """
    Divide the first number by the second.

    Args:
        number_1 (float): The number to be divided.
        number_2 (float): The number to divide by.

    Returns:
        float: The result of dividing number_1 by number_2.
    """
    return number_1 / number_2


# main.py
from operations import add, subtract, multiply, divide

number_1 = 10
number_2 = 5

print(f"{number_1} + {number_2} = {add(number_1, number_2)}")
print(f"{number_1} - {number_2} = {subtract(number_1, number_2)}")
print(f"{number_1} * {number_2} = {multiply(number_1, number_2)}")
print(f"{number_1} / {number_2} = {divide(number_1, number_2)}")
