def pitagoras(a,b):
    wynik = a**2 + b**2 
    return wynik**(1/2) # ponieważ wynik jest do kwadratu, trzeba go spierwiastkować. 
print(pitagoras(3,4))