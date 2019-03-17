import csv

years = []
scores = []

with open ('przykladowy.csv', 'r') as f:
    czytacz = csv.DictReader(f)
    for wiersz in czytacz:
        #1 Konwertowanie na int
        year = int(wiersz['Year'])
        score = int(wiersz['Score'])

        #2 Dodawanie do listy
        years.append(year)
        scores.append(score)

        #3 Wypisz każdą listę, by można było sprawdzić
minimalny_wynik_rok = years[0]
maksymalny_wynik = scores[0]
minimalny_wynik = scores[0]
maksymalny_wynik_rok = years[0]

for rok, wynik in zip(years, scores):
    print('W roku', rok, 'miał wynik', wynik)
    # czy ten wynik jest mniejszy od najmniejszygo dotychczasowego wyniku?