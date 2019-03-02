#Mamy trzy typy for. 1) for in, 2) for enumerate, 3) for range
#zlicz wystąpienia literek w tekście. Użyj słownika
#Jak sprawdzić, czy dany klucz jest w słowniku?
#if klucz in słownik:
#Poszczegolne literki beda kluczami w danym slowniku
#Dlaczego slownik? Bo jezeli wystapi literka a 10 razy to w naszym slownik['a'] == 10
#Trzeba sprawdzić czy dana literka w słowniku już jest, jeśli nie ma to trzeba dodać wartość 1.
#1. Tworzymy tekst (dane wejściowe)
#2. Tworzymy słownik (wystąpienia = dict())
#3. Pętla
#4. Print (wystąpienia)
#5. W pętli trzeba wpisac wystapienia[literka]

tekst = "Ala ma kota"
wystapienia = dict()
for literka in tekst:
    if literka in wystapienia:
        wystapienia[literka] += 1
    else:
        wystapienia[literka] = 1
print(wystapienia)
    


