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
