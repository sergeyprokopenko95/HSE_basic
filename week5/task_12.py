c = int(input())
x = list(map(int, input().split(' ')))
n = int(input())
to_close = 0
dif = 2001
for i in range(len(x)):
    if abs(x[i] - n) < dif:
        to_close = x[i]
        dif = abs(x[i] - n)
print(to_close)
