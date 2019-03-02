# Mamy ciąg: [0, 1, 1, 2, 3, 5, 8]
#             ^ n=0             ^ n=6
# Wypisz m-ty wyraz ciągu.
# lista = [0,1]
#x(n) = x(n-1) + x(n-2)
#------------
#lista.append()
#range(2, m+1)
#for (i=2; i++; i<m+1) {}


lista = [0,1] 
m = 10
for i in range(2, m+1):
    #lista[i] = lista[i-1] + lista[i-2]
    lista.append(lista[i-1] + lista[i-2])
print(lista[m])


