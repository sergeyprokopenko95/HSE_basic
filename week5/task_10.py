x = list(map(int, input().split(' ')))
prev_elem = x[0]
for i in range(1, len(x)):
    if x[i] > prev_elem:
        print(x[i], end=' ')
    prev_elem = x[i]
