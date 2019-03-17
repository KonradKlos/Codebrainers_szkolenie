L = [["","",""],
    ["","",""],
    ["","",""]]
def rysuj_tablice(tablica):
    for x, wiersz in enumerate(tablica):
        for y, v in enumerate(wiersz):
            if not v.strip():
                v = ' '
            if y < len(wiersz) - 1:
                print(v, '| ', end='')
            else:
                print(v)
        if x < len(tablica) - 1:
            print('-' * 9)

gracz = "o"
for i in range(9):
    print("Kolej gracza: ", gracz)
    wiersz = int(input("Podaj wiersz: "))
    kolumna = int(input("Podaj kolumnę: "))
    L[wiersz][kolumna] = gracz
    
    rysuj_tablice(L)
    if gracz == "o":
        gracz = "x"
    elif gracz == "x":
        gracz = "o"


#zmienic typ petli na while, zabezpieczamy sie przed trafieniem w zapelnione pole i wykorzystujemy do tego ifa .if
#try + continue 
#














#skopiować rysowanie tablicy kolko krzyzyk z githuba Piotra.