def IsPointInSquare(x, y):
    res = x >= -1 and x <= 1 and y >= -1 and y <= 1
    return res


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
