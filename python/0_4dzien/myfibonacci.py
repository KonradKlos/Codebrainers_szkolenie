
def fibonacci(m):
    #wymagania m:
    # 1. to musi być liczba
    # 2. liczba >= 2
    if not isinstance(m,int):
        raise Exception("To nie jest int")
    if m < 2:
        raise Exception("Liczba musi być większa od 1")
    lista = [0,1] 
    for i in range(2, m+1):
        lista.append(lista[i-1] + lista[i-2])
    mtyelement = lista[-1]
    return mtyelement
try:
    mty = fibonacci(10)
    print(mty)
except Exception:
    print("Liczba musi być równa bądź większa od 2!")

#
#try:
#    print(fib(1))
#except Exception as exc:
#    print("Wystapil blad: ")
#    print(exc.args[0])