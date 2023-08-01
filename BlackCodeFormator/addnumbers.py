def add_numbers(number1: int, number2: int) -> int:
    return number1 + number2


def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    if number == 0:
        return 1
    return number * factorial(number - 1)


print(add_numbers(5, 10))
print(factorial(6))
