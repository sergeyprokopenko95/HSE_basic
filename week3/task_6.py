p = float(input())
x = float(input())
y = float(input())

coast = x * 100 + y
coast += coast*(p / 100)
print(int(coast) // 100, int(coast % 100))
