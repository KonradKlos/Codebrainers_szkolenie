def kwadratowa (a,b,c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b-delta**(1/2)/2*a)
        x2 = (-b+delta**(1/2)/2*a)
        return x1, x2
    if delta == 0:
        x0 = -b /(2*a)
        return x0
    if delta < 0:
        return None
print(kwadratowa(1,1,10))