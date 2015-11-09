def digit_sum(n: int) -> int:
    if n // 10 == 0:
        return n
    return (n % 10) + digit_sum(n // 10)

print(digit_sum(2**1000))