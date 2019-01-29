from math import sqrt


def IsPrime(n):
    i = 2
    while i <= int(sqrt(n)):
        if n % i == 0:
            return True
        i += 1
    return False


n = int(input())
if IsPrime(n):
    print('NO')
else:
    print('YES')
