def inna (tekst):
    wystapienia = dict()
    for literka in tekst:
        if literka in wystapienia:
            wystapienia[literka] += 1
        else:
            wystapienia[literka] = 1
    return wystapienia
wlasna = inna("Ala ma kota")
print (wlasna)