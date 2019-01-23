h = int(input())
a = int(input())
b = int(input())
h = h - b - 1
steps = (h // (a - b) + ((a - b) // (a - b)))
print(steps)
