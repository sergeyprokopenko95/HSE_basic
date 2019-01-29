def IsPointInCircle(x, y, xc, yc, r):
    d_x = xc - x
    d_y = yc - y
    res = d_x ** 2 + d_y ** 2 <= r ** 2
    return res


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
