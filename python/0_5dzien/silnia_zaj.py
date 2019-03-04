def silnia(n):
    wynik = 1 #należy zacząć od 1, ponieważ nie można zacząć od 0.
    for liczba in range(2,n+1): #n+1, bo jesli podasz dowolną liczbę to na niej powinno się skończyć.
        wynik *= liczba
    return wynik
wynik = silnia(3)
print(wynik)