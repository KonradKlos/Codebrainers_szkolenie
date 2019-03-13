import random 
losowa_liczba = random.randint(0,100)
from utils import HASLA, szubienica, maskowanie
zgadniete = False
nieudane_proby = 0
literki = []
losowe_haslo = random.choice(HASLA)
ilosc_prob = 0
imie = input("Wpisz swoje imię: ")
print("WITAJ W GRZE!", imie)
print("Komputer wylosuje dla Ciebie nazwę filmu. Twoim zadaniem jest odgadnięcie jego nazwy.")

while (not zgadniete) and (ilosc_prob < 9):
    #print(szubienica(ilosc_prob))
    uzyt_zgaduje = input('Wpisz literkę: ')
    literki.append(uzyt_zgaduje)
    ilosc_prob += 1
    if uzyt_zgaduje.lower() not in losowe_haslo.lower():
        nieudane_proby += 1
        print(szubienica(ilosc_prob))
    print("Dotychczasowe hasło wygląda następująco: ", maskowanie(losowe_haslo, literki))
    if nieudane_proby > 0:
        print(szubienica(ilosc_prob))
print("Niestety, przegrałeś. Wylosowana nazwa filmu to: ",(losowe_haslo))