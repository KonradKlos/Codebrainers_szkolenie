#stan, imie, nazwisko - to atrybuty konta
#info wpłata, wypłata - to metody konta
#numer konta - atrybut

class KontoBankowe:
    def __init__(self,nazwisko,stan=0):
        self.nazwisko = nazwisko
        self.stan = stan
    
    def info(self):
        print("Konto bankowe", self.nazwisko, "<", "stan:", self.stan, ">")
    
    def wplac(self, kwota):
        self.stan += kwota

    def wyplac(self, kwota):
        self.stan -= kwota


jk = KontoBankowe ("Jan Kowalski")

jn = KontoBankowe ("Janusz Nowak", 1000)

jk.info()
jn.info()

jk.wplac(2000)
jk.wyplac(1500)

jk.info()