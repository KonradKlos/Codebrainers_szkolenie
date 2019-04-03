class Uczen:
    imie = ""
    nazwisko = ""
    PESEL = 123456778

    def info(self):
        print("Uczeń", self.imie, self.nazwisko)

piotr = Uczen()
piotr.nazwisko = "Banaszkiewicz"
piotr.info()

natalia = Uczen()
natalia.imie = "Natalia"
natalia.info()
