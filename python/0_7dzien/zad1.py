#Napisz program edytortekstu
#w którym pozwolisz użytkownikowi stworzyć plik o wybranej nazwie i o wybranej treści
#1. Spytać usera o nazwę pliku
#2. Spytać o treść.
#3. Utworzyc plik i zapisać
#input()
#tresc = tresc + "\n"
#tresc += "\n"


#pytam o nazwe pliku:
nazwa_pliku = input("Podaj nazwę pliku: ")
#pytam o treść pliku:
tresc = input("Podaj treść Twojego pliku: ")
tresc = tresc + '\n'
#tworze plik, tj. otwieram plik literka w sluzy za WRITE w pliku. f.write wpisuje zadana tresc pod zmienna:
with open(nazwa_pliku, 'w') as f:
    f.write(tresc)