def fibonacci(number: int) -> int:
    if number < 0:
        raise ValueError("Fibonacci number is not defined for negative indices.")
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(15))
