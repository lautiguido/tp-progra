# Solicitar al usuario que ingrese dos números enteros m y n
m = int(input("Ingrese el primer número: "))
n = int(input("Ingrese el segundo número: "))

# Iterar a través de los números desde m hasta n (inclusive)
for i in range(m, n + 1):
    # Iterar a través de los números desde i hasta n (inclusive) para cada número i
    for j in range(i, n + 1):
        # Imprimir el par de números i y j
        print(i, j)
