sito = [True] * 100 # po tej linijce mamy liste 100 wartości TRUE
sito[0] = False # wykluczamy 0 oraz 1, ponieważ przyjmujemy, że nie sa one liczbami pierwszymi.
sito[1] = False # sprawdzamy do 50, ponieważ powyżej 50 wykracza już poza Nasz zakres.
for i in range(2,51): # Range wygeneruje nam liste od 2 do 50. Zatem w każdym przebiegu tej pętli będziemy mieć kolejną liczbę z listy, Będzie ona za każdym razem zapisywana w i.
    n = 2
    wielokrotnosc = n * i
    while wielokrotnosc < 100:
        sito[wielokrotnosc] = False
        n += 1
        wielokrotnosc = n * i
for indeks, wartosc in enumerate(sito):
    if wartosc == True:
        print("Liczba pierwsza: ", indeks)