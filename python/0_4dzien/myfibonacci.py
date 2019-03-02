
def fibonacci(m):
    lista = [0,1] 
    for i in range(2, m+1):
        lista.append(lista[i-1] + lista[i-2])
    mtyelement = lista[-1]
    return mtyelement
mty = fibonacci(10)
print(mty)
