def sredniawazona(wartosci, wagi):
    licznik = 0
    mianownik = 0
    for wartosc, waga in zip(wartosci, wagi):
        licznik = wartosc * waga + licznik 
        mianownik = waga + mianownik
    wynik = licznik/mianownik
    return wynik 
print(sredniawazona([3, 4], [4, 4])

#Brainstorming 
#1. Funkcja do losowania liczb z danego zakresu
#2. Wprowadzenie danych do programu przez użytkownika
#3. Wyświetlanie na ekranie
#4. Komunikaty
#5. Pętla
#6. Sprawdzanie poprawności danych
#7. Ilość prób (ograniczona -> Prowadzi do Game Over)