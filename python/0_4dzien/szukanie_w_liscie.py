uczestnik = 'Piotr'
dziennik = [
    'Piotr',
    'Konrad',
    'Mateusz',
    'Przemek',
    'Olga',
]
for uczen in dziennik: #przechodząc przez wszystkich w dzienniku, wszyscy będą przypisywani do zmiennej
    if uczen == uczestnik: #jeśli uczeń będzie 'równać się' 
        print("Znalazłem")
    else:
        print('Nie znalazłem')

# drugi program z nieco zmienioną petlą if.
uczestnik = 'Piotr'
dziennik = [
    'Piotr',
    'Konrad',
    'Mateusz',
    'Przemek',
    'Olga',
]
if uczen in dziennik: #przechodząc przez wszystkich w dzienniku, wszyscy będą przypisywani do zmiennej
        print("Znalazłem")

# trzeci program, gdzie enum pokazuje linię w której znaleziono dane.
uczestnik = 'Piotr'
dziennik = [
    'Piotr',
    'Konrad',
    'Mateusz',
    'Przemek',
    'Olga',
]
    
for pozycja, uczen in enumerate(dziennik):
    if uczen == uczestnik:
        print(pozycja, ": ", uczen)
        