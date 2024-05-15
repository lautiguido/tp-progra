def LaMasCorta(lista1,lista2):
    if len (lista1)<=len (lista2):
        return lista1
    else:
        return lista2

lista1=[1,2,3,4,5]
lista2=[1,2,3,5]
print(LaMasCorta(lista1,lista2))