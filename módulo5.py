def sonFactores(n,lista):
    for factor in lista:
        if n % factor != 0:
            return False
    return True

n=20
lista=[3,4,5,10]
print(sonFactores(n,lista))
