try:
    a = 1   
    b = 0
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Nie dziel przez zero!")
    
try:
    lista = [22222222]
    print(lista[123])
except IndexError:
    print("Błędny parametr zadeklarowanej listy!")

try:
    slownik = {'Konrad', 'Bartek'}
    print(slownik('Grzesiek'))
except TypeError:
    print("Nie możesz modyfikować tupli!")

try:
    proba(6)
    print(proba())
except NameError:
    print("Nazwa nie została zdefiniowana")

try:
    liczba = 10
    liczba()
except TypeError:
    print("Funkcja dodawania listy potrzebuje co najmniej jednego argumenty. Nie wpisałeś żadnego.")