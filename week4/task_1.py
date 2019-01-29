def min4(a, b, c, d):
    res = min(a, b)
    res = min(res, c)
    return min(res, d)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))
