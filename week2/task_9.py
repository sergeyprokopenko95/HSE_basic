n = int(input())
if n < 100:
    if n == 1 or ((n > 20) and n % 10 == 1):
        print(str(n), 'korova')
    elif (n < 5) or (n > 20 and 1 < n % 10 < 5):
        print(str(n), 'korovy')
    else:
        print(str(n), 'korov')
