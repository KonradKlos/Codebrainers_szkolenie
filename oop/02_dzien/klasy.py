class NazwaKlasy: # w klasach powinno się stosować CAMELCASE, zaczynamy od dużej i każde słowo zaczynamy od wielkiej litery
    def nazwa_metody(self, argument1, argument2): # piewszy argument w metodzie, zawsze powinien być self!
        print("arg1:", argument1)
        print("arg2:", argument2)
        print(self.text)


obiekt = NazwaKlasy()
obiekt.text= "Obiekt"
instancja = NazwaKlasy() # obiekt i instancja to egzemplarze na których można operować w klasach.
instancja.text = "Instancja"

obiekt.nazwa_metody("Piotr", "B")
instancja.nazwa_metody("Python", "v3.7")