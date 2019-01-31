def sum(a, b):
    a += 1
    b -= 1
    if b > 0:
        return sum(a, b)
    else:
        return a


a = int(input())
b = int(input())
print(sum(a, b))
