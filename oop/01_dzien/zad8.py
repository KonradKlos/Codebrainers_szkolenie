szesciany []

for x in range (1, 101):
	szesciany.append(x **3)
#krótsza wersja
szesciany = [x**3 for x in range (1, 101)]

kwadraty = [el ** 2 for el in range(10) if el &% 2 == 0]
print(kwadraty)
