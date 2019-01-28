a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

det = a*d - b*c
det_x = e*d - f*b
det_y = a*f - e*c
x = det_x / det
y = det_y / det
print(x, y)
