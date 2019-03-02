#Sprawdź, czy zadany tekst jest palindromem. 
#tekst = "piotrrtoip"
#
#
#
tekst = "piotrrtoip"
czy_palindrom = True #funkcja ta sprawdza, czy dany tekst JEST PALINDROMEM.
for pozycja, sprawdzenie in enumerate(tekst): # pozycja, sprawdzenie - to pozycja każdej z liter, natomiast sprawdzenie (co ile) w tym wypadku co -1.
    if tekst[pozycja] == tekst[-pozycja-1]:
        pass
    else:
        czy_palindrom = False
        break
if czy_palindrom:
        print("Tak to jest palindrom")
else:
        print ("To nie jest palindrom")