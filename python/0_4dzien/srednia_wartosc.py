#Oblicz średnią wartość dla całej listy wartości numerycznych
# *: oblicz inne rodzaje średnich niż arytmetyczną.
lista = [3,5,7,8,9,10]
suma = 0
i = len(lista)
for liczba in lista:
    suma = suma + liczba
print("Średnia wartość dla całej listy to: ", suma/i) 
#Dzieli zapisaną sumę przez liczbę elementów w liście. Liczba elementów zapisana jest w zmiennej i.
