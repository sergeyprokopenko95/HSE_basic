x = list(map(int, input().split()))
max_element = x[0]
max_index = 0
for i in range(len(x)):
    if x[i] >= max_element:
        max_element = x[i]
        max_index = i
print(max_element, max_index, sep=' ')
