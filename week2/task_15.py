a, b, c = int(input()), int(input()), int(input())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > c:
    a, c = c, a
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > c:
    a, c = c, a
print(a, b, c)
