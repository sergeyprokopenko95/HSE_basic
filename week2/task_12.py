x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1 < 8) and (y1 < 8):
    if x2 > x1:
        if ((x2 - x1) % 2 == 1) and (((y2 - y1) % 2) == 1):
            print('YES')
        elif ((x2 - x1) % 2 == 0) and (((y2 - y1) % 2) == 0):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
