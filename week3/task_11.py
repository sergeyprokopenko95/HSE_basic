s = input()
first = s.find('h')
last = s.rfind('h')
res = s[:first] + s[last+1:]
print(res)
