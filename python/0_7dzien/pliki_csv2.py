import csv 

with open ('przykladowy.csv', 'r') as f:
    czytacz = csv.DictReader(f)
    for wiersz in czytacz:
        print(wiersz)
        print (wiersz['Year'])
        print(wiersz['Score'])
        print(wiersz['Title'])
        