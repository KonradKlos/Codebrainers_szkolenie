#stan, imie, nazwisko - to atrybuty konta
#info wpłata, wypłata - to metody konta
#numer konta - atrybut

class KontoBankowe:
    def __init__(self,nazwisko,stan=0):
        self.nazwisko = nazwisko
        self.stan = stan
    
    def info(self):
        print("Konto bankowe", self.nazwisko, "<", "stan konta:", self.stan, ">")
    
    def wplac(self, kwota):
        self.stan += kwota
        print("Dla konta",self.nazwisko,"wpłacono:", self.stan)

    def wyplac(self, kwota):
        self.stan -= kwota
        print("Dla konta",self.nazwisko,"wypłacono:", self.stan)

    def przelew (self, Wartosc_przelewu):
        print("Wprowadź kwotę przelewu dla", self.nazwisko, ":") 
        self.Wartosc_przelewu = (int(input()))
        self.stan += self.Wartosc_przelewu



jk = KontoBankowe ("Jan Kowalski")

jn = KontoBankowe ("Janusz Nowak", 1000)

jk.info()
jn.info()

print("-------------------------------------------------")

jk.wplac(2000)
jk.wyplac(1500)

print("-------------------------------------------------")
print("Saldo po operacjach:")
jk.info()
jn.info()

print("-------------------------------------------------")

jk.przelew(0)
jn.przelew(0)

jk.info()
jn.info()