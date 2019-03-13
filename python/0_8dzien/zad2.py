def min (L):
    """Funkcja szukająca minimalnej wartości.
    
    Funkcja pobiera listę wartości i iteruje po nich,
    żeby znaleźć najmniejszą.
    >>> min([1,2,3,4])
    1

    >>> min([])
    Traceback (most recent call last):
        ...
    IndexError: list index out of range

    >>> min("Piotr")
    'P'

    >>> min(None)
    Traceback (most recent call last):
        ...
    TypeError: 'NoneType' object is not subscriptable


    >>> min[1,"P"]
    Traceback (most recent call last):
        ...
    TypeError: 'function' object is not subscriptable

    >>> min([2.33, 3.14])
    2.33

    >>> min([-3,4,-5])
    -5

    >>> min([0])
    0

    """
    min_value = L[0]
    for a in L:
        if a < min_value:
            min_value = a
    return min_value
#wbić sobie to do głowy. 
#Warunek ten zapewnia, że wszystko w tym warunku, 
#wykona się tylko i wyłącznie,
# jeżeli bezpośrednio ten plik w pythonie uruchomimy.
# $ python zad2.py
# 
if __name__ == "__main__": 
    import doctest
    doctest.testmod()

#print(min([]))


#[1,2,3,4] -> 1  
#[] -> IndexError
#"Piotr" -> "P"
#None - TypeError
#[1,"P"] -> TypeError
#[2.33,3.14] -> 2.33
#[-3,4,-5] -> -5
#[0]-> 0