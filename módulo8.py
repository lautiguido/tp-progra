def decimales(lista):
    if lista==0:
        return 0

    suma=sum(lista)

    promedio=suma/len(lista)

    return promedio



lista=[1.5, 2.5, 3.5, 4.5, 5.5]
print(decimales(lista))