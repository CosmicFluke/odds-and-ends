def sum_digits(n: int) -> int:
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

def factorial(n: int) -> int:
    if n == 1:
        return n
    return n * factorial(n - 1)

print(sum_digits(factorial(100)))