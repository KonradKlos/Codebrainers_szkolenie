lista = range(101)
for zmienna in lista:
    if zmienna %15 == 0:
        print(zmienna, "FIZZBUZZ")
    if zmienna %5 == 0:
        print(zmienna, "BUZZ")
    if zmienna %3 == 0:
        print(zmienna, "FIZZ")
    