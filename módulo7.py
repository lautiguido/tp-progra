def DondeAparece(blanco,lista):
  for i in range(len(lista)):
    if lista[i] == blanco:
            return i
  return -1

blanco=8
lista=[1,2,3,4,5,6,7]
print(DondeAparece(blanco,lista))