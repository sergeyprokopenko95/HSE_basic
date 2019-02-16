x = list(map(int, input().split()))
min_elem = x[0]
min_index = 0
max_elem = x[0]
max_index = 0
for i in range(len(x)):
    if x[i] < min_elem:
        min_elem = x[i]
        min_index = i
    elif x[i] > max_elem:
        max_elem = x[i]
        max_index = i
x[min_index], x[max_index] = x[max_index], x[min_index]
print(*x)
