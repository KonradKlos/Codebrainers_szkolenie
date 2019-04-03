kwadraty = [el**2 for el in range (1,10000) if el % 5 ==0 or  el % 9 ==0]
kwadraty = map(lambda x: x % 5 ==0 and x % 9 ==0)
print(kwadraty)

