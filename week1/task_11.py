n = int(input()) % 10000000
h = n // 60
h = h % 24
m = n % 60
print(h, m)
