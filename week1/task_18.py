n = int(input()) % 10000001
sec = 60*60*24
time = n % sec
h = time // (60 * 60)
print(h)
time = time - h * 60 * 60
m = time // 60
print(m)
time = time - m * 60
s = time
print(s)
print(h, ':', m // 10, m % 10, ':', s // 10, s % 10, sep='')
