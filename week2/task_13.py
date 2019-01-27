a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    if a >= b + c:
        print('impossible')
    elif a*a < b*b + c*c:
        print('acute')
    elif a*a > b*b + c*c:
        print('obtuse')
    else:
        print('rectangular')
elif b >= c and b >= a:
    if b >= a + c:
        print('impossible')
    elif b*b < a*a + c*c:
        print('acute')
    elif b*b > a*a + c*c:
        print('obtuse')
    else:
        print('rectangular')
elif c >= a and c >= b:
    if c >= a + b:
        print('impossible')
    elif c*c < b*b + a*a:
        print('acute')
    elif c*c > b*b + a*a:
        print('obtuse')
    else:
        print('rectangular')
