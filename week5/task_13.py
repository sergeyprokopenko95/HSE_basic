x = list(map(int, input().split(' ')))
if len(x) % 2 == 0:
    for i in range(0, len(x), 2):
        x[i], x[i + 1] = x[i + 1], x[i]
else:
    for i in range(0, len(x) - 1, 2):
        x[i], x[i + 1] = x[i + 1], x[i]
print(*x)
