def naszafunkcja(m):
    # 'wynik' to zmienna używana tylko w funkcji i nie istnieje poza nią
    wynik = m+2
    # return zwraca wartość zmiennej "wynik"
    return wynik
# wartosc obliczona przez funkcję "naszafunkcja" jest zwracana
# i zapisywana do zmiennej "wartość"
wartosc = naszafunkcja("Piotr")
print(wartosc)

wartosc = naszafunkcja("Marek")
print(wartosc)