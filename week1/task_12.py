# cost rubles
a = int(input()) % 10000
# cost cent
b = int(input()) % 10000
# count
n = int(input()) % 10000

result = ((a * 100) + b) * n
print(result // 100, result % 100)
