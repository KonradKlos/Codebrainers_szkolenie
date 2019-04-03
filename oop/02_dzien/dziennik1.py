class Uczen:
    imie = ""
    nazwisko = ""
    PESEL = 123456778

    def _init_(self, imie, nazwisko, PESEL):
        self.imie = imie
        self.nazwisko = nazwisko
        self.PESEL = PESEL
    
    def into(self):
        print("Uczeń", self.imie, self.nazwisko)

piotr = Uczen("Piotr", "B", 121212413123123)
piotr.info()

natalia = Uczen("Natalia", "N", 124123123512)
natalia.info()
