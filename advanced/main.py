
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


# utils.py
def get_user_number() -> float:
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("Invalid number, please try again.")


def get_operation() -> str:
    while True:
        operation = input("Enter an operation (+, -, *, /): ")
        if operation in ("+", "-", "*", "/"):
            return operation
        print("Invalid operation, please try again.")


# main.py
from operations import add, subtract, multiply, divide
from utils import get_user_number, get_operation

number_1 = get_user_number()
number_2 = get_user_number()
operation = get_operation()

while operation == "/" and number_2 == 0:
    print("cannot divide by zero")
    number_2 = get_user_number()

if operation == "+":
    result = add(number_1, number_2)
elif operation == "-":
    result = subtract(number_1, number_2)
elif operation == "*":
    result = multiply(number_1, number_2)
elif operation == "/":
    result = divide(number_1, number_2)

print(f"{number_1} {operation} {number_2} = {result}")
