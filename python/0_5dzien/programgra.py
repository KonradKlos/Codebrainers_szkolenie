
#Brainstorming 
#1. Funkcja do losowania liczb z danego zakresu
    #-> import random
    #-> random.randint(0,100)
#2. Wprowadzenie danych do programu przez użytkownika
#3. Wyświetlanie na ekranie
#4. Komunikaty
#5. Pętla
#6. Sprawdzanie poprawności danych
#7. Ilość prób (ograniczona -> Prowadzi do Game Over)


#random.randrange(start,stop[,step]) trzeci kroki domyślnie jest opcjonalny.
#random.randint(a,b) -> (a, b+1) - czyli jesli podam 0,100 to bedzie do 100 włącznie.
#trzeba użyć pętli while

import random 
losowa_liczba = random.randint(0,100)

zgadniete = False
ilosc_prob = 1
imie = input("Wpisz swoje imię: ")
print("WITAJ W GRZE!", imie)
print("Musisz odgadnąć wylosowaną przez komputer liczbę w maksymalnie 7-miu krokach.")

while (not zgadniete):
    uzyt_zgaduje = input('Podaj liczbe: ')
    uzyt_zgaduje = int(uzyt_zgaduje)
    if ilosc_prob >= int(7):
        print("GAME OVER. Przekroczyłeś liczbę prób :( ")
        print("Komputer wylosował liczbę: ", losowa_liczba)
        break
    if uzyt_zgaduje == losowa_liczba: #sprawdzenie czy zgadniete
        print("Brawo odgadłeś liczbę! Ta liczba to: ", losowa_liczba)
        print("Zgadłeś w próbie numer: ", ilosc_prob)
        break
    else:
        print("Spróbuj ponownie")
        print("Liczba pozostałych prób: ", 7-(ilosc_prob))
        ilosc_prob += 1
        continue
        


    #zmienic:zgadniete
    #zmienic: ilosc_prob
    # komunikat: statysyki ("Zgadłeś w 5 próbie")
    # jeśli się nie uda to komunikat, żę przegrałeś..