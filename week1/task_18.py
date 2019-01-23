n = int(input()) % 10000001
sec = 60*60*24
time = n % sec
h = time // (60 * 60)
m = (time % 24) // 60
s = (time % 24) % 60
print(h, ':', m // 10, m % 10, ':', s // 10, s % 10, sep='')
