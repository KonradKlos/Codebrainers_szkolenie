import csv

with open('przykladowy.csv', 'r') as f:
    czytacz = csv.reader(f)
    for wiersz in czytacz:
        print(wiersz)