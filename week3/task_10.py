s = input()
i = -2
first = s.find('f')
second = s.find('f', first + 1)
if second != -1:
    print(first, s.rfind('f'))
elif first != -1:
    print(first)
