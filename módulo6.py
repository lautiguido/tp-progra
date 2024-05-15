def repetido(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

lista = [1, 2, 3, 4, 5]
print(repetido(lista))
