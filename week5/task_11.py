x = list(map(int, input().split()))
min_positive = 1001
for i in range(len(x)):
    if x[i] > 0 and x[i] < min_positive:
        min_positive = x[i]
print(min_positive)
