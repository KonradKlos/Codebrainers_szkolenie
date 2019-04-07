kwadraty = [x**2 for x in range (0,101) if x % 5 ==0 or  x % 9 ==0]
kwadraty2 = [y for y in kwadraty if (y% 5 ==0) and (y% 9 == 0)]
print(kwadraty2)
