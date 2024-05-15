m = int(input("Ingrese el primer número: "))
n = int(input("Ingrese el segundo número: "))

print("Pares de números entre", m, "y", n, "con dos ciclos:")
for i in range(m, n+1):
    for j in range(m, n+1):
        print(i, j)


