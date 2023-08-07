def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci number is not defined for negative indices.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


#correct inputs
print(fibonacci(15))

#wrong inputs
#print(fibonacci("6"))