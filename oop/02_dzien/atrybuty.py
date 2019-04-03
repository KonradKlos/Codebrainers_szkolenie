#Zaimplementuj klase produkt, ktora ma dwa atrybuty cene i nazwe (_init_),
# stworz metode details ktora wyswietla informacje o produkcie.

class Produkt:
    cena = ""
    nazwa = ""

    def __init__(self, cena, nazwa):
        self.cena = cena
        self.nazwa = nazwa

    def details(self):
        print("Produkt", self.nazwa, self.cena)

Jogurt = Produkt ("Jogurt", "12zł")
Jogurt.details()
