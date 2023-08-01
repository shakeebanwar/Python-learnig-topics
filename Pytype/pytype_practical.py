def add_numbers(a: int, b: int) -> int:
    return a + b


def factorial(n: int) -> int:

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)


#correct inputs
print(add_numbers(5, 5))
print(factorial(6))

#wrong inputs
# print(add_numbers("8", 5))
# print(factorial("9"))


