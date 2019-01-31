def power(a, n):

    if n > 0:
        if n % 2 == 0:
            return a * power(a**2, n / 2)
        else:
            return a * power(a, n - 1)
    return a

print(power(2, 10))
