#open(NAZWA_PLIKU, TRYB)
#NAZWA_PLIKU -- string
# TRYB -- string ('r', 'w', 'a', ew. z dodatkowym znakiem 't' lub 'b')
# (np. 'rt', 'wb', etc.)
# r - read, w - write, a - append, t - text, b - bytes 


f = open('nowy_plik.txt', 'w')
f.write('To zostanie wpisane do pliku.')
f.close()