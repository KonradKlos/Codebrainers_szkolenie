
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
ilosc_prob = 0
#Mozna komunikat- witaj w grze itp itd. Wszystko z printa.
while (not zgadniete) and (ilosc_prob ,7): #Gdy warunek pierwszy nie bedzie spelniony to petla sie konczy.if __name__ == "__main__":
    uzyt_zgaduje = input('Podaj liczbe: ')
    uzyt_zgaduje = int(uzyt_zgaduje)
    #if uzyt_zgaduje == losowa_liczba - sprawdzenie czy zgadniete
    #komunikat
    #zmienic:zgadniete
    #zmienic: ilosc_prob
    # komunikat: statysyki ("Zgadłeś w 5 próbie")
    # jeśli się nie uda to komunikat, żę przegrałeś..